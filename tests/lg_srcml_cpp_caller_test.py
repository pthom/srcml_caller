import lg_srcml_cpp_caller


def test_version():
    assert lg_srcml_cpp_caller.__version__ == "0.0.1"

def test_code():
    import lg_srcml_cpp_caller
    code = """
    // Héloïse
    int a = 1;
    """
    xml = lg_srcml_cpp_caller.to_srcml(code)
    code2 = lg_srcml_cpp_caller.to_cpp(xml)
    assert code2 == code
