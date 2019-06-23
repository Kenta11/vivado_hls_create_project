open_project $env(HLS_TARGET)

# add source files
foreach f $env(HLS_SOURCE) {
    add_files $f -cflags "-Iinclude/ {{COMPILER_ARG}}"
}

# add simulation files
add_files -tb $env(HLS_TEST) -cflags "-Iinclude/ -Itest/include/ {{COMPILER_ARG}}"
