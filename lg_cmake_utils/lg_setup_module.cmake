function(lg_setup_module
    bound_library
    python_native_module_name
    python_wrapper_module_name
    )
    # Parameters explanation, with an example: let's say we want to build binding for a C++ library named "foolib",
    #
    #    bound_library               : name of the C++ for which we build bindings ("foolib")
    #    python_native_module_name   : name of the native python module that provides bindings (for example "_foolib")
    #    python_wrapper_module_name  : name of the standard python module that will import the native module (for example "foolib")

    target_link_libraries(${python_native_module_name} PRIVATE ${bound_library})

    # Set python_native_module_name install path to "." (required by skbuild)
    install(TARGETS ${python_native_module_name} DESTINATION .)
    # Copy the python module to the project dir post build (for editable mode)
    set(python_native_module_dest ${CMAKE_CURRENT_SOURCE_DIR}/bindings/${python_wrapper_module_name}/$<TARGET_FILE_NAME:${python_native_module_name}>)
    set(bound_library_dest ${CMAKE_CURRENT_SOURCE_DIR}/bindings/${python_wrapper_module_name}/lib/$<TARGET_FILE_NAME:${bound_library}>)
    add_custom_target(
        ${python_native_module_name}_deploy_editable
        ALL
        COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:${python_native_module_name}> ${python_native_module_dest}
        COMMAND ${CMAKE_COMMAND} -E copy $<TARGET_FILE:${bound_library}> ${bound_library_dest}
        DEPENDS ${python_native_module_name}
    )
endfunction()