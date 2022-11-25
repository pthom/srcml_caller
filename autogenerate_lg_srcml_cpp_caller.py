import os

from codemanip import amalgamated_header

import litgen


THIS_DIR = os.path.dirname(__file__)
EXTERNAL_DIR = THIS_DIR + "/external"
CPP_LIB_DIR = EXTERNAL_DIR + "/srcml_cpp_caller"
CPP_GENERATED_PYBIND_DIR = THIS_DIR + "/bindings"
assert os.path.isdir(CPP_LIB_DIR)
assert os.path.isdir(CPP_GENERATED_PYBIND_DIR)


def make_amalgamated_header():
    options = amalgamated_header.AmalgamationOptions()

    options.base_dir = EXTERNAL_DIR
    options.local_includes_startwith = "srcml_cpp_caller/"
    options.include_subdirs = ["srcml_cpp_caller"]
    options.main_header_file = "srcml_cpp_caller.h"
    options.dst_amalgamated_header_file = THIS_DIR + "/srcml_cpp_caller_amalgamation.h"

    amalgamated_header.write_amalgamate_header_file(options)


def autogenerate():
    output_cpp_pydef_file = CPP_GENERATED_PYBIND_DIR + "/pybind_srcml_cpp_caller.cpp"
    output_stub_pyi_file = CPP_GENERATED_PYBIND_DIR + "/lg_srcml_cpp_caller/__init__.pyi"

    # Configure options
    options = litgen.LitgenOptions()

    include_dir = THIS_DIR + "/external/srcml_cpp_caller"
    header_file = include_dir + "/srcml_cpp_caller.h"
    litgen.write_generated_code_for_file(options, header_file, output_cpp_pydef_file, output_stub_pyi_file)


if __name__ == "__main__":
    autogenerate()
