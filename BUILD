genrule(
    name = "catch_github",
    srcs = [],
    outs = ["catch.h"],
    cmd = "wget https://raw.githubusercontent.com/philsquared/Catch/develop/single_include/catch.hpp -O $@"
)

cc_library(
    name = "manacher",
    srcs = ["manacher.cc"],
)

cc_test(
	name = "manacher_test",
	srcs = ["catch.h"],
	deps = [":manacher"]
)
