# srcml_caller

simple bindings for srcML, when used with C++ code.

Provides:

````python
from typing import Optional
import enum


class CodeLanguage(enum.Enum):
    c = enum.auto()            # (= 0)
    c_sharp = enum.auto()      # (= 1)
    c_plus_cplus = enum.auto() # (= 2)
    java = enum.auto()         # (= 3)
    objective_c = enum.auto()  # (= 4)


def to_code(
        xml_str: str,
        encoding_src: str = "utf-8",
        encoding_xml: str = "utf-8"
) -> Optional[str]:
    pass


def to_srcml(
        code: str,
        language: CodeLanguage,
        include_positions: bool = True,
        encoding_src: str = "utf-8",
        encoding_xml: str = "utf-8"
) -> Optional[str]:
    pass
````

Based on [scikit_build_example](https://github.com/pybind/scikit_build_example) for [litgen](https://github.com/pthom/litgen)

# Install instructions

````
git clone https://github.com/pthom/srcml_caller.git
cd srcml_caller
git submodule update --init # will fetch srcML submodule
pip install -v .
````

# Development build instructions

## Install requirements


### Linux

#### Download and install a newer binary version of cmake (cmake 3.24 is required)

For example:
````
# This is where cmake will be put
MY_BIN_DIR=~/bin

# (select your arch below)
CMAKE_BIN_URL=https://cmake.org/files/v3.25/cmake-3.25.0-linux-x86_64.tar.gz
# CMAKE_BIN_URL=https://cmake.org/files/v3.25/cmake-3.25.0-linux-aarch64.tar.gz
curl -L $CMAKE_BIN_URL  > cmake_new.tgz
tar xvfz cmake_new.tgz
rm cmake_new.tgz
echo "export PATH=$MY_BIN_DIR/cmake-3.25.0-linux-aarch64/bin:$PATH" >> ~/.bashrc
echo "export PATH=$MY_BIN_DIR/cmake-3.25.0-linux-aarch64/bin:$PATH" >> ~/.zshrc
````

#### Install requirements

Follow instructions on srcML repo: https://github.com/srcML/srcML/blob/master/BUILD.md

#### Install requirements for Ubuntu

From https://github.com/srcML/Docker/blob/ubuntu_latest/base/Dockerfile

````
sudo apt-get update && sudo apt-get install --no-install-recommends -y \
    curl \
    zip \
    g++ \
    make \
    ninja-build \
    libxml2-dev \
    libxml2-utils \
    libxslt1-dev \
    libarchive-dev \
    libssl-dev \
    libcurl4-openssl-dev \
    cpio \
    man \
    file \
    dpkg-dev
````

You can also run ci_scripts/install_requirements_ubuntu.sh, which does exactly this.


# Build
````bash
git submodule update --init
````

Unix and MacOS
````bash
python3 -m venv venv
source venv/bin/activate
pip install pybind11
mkdir build
cd build
cmake .. -DPYTHON_EXECUTABLE=../venv/bin/python
````

Windows
````bash
python3 -m venv venv
venv\Scripts\activate
pip install pybind11
mkdir build
cd build
cmake .. -DPYTHON_EXECUTABLE=c:\FULL\PATH\TO\venv\Scripts\python.exe
````
