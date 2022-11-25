# Set the rpath for Linux and  MacOS (see https://github.com/pybind/cmake_example/issues/11)
function(lg_target_set_rpath target relative_path)
    set_target_properties(${target} PROPERTIES BUILD_WITH_INSTALL_RPATH TRUE)
    if(UNIX AND NOT APPLE)
        set_target_properties(${target} PROPERTIES INSTALL_RPATH "$ORIGIN/${relative_path}/")
    elseif(APPLE)
        set_target_properties(${target} PROPERTIES INSTALL_RPATH "@loader_path/${relative_path}/")
    endif()
    set_target_properties(${target} PROPERTIES INSTALL_RPATH_USE_LINK_PATH TRUE)
endfunction()


function(lg_target_install_linked_dlls_in_same_folder target)
    if (WIN32)
        install(FILES $<TARGET_RUNTIME_DLLS:${target}> DESTINATION .)
    endif()
endfunction()

