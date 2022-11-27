#include <string>
#include <optional>


std::optional<std::string> to_cpp(
    const std::string& xml_str,
    const std::string& encoding_src = "utf-8",
    const std::string& encoding_xml = "utf-8"
);


std::optional<std::string> to_srcml(
    const std::string& cpp_code,
    bool include_positions = true,
    const std::string& encoding_src = "utf-8",
    const std::string& encoding_xml = "utf-8"
    );
