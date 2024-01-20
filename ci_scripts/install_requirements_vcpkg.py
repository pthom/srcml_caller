import os
import subprocess
import platform
import sys


this_dir = os.path.dirname(__file__)
repository_dir = os.path.realpath(this_dir + "/../")
os.chdir(repository_dir)


def vcpkg_path():
    return repository_dir + "/vcpkg"


def required_libraries():
    return ["libxml2", "libxslt", "libarchive"]


def bootstrap_vcpkg():
    if os.path.exists("vcpkg"):
        print("vcpkg already exists, skipping bootstrap")
        return

    print("Cloning vcpkg...")
    os.system("git clone https://github.com/Microsoft/vcpkg.git")

    print("Bootstrapping vcpkg...")
    if os.name == "nt":
        os.system("./vcpkg/bootstrap-vcpkg.bat")
    else:
        os.system("./vcpkg/bootstrap-vcpkg.sh")


def is_inside_cibuildwheel():
    return os.environ.get("CIBUILDWHEEL") == "1"


def cibuildwheel_host_platform():
    return os.environ.get("_PYTHON_HOST_PLATFORM")


def cibuildwheel_is_building_arm():
    return "arm" in cibuildwheel_host_platform()


def shall_build_for_arm():
    if not is_inside_cibuildwheel():
        is_arm = "arm" in platform.machine().lower()
        return is_arm
    else:
        return cibuildwheel_is_building_arm()


def platform_static_lib_linkage_triplet() -> str:
    os_info = platform.system()
    is_64_bits = sys.maxsize > 2 ** 32
    is_arm = shall_build_for_arm()
    print(f"os_info={os_info}, is_64_bits={is_64_bits}, is_arm={is_arm}")
    # sys.exit(1)

    if not is_64_bits:
        raise RuntimeError("32 bits is not supported")

    if os_info == "Windows":
        return "x64-windows-static" if not is_arm else "arm64-windows-static"
    elif os_info == "Linux":
        return "x64-linux" if not is_arm else "arm64-linux"
    elif os_info == "Darwin":
        return "x64-osx" if not is_arm else "arm64-osx"


def install_vcpkg_packages():
    for library in required_libraries():
        triplet = platform_static_lib_linkage_triplet()
        print(f"Installing {library} for {triplet}...")
        cmd = f"./vcpkg/vcpkg install {library}:{triplet}"
        print(cmd)
        subprocess.check_call(cmd, shell=True)


def vcpkg_cmake_args():
    triplet = platform_static_lib_linkage_triplet()
    return [
        f"-DCMAKE_TOOLCHAIN_FILE={repository_dir}/vcpkg/scripts/buildsystems/vcpkg.cmake",
        f"-DVCPKG_TARGET_TRIPLET={triplet}",
    ]


def main():
    bootstrap_vcpkg()
    install_vcpkg_packages()


if __name__ == "__main__":
    main()
