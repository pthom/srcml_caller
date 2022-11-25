#include "srcml_cpp_caller.h"

#include <srcml.h>
#include <srcml_types.hpp>

#include <string>
#include <optional>
#include <memory>


// inspired from int srcml(const char* input_filename, const char* output_filename)
// inside libsrcml.cpp


std::optional<std::string> to_cpp(
    const std::string& xml_str,
    const std::string& encoding_src,
    const std::string& encoding_xml
)
{
    srcml_set_src_encoding(encoding_src.c_str());
    srcml_set_xml_encoding(encoding_src.c_str());

    std::unique_ptr<srcml_archive> archive(srcml_archive_create());
    srcml_archive_set_src_encoding(archive.get(), encoding_src.c_str());
    srcml_archive_set_xml_encoding(archive.get(), encoding_xml.c_str());

    int status = srcml_archive_read_open_memory(archive.get(), xml_str.c_str(), xml_str.size());
    if (status != SRCML_STATUS_OK)
        return std::nullopt;

    std::unique_ptr<srcml_unit> unit(srcml_archive_read_unit(archive.get()));
    if (!unit)
        return std::nullopt;

    char *buffer;
    size_t buffer_size;
    status = srcml_unit_unparse_memory(unit.get(), &buffer, &buffer_size);
    if (status != SRCML_STATUS_OK)
        return std::nullopt;

    std::string r = buffer;
    return r;
}


std::optional<std::string> to_srcml(
    const std::string& cpp_code,
    bool include_positions,
    const std::string& encoding_src,
    const std::string& encoding_xml
    )
{
    srcml_set_language("C++");
    srcml_set_src_encoding(encoding_src.c_str());
    srcml_set_xml_encoding(encoding_xml.c_str());

    auto archive = srcml_archive_create();
    srcml_archive_set_src_encoding(archive, encoding_src.c_str());
    srcml_archive_set_xml_encoding(archive, encoding_xml.c_str());

    auto unit = srcml_unit_create(archive);
    srcml_unit_set_language(unit, "C++");
    srcml_unit_set_src_encoding(unit, encoding_src.c_str());

    if (include_positions)
    {
        size_t srcml_options = SRCML_OPTION_POSITION;
        srcml_set_options(srcml_options);
        srcml_archive_set_options(archive, srcml_options);
    }

    int status = srcml_unit_parse_memory(unit, cpp_code.c_str(), cpp_code.size());
    bool success = (status == 0);

    std::string r;
    if (success)
    {
        const char* srcml_str = srcml_unit_get_srcml(unit);
        r = srcml_str;
    }

    srcml_unit_free(unit);
    srcml_archive_free(archive);

    if (success)
        return r;
    else
        return std::nullopt;
}


//int main()
//{
//    if (true) // to_srcml
//    {
//        std::string code = "int i = 1;";
//        auto r = to_srcml(code);
//        if (r)
//            printf("%s\n", r.value().c_str());
//        else
//            printf("Error!!!\n");
//    }
//    if(true) // to_cpp
//    {
//        std::string srcml = R"(<unit xmlns="http://www.srcML.org/srcML/src" revision="1.0.0" language="C++" hash="2282bfb857b594a3eacd2216145d1682fb980711"><decl_stmt><decl><type><name>int</name></type> <name>i</name> <init>= <expr><literal type="number">1</literal></expr></init></decl>;</decl_stmt></unit>)";
//        auto r = to_cpp(srcml);
//        if (r)
//            printf("%s\n", r.value().c_str());
//        else
//            printf("Error!!!\n");
//    }
//}
