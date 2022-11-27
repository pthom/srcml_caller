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
    name="srcml-caller",
    version="0.0.1",
    description="srcml-caller, simple bindings for srcML, with C++ code",
    long_description="...",
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
)
