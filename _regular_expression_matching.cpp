#include <string>
#include <iostream>
#include <vector>
#include <map>

class regular_expression_matching {
public:

    bool isMatch(std::string s, std::string p) {
        if (p.empty()) return s.empty();
        bool first_match = (!s.empty() && (p.at(0) == s.at(0) || p.at(0) == '.'));

        if (p.length() >= 2 && p.at(1) == '*') {
            return (isMatch(s, p.substr(2))) || (first_match && isMatch(s.substr(1), p));
        } else {
            return first_match && isMatch(s.substr(1), p.substr(1));
        }
    }
    // idea: collect all pattern into a vector
    // then try to match s iteratively
//    bool isMatch(std::string s, std::string p) {
//        int origin_len = s.length();
//        int pure_len = p.length();
//        std::vector<std::string> patterns;
//        std::string last_part;
//        //find all patterns
//        std::string cp;
//        std::string pure_str;
//        int matched = 0;
//        int last_starIndex = -1;
//        for (int i = 0; i < p.length(); ++i) {
//            if (p.at(i) != '*') {
//                cp.push_back(p.at(i));
//                if ((i < p.length() - 1 && p.at(i + 1) != '*') || (i == p.length() - 1)) {
//                    pure_str.push_back(p.at(i));
//                }
//                continue;
//            }
//            pure_len -= 2;
//            last_starIndex = i;
//
//            /////////////////////////////////////
//            if(cp.length() != 1 || cp.at(0) != '.') {
//                patterns.emplace_back(cp);
//            }
//            cp.clear();
//        }
//
//        if (patterns.empty()) {
//            //all patterns are '.'
//            if(p.find('*') !=std::string::npos) return true;
//            if (s.length() != p.length()) {
//                return false;
//            }
//            if (s.length() == p.length()) {
//                if (s == p) { return true; }
//                for (int i = 0; i < s.length(); ++i) {
//                    if (s.at(i) != p.at(i) && p.at(i) != '.') return false;
//                }
//                return true;
//            }
//        }
//
//        if (pure_len > origin_len) {
//            return false;
//        }
//        if (pure_len == origin_len) {
//            if (pure_str == s) return true;
//            for (int i = 0; i < pure_len; ++i) {
//                if (pure_str.at(i) != s.at(i) && pure_str.at(i) != '.') return false;
//            }
//            return true;
//        }
//        //patterns.emplace_back(cp);
//
//        last_part = p.substr(last_starIndex + 1);
//        int r = s.length() - 1;
//        for (int i = last_part.length() - 1; i >= 0; --i) {
//            if (s.at(r) != last_part.at(i) && last_part.at(i) != '.') {
//                return false;
//            }
//            r--;
//        }
//        bool full_match = true;
//        int j = 0;
//        //should return if already match before end
//        if (s.length() == 0 && matched == last_part.length()) return true;
//        for (int pt = 0; pt < patterns.size(); ++pt) {
//            for (int i = 0; i < patterns.at(pt).length() - 1; ++i) {
//                if ((j <= s.length() - 1) && (patterns.at(pt).at(i) == s.at(j) || patterns.at(pt).at(i) == '.')) {
//                    //matched++;
//                    j++;
//                    continue;
//                }
//                full_match = false;
//                if (pt == patterns.size() - 1) return false;
//            }
//            if (full_match) {
//                matched += (patterns.at(pt).length() - 1);
//            }
//            while ((j <= s.length() - 1) &&
//                   (patterns.at(pt).at(patterns.at(pt).length() - 1) == s.at(j) ||
//                    patterns.at(pt).at(patterns.at(pt).length() - 1) == '.')) {
//                matched++;
//                j++;
//            }
//            if (matched >= origin_len) return true;
//        }
//
//        if (s.substr(j).length() == last_part.length()) {
//            if (s.substr(j) == last_part) { return true; }
//            for (int i = 0; i < last_part.length(); ++i) {
//                if (s.at(i) != p.at(i) && p.at(i) != '.') return false;
//            }
//            return true;
//        }
//
//        if (matched < origin_len) return false;
//        return false;
//    }

};

