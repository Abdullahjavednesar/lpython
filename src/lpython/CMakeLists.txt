set(SRC
    semantics/python_ast_to_asr.cpp

    fortran_evaluator.cpp

    pickle.cpp
    python_serialization.cpp

    utils.cpp

    ../bin/tpl/whereami/whereami.cpp
)
if (WITH_XEUS)
    set(SRC ${SRC}
#        fortran_kernel.cpp
    )
endif()
add_library(lfortran_lib ${SRC})
target_link_libraries(lfortran_lib asr lfortran_runtime_static ZLIB::ZLIB)
target_include_directories(lfortran_lib BEFORE PUBLIC ${lfortran_SOURCE_DIR}/src)
target_include_directories(lfortran_lib BEFORE PUBLIC ${lfortran_BINARY_DIR}/src)
if (WITH_XEUS)
    target_link_libraries(lfortran_lib xeus)
endif()
if (WITH_BFD)
    target_link_libraries(lfortran_lib p::bfd)
endif()
if (WITH_LINK)
    target_link_libraries(lfortran_lib p::link)
endif()
if (WITH_EXECINFO)
    target_link_libraries(lfortran_lib p::execinfo)
endif()
if (WITH_LLVM)
    target_link_libraries(lfortran_lib p::llvm)
endif()
#install(TARGETS lfortran_lib
#    RUNTIME DESTINATION bin
#    ARCHIVE DESTINATION lib
#    LIBRARY DESTINATION lib
#)

add_subdirectory(tests)
