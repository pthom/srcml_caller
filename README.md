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