int main() {
    regular_expression_matching r;
    //bool v = r.isMatch("aaabaaaababcbccbaab", "c*c*.*c*a*..*c*");
    //bbbbbbbb
    //aa*.*
    bool v = r.isMatch("aababbabacaabacbbbc", ".b*ac*.*c*a*b*.*");
    std::cout << v << std::endl;
    std::map<std::pair<std::string, std::string>, bool> invalidCases = {
            {{"aab",                 "c*a*b"},                      true},
            {{"mississippi",         "mis*is*p*."},                 false},
            {{"aaa",                 "ab*ac*a"},                    true},
            {{"aaa",                 "ab*a*c*a"},                   true},
            {{"aaca",                "ab*a*c*a"},                   true},
            {{"a",                   "ab*"},                        true},
            {{"bbbba",               ".*a*a"},                      true},
            {{"ab",                  ".*.."},                       true},
            {{"ab",                  ".*..c*"},                     true},
            {{"a",                   ".*."},                        true},
            {{"aasdfasdfasdfasdfas", "aasdf.*asdf.*asdf.*asdf.*s"}, true},
            {{"abbbcd",              "ab*bbbcd"},                   true},
            {{"bbab",                "b*a*"},                       false},
            {{"a",                   "c*."},                        true},
            {{"a",                   "c*a"},                        true},
            {{"b",                   "a*."},                        true},
            {{"a",                   ".*a*"},                       true},
            {{"a",                   "..*"},                        true},
            {{"aabcbcbcaccbcaabc",   ".*a*aa*.*b*.c*.*a*"},         true},
            {{"abbabaaaaaaacaa",     "a*.*b.a.*c*b*a*c*"},          true},
            {{"bcaccbbacbcbcab",     "b*.c*..*.b*b*.*c*"},          true},
            {{"baabbbaccbccacacc",   "c*..b*a*a.*a..*c"},           true},
            {{"abcaaaaaaabaabcabac", ".*ab.a.*a*a*.*b*b*"},         true},
            {{"cbaacacaaccbaabcb",   "c*b*b*.*ac*.*bc*a*"},         true},
            {{"cbaacacaaccbaabcb",   "c*b*b*.*ac*.*bc*a*"},         true},
            {{"cabbbbcbcacbabc",     ".*b.*.ab*.*b*a*c"},           true},
            {{"abbcacbbbbbabcbaca",  "a*a*.*a*.*a*.b*a*"},          true},
            {{"aababbabacaabacbbbc", ".b*ac*.*c*a*b*.*"},           true},
            {{"aaabaaaababcbccbaab", "c*c*.*c*a*..*c*"},            true},
            {{"cbccaababcbabac",     "c*aab*.*b.b.*.*a*."},         false},
            {{"caccccaccbabbcb",     "c*c*b*a*.*c*.a*a*a*"},        true},
            {{"bbbaccbbbaababbac",   ".b*b*.*...*.*c*."},           true},
            {{"ccbbcabcbbaabaccc",   "c*a*.*a*a*.*c*b*b*."},        true},
            {{"abbaaaabaabbcba",     "a*.*ba.*c*..a*.a*."},         true},
            {{"bbcacbabbcbaaccabc",  "b*a*a*.c*bb*b*.*.*"},         true},
            {{"aabccbcbacabaab",     ".*c*a*b.*a*ba*bb*"},          true},
            {{"cbbbaccbcacbcca",     "b*.*b*a*.a*b*.a*"},           true},
            {{"cbacbbabbcaabbb",     "b*c*.*a*..a.*c*.*"},          true},
            {{"abaabababbcbcabbcbc", "b*ab.*.*.*.b..*"},            true},
            {{"caaacccbaababbb",     "c*.*b*ba*ac*c*b*.*"},         true},
            {{"abbbaabccbaabacab",   "ab*b*b*bc*ac*.*bb*"},         true},
            {{"abbbaabccbaabacab",   "ab*b*b*bc*ac*.*bb*"},         true},
            {{"cacbacccbbbccab",     ".b*b*.*c*a*.*bb*"},           true},
            {{"abcbccbcbaabbcbb",    "c*a.*ab*.*ab*a*..b*"},        true},
            {{"caabbabbbbccccbbbcc", ".b*c*.*.*bb*.*.*"},           true},
            {{"caaccabbbabcacaac",   "b*c*b*b*.b*.*c*a*c"},         true},
            {{"cbcaabcbaabccbaa",    "c*b*ab*.*b*c*a*"},            false},
            {{"bccbcccbcbbbcbb",     "c*c*c*c*c*.*.*b*b*"},         true},
            {{"ccacbcbcccabbab",     ".c*a*aa*b*.*b*.*"},           true},
            {{"aabbcbcacbacaaccacc", "c*b*b*.*.*.*a*.*"},           true},
            {{"bcbabcaacacbcabac",   "a*c*a*b*.*aa*c*a*a*"},        true},
            {{"acabbabacaccacccabc", "a*.*c*a*.b.*a*.*"},           true},
            {{"babbcccbacaabcbac",   "b.*.*c*b*b*.*c*c"},           true},
            {{"cbbbbabaabbacbbc",    "a*c*b*.*bb*a*.*a*"},          true},
            {{"accbabbacbbbacb",     ".*.*.*a*bba*ba*"},            false},
            {{"ababbcaaabbaccb",     "c*c*..*a*a*a*.*"},            true},
            {{"bcabcbcaccabcbb",     "a*a*c*a*.*a*c*bc*."},         true},
            {{"bcbbbacbabccbabbac",  "c*.*b*a.*a*a*a*"},            true},
            {{"ccbbbbbacacaaabcaa",  ".*ba*.*.b*c*c*b*a.*"},        true},
            {{"acaababbccbaacabcab", "..*bb*b*c*a*c*.*.b"},         true},
            {{"cbabcabbbacbcaca",    "a*c*.*a*a*b*c*a*.*"},         true},
            {{"bacacaababbbcbc",     ".*a*.*a*.aa*c*b*c"},          false},
            {{"cbabcbbaabbcaca",     ".a*b*.*.*b*c*.*b*a*"},        true},
            {{"bbaaaacabccbcac",     "b*b*a*c*c*a*c*.*"},           true},
            {{"bcccccbaccccacaa",    ".*bb*c*a*b*.*b*b*c*"},        true},
            {{"bcbaccbbbccabaac",    "c*.*a*b*ac*a*a*"},            true},
            {{"bacacbacaaabccbcbaa", "a*.c*c*c*a*b*..*"},           true},
            {{"baccbbcbcacacbbc",    "c*.*b*c*ba*b*b*.a*"},         true},

    };

    int f = 0;
    int t = 0;
    for (const auto &s: invalidCases) {
        bool b = r.isMatch(s.first.first, s.first.second);
        if (s.second == b) {
            t++;
        } else f++;
        std::cout << s.first.first << ", " << s.first.second << ": " << b << " expected: " << s.second << std::endl;
    }
    std::cout << "Passed: " << t << "/" << t + f << std::endl;

}
//1 <= s.length <= 20
//1 <= p.length <= 20
//s contains only lowercase English letters.
//p contains only lowercase English letters, '.', and '*'.
//It is guaranteed for each appearance of the character '*', there will be a previous valid character to match.
