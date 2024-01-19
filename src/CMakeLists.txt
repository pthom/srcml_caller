add_subdirectory(libsrcml_caller)

#if (TRUE)
#    # Note srcml_cmd_line is a simple command line to test the library
#    # It is build on apple only, but could be build on other platforms
#    add_executable(srcml_cmd_line srcml_cmd_line.cpp)
#    target_link_libraries(srcml_cmd_line PRIVATE libsrcml_caller)
#endif()