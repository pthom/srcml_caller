import srcml_caller


def test_version():
    assert srcml_caller.__version__ == "0.0.1"

def test_code():
    import srcml_caller
    code = """
    // Héloïse
    int a = 1;
    """
    xml = srcml_caller.to_srcml(
        code, srcml_caller.CodeLanguage.c_plus_cplus,
        encoding_src="utf-8",
        encoding_xml="utf-8"
        )
    code2 = srcml_caller.to_code(xml, encoding_src="utf-8", encoding_xml="utf-8")
    assert code2 == code
