# lg_srcml_cpp_caller

simple bindings for srcML, when used with C++ code.

Provides:

````python
def to_cpp(
    xml_str: str,
    encoding_src: str = "utf-8",
    encoding_xml: str = "utf-8"
    ) -> Optional[str]:
    pass


def to_srcml(
    cpp_code: str,
    include_positions: bool = True,
    encoding_src: str = "utf-8",
    encoding_xml: str = "utf-8"
    ) -> Optional[str]:
    pass
````

Based on [scikit_build_example](https://github.com/pybind/scikit_build_example) for [litgen](https://github.com/pthom/litgen)
