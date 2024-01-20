import sys
import os

# add the directory containing this file to the python path
this_dir = os.path.dirname(__file__)
sys.path.insert(0, this_dir)
from ci_scripts import install_requirements_vcpkg


from skbuild import setup
from setuptools import find_packages


def get_readme():
    with open("README.md") as f:
        r = f.read()
    return r


install_requirements_vcpkg.bootstrap_vcpkg()
install_requirements_vcpkg.install_vcpkg_packages()
cmake_args = install_requirements_vcpkg.vcpkg_cmake_args()

print("cmake_args", cmake_args)
# sys.exit(1)


setup(
    name="srcml-caller",
    version="0.2.0",
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
