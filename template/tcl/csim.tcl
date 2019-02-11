open_project $env(HLS_TARGET)

# add source files
foreach f $env(HLS_SOURCE) {
    add_files $f -cflags "-Iinclude/"
}

# add simulation files
foreach f $env(HLS_TEST) {
    add_files -tb $f -cflags "-Iinclude/ -Itest/include/"
}

open_solution $env(HLS_SOLUTION)

csim_design
