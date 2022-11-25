import sys

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

setup(
    name="lg-srcml-cpp-caller",
    version="0.0.1",
    description="lg-srcml-cpp-caller, simple bindings for srcML, with C++ code",
    long_description="...",
    author="Pascal Thomet",
    author_email="pthomet@gmail.com",
    url="https://github.com/pthom/lg_srcml_cpp_caller",
    packages=(["lg_srcml_cpp_caller"]),
    package_dir={"": "bindings"},
    cmake_install_dir="bindings/lg_srcml_cpp_caller",
    # include_package_data=True,
    package_data={"lg_srcml_cpp_caller": ["py.typed", "*.pyi"]},
    extras_require={"test": ["pytest"]},
    python_requires=">=3.6",
    install_requires=[],
)