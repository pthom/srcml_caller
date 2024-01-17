add_library(libsrcml_caller STATIC libsrcml_caller.cpp libsrcml_caller.h)
target_include_directories(libsrcml_caller PUBLIC ${CMAKE_CURRENT_LIST_DIR}/..)
# Under windows, auto __declspec(dllexport)
if (WIN32)
    set_target_properties(libsrcml_caller PROPERTIES WINDOWS_EXPORT_ALL_SYMBOLS ON)
endif()
target_link_libraries(libsrcml_caller PUBLIC libsrcml_static)
target_include_directories(libsrcml_caller PRIVATE ${CMAKE_CURRENT_LIST_DIR}/../../external/srcML/src/parser)


# Unix compile options: fPIC + pthread
if (UNIX)
    target_compile_options(libsrcml_caller PRIVATE -fPIC)
    target_link_libraries(libsrcml_caller PUBLIC pthread)
    target_compile_options(libsrcml_caller PUBLIC -pthread)
endif()
