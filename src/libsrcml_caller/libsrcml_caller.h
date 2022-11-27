#include <string>
#include <optional>


enum class CodeLanguage
{
    C = 0,
    CSharp,
    CPlusCplus,
    Java,
    ObjectiveC
};


std::optional<std::string> to_code(
    const std::string& xml_str,
    const std::string& encoding_src = "utf-8",
    const std::string& encoding_xml = "utf-8"
);


std::optional<std::string> to_srcml(
    const std::string& code,
    CodeLanguage language,
    bool include_positions = true,
    const std::string& encoding_src = "utf-8",
    const std::string& encoding_xml = "utf-8"
    );
