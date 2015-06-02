#include <cassert>
#include <iostream>
#include <string>

using std::min;
using std::string;

class StringView {
  public:
    const string& str;
    const int begin;
    const int end;

    StringView(const string& str, const int begin, const int end) :
        str(str), begin(begin), end(end) {}

    string as_string() {
        return str.substr(begin, end - begin - 1);
    }
};

void print(int* arr, int size) {
    for (int i = 0; i < size; ++i) {
        std::cout << i << ' ';
    }
    std::cout << std::endl;
}

string preprocess(const string& input, const char delimiter) {
    const char begin_char = delimiter;
    const char end_char = delimiter;
    const int finalSize = 2 * input.size() + 3;
    string output;
    output.reserve(finalSize);

    char d = begin_char;
    for (char character : input) {
        output.push_back(d);
        output.push_back(character);
        d = delimiter;
    }
    output.push_back(end_char);

    return output;
}

StringView findLongestPalindrome(const string& input_text) {
    const string& text = preprocess(input_text, '#');

    // p[i] stores the longest palindrome centered at i
    int p[text.size()];
    p[0] = 0;
    int max_p_index = 0;
    int max_p_value = 0;

    auto update_max = [&max_p_index, &max_p_value](int index, int value) {
        if (value > max_p_value) {
            max_p_index = index;
            max_p_value = value;
        }
    };

    // center and right indices of the rightmost-reaching palindrome
    int center = 0;
    int right = 0;

    for (int i=1 ; i < text.size() - 1 ; i++) {
        // Update p[i] using the palindrome centered around i's mirror
        if (i <= right) {
            const int mirror = center - (i - center);
            const int distance_to_right = right - i;
            p[i] = min(p[mirror], distance_to_right);
            update_max(i, p[i]);
        } else {
            p[i] = 0;
        }

        // Expand palindrome around center
        for (int left = i - p[i] - 1, right = i + p[i] + 1 ;
                left >= 0 && right < text.size();
                left--, right++) {
            p[i]++;
            update_max(i, p[i]);
        }

        // Update rightmost-reaching palindrome
        if (i + p[i] > right) {
            center = i;
            right = i + p[i];
        }
    }

    print(p, text.size());


    int inclusive_begin, exclusive_end;
    if (max_p_index % 2 == 0) {
        // even-length palindrome
        assert(max_p_value % 2 == 0);

        const int right_center = max_p_index / 2;
        inclusive_begin = right_center - (max_p_value / 2);
        exclusive_end = right_center + (max_p_value / 2) + 1;
    } else {
        // odd-length palindrome
        assert(max_p_value % 2 == 1);

        const int center = max_p_index / 2;
        inclusive_begin = center - max_p_value / 2;
        exclusive_end = center + max_p_value / 2 + 1;
    }
    return StringView(input_text, inclusive_begin, exclusive_end);
}
