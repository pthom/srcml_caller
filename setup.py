import sys
import os


try:
    from skbuild import setup
except ImportError:
    print(
        "Please update pip, you need pip 10 or greater,\n"
        " or you need to install the PEP 518 requirements in pyproject.toml yourself",
        file=sys.stderr,
    )
    raise

from setuptools import find_packages


def get_readme():
    with open("README.md") as f:
        r = f.read()
    return r


# if on windows, set cmake toolchain to use vcpkg
this_dir = os.path.dirname(os.path.realpath(__file__))
if sys.platform == "win32":
    # We could also check that java is installed by checking that "java" is in the path

    if not os.path.isdir(this_dir + "/vcpkg"):
        msg = """
        Please clone vcpkg in the same directory as this project, then install libxml2 and libxslt like this:
        
            git clone https://github.com/Microsoft/vcpkg.git
            .\vcpkg\bootstrap-vcpkg.bat
            .\vcpkg\vcpkg install libxml2:x64-windows-static libxslt:x64-windows-static                                
        """
        raise RuntimeError(msg)

    cmake_args = [
        f"-DCMAKE_TOOLCHAIN_FILE={this_dir}/vcpkg/scripts/buildsystems/vcpkg.cmake",
        "-DVCPKG_TARGET_TRIPLET=x64-windows-static",
    ]
else:
    cmake_args = []


setup(
    name="srcml-caller",
    version="0.1.3",
    description="srcml_caller, simple python bindings for srcML ",
    long_description=get_readme(),
    long_description_content_type="text/markdown",
    author="Pascal Thomet",
    author_email="pthomet@gmail.com",
    url="https://github.com/pthom/srcml_caller",
    packages=(["srcml_caller"]),
    package_dir={"": "bindings"},
    cmake_install_dir="bindings/srcml_caller",
    # include_package_data=True,
    package_data={"srcml_caller": ["py.typed", "*.pyi"]},
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
    install_requires=[],
    cmake_args=cmake_args,
)
