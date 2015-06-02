#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.h"
#include "manacher.cc"

TEST_CASE( "Longest palindrome is found", "[findLongestPalindrome]" ) {
  REQUIRE( findLongestPalindrome("").as_string() == "");
  REQUIRE( findLongestPalindrome("a").as_string() == "a");
  REQUIRE( findLongestPalindrome("ab").as_string() == "a");
  REQUIRE( findLongestPalindrome("aa").as_string() == "aa");
  REQUIRE( findLongestPalindrome("aaa").as_string() == "aaa");
  REQUIRE( findLongestPalindrome("aaabbb").as_string() == "aaa");
  REQUIRE( findLongestPalindrome("abaaba").as_string() == "abaaba");
  REQUIRE( findLongestPalindrome("cabcbabcbabcba").as_string() == "abcbabcba");
}
