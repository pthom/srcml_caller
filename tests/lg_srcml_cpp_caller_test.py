import srcmlcpp_caller


def test_version():
    assert srcmlcpp_caller.__version__ == "0.0.1"

def test_code():
    import srcmlcpp_caller
    code = """
    // Héloïse
    int a = 1;
    """
    xml = srcmlcpp_caller.to_srcml(code)
    code2 = srcmlcpp_caller.to_cpp(xml)
    assert code2 == code
