#include "srcml_cpp_caller/srcml_cpp_caller.h"
#include <iostream>

int main()
{
    std::string code = R"(
    // Héloïse
    int a = 1;
    )";

    std::string xml = R"(
<unit revision="1.0.0" language="C++" pos:tabs="8">
    <comment type="line" pos:start="2:5" pos:end="2:16">// Héloïse</comment>
    <decl_stmt pos:start="3:5" pos:end="3:14"><decl pos:start="3:5" pos:end="3:13"><type pos:start="3:5" pos:end="3:7"><name pos:start="3:5" pos:end="3:7">int</name></type> <name pos:start="3:9" pos:end="3:9">a</name> <init pos:start="3:11" pos:end="3:13">= <expr pos:start="3:13" pos:end="3:13"><literal type="number" pos:start="3:13" pos:end="3:13">1</literal></expr></init></decl>;</decl_stmt>
    </unit>
)";

    auto r = to_srcml(
    code,
    true,
    "utf-8",
    "utf-8"
    );

    if (r)
        std::cout << r.value() << "\n";


    auto r2 = to_cpp(xml,
                     "utf-8",
                     "utf-8"
                     );
    if (r2)
        std::cout << r2.value() << "\n";

}