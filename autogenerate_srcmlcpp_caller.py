import os
import litgen


THIS_DIR = os.path.dirname(__file__)
EXTERNAL_DIR = THIS_DIR + "/external"
CPP_LIB_DIR = EXTERNAL_DIR + "/libsrcml_caller"
CPP_GENERATED_PYBIND_DIR = THIS_DIR + "/bindings"
assert os.path.isdir(CPP_LIB_DIR)
assert os.path.isdir(CPP_GENERATED_PYBIND_DIR)


def autogenerate():
    output_cpp_pydef_file = CPP_GENERATED_PYBIND_DIR + "/pybind_srcml_caller.cpp"
    output_stub_pyi_file = CPP_GENERATED_PYBIND_DIR + "/srcml_caller/__init__.pyi"

    # Configure options
    options = litgen.LitgenOptions()

    include_dir = THIS_DIR + "/external/libsrcml_caller"
    header_file = include_dir + "/libsrcml_caller.h"
    litgen.write_generated_code_for_file(options, header_file, output_cpp_pydef_file, output_stub_pyi_file)


if __name__ == "__main__":
    autogenerate()
