# srcml_caller

Simple python bindings for [srcML](https://www.srcml.org/).

Provides:

````python
from typing import Optional
import enum


class CodeLanguage(enum.Enum):
    c = enum.auto()            # (= 0)
    c_sharp = enum.auto()      # (= 1)
    c_plus_plus = enum.auto()  # (= 2)
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


def cpp_to_srcml(
        code: str,
        include_positions: bool = True,
        encoding_src: str = "utf-8",
        encoding_xml: str = "utf-8"
) -> Optional[str]:
    pass
````

# Example usage

```
>>> import srcml_caller
>>> srcml_caller.to_srcml("void foo(int v);", srcml_caller.CodeLanguage.c_plus_cplus)

'<unit revision="1.0.0" language="C++" pos:tabs="8"><function_decl pos:start="1:1" pos:end="1:16"><type pos:start="1:1" pos:end="1:4"><name pos:start="1:1" pos:end="1:4">void</name></type> <name pos:start="1:6" pos:end="1:8">foo</name><parameter_list pos:start="1:9" pos:end="1:15">(<parameter pos:start="1:10" pos:end="1:14"><decl pos:start="1:10" pos:end="1:14"><type pos:start="1:10" pos:end="1:12"><name pos:start="1:10" pos:end="1:12">int</name></type> <name pos:start="1:14" pos:end="1:14">v</name></decl></parameter>)</parameter_list>;</function_decl></unit>'
```

# Install instructions (from pypi)

```bash
pip install -v srcml_caller
```


# Install instructions (from source)'

````
git clone https://github.com/pthom/srcml_caller.git
cd srcml_caller
git submodule update --init # will fetch srcML submodule
pip install -v .
````

Note: on windows, you need to first install libxml2 and libxslt with vcpkg, see below:
```bash
# inside the srcml_caller directory:
git clone https://github.com/Microsoft/vcpkg.git
.\vcpkg\bootstrap-vcpkg.bat
.\vcpkg\vcpkg install libxml2:x64-windows-static libxslt:x64-windows-static                                
.\vcpkg\vcpkg install libxml2:x86-windows-static libxslt:x86-windows-static
```      


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

### Unix and MacOS
````bash
python3 -m venv venv
source venv/bin/activate
pip install pybind11
mkdir build
cd build
cmake .. -DPYTHON_EXECUTABLE=../venv/bin/python
````

### Windows

Please clone vcpkg in the same directory as this project, then install libxml2 and libxslt like this:

```bash
git clone https://github.com/Microsoft/vcpkg.git
.\vcpkg\bootstrap-vcpkg.bat
.\vcpkg\vcpkg install libxml2:x64-windows-static libxslt:x64-windows-static                                
.\vcpkg\vcpkg install libxml2:x86-windows-static libxslt:x86-windows-static
```      

````bash
python3 -m venv venv
venv\Scripts\activate
pip install pybind11
mkdir build
cd build
cmake .. -DPYTHON_EXECUTABLE=c:\FULL\PATH\TO\venv\Scripts\python.exe
````
