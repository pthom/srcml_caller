import lg_srcml_cpp_caller


def test_version():
    assert lg_srcml_cpp_caller.__version__ == "0.0.1"


def test_examplelib():
    assert lg_srcml_cpp_caller.add(3, 4) == 7


def test_boxed_type():
    i = lg_srcml_cpp_caller.BoxedInt(3)
    lg_srcml_cpp_caller.inplace_multiply(i)
    assert i.value == 6
