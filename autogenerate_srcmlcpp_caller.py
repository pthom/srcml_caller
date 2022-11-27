import os
import litgen




def autogenerate():
    this_dir = os.path.dirname(__file__)
    output_cpp_pydef_file = this_dir + "/bindings/pybind_srcml_caller.cpp"
    output_stub_pyi_file = this_dir + "/bindings/srcml_caller/__init__.pyi"

    # Configure options
    options = litgen.LitgenOptions()

    header_file = this_dir + "/src/libsrcml_caller/libsrcml_caller.h"
    litgen.write_generated_code_for_file(options, header_file, output_cpp_pydef_file, output_stub_pyi_file)


if __name__ == "__main__":
    autogenerate()
