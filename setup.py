import sys
import os
import platform

# add the directory containing this file to the python path
this_dir = os.path.dirname(__file__)
sys.path.insert(0, this_dir)


from skbuild import setup
from setuptools import find_packages


this_dir = os.path.dirname(__file__)
repository_dir = this_dir

def get_readme():
    with open("README.md") as f:
        r = f.read()
    return r


def vcpkg_cmake_args_cibuildwheel():
    # Cf .github/workflows/wheels.yml, we only handle those platforms and archs with cibuildwheel
    if platform.system() == "Linux":
        return []

    if platform.system() == "Windows":
        triplet = "x64-windows-static"
    elif platform.system() == "Darwin":
        triplet = "arm64-osx"
    return [
        f"-DCMAKE_TOOLCHAIN_FILE={repository_dir}/vcpkg/scripts/buildsystems/vcpkg.cmake",
        f"-DVCPKG_TARGET_TRIPLET={triplet}",
    ]


is_inside_cibuildwheel = os.environ.get("CIBUILDWHEEL") is not None
if is_inside_cibuildwheel:
    cmake_args = vcpkg_cmake_args_cibuildwheel()
else:
    cmake_args = []
print("cmake_args", cmake_args)


setup(
    name="srcml-caller",
    version="0.4.0",
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
