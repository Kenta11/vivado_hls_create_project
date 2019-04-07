open_project $env(HLS_TARGET)

# add source files
foreach f $env(HLS_SOURCE) {
    add_files $f -cflags "-Iinclude/ {{COMPILER_ARG}}"
}

# add simulation files
foreach f $env(HLS_TEST) {
    add_files -tb $f -cflags "-Iinclude/ -Itest/include/ {{COMPILER_ARG}}"
}
