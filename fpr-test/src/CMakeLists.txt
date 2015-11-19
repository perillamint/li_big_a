file(GLOB_RECURSE fpr-test_SOURCES "*.c")
file(GLOB_RECURSE fpr-test_HEADERS "*.h")

#find_package (Threads)
add_executable (fpr-test ${fpr-test_SOURCES})
target_link_libraries (fpr-test ${CMAKE_THREAD_LIBS_INIT})
set_property(TARGET fpr-test PROPERTY C_STANDARD 99)
