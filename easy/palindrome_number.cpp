#include <string>
#include <iostream>

class palindrome_number {
public:
    bool isPalindrome(int x) {
        if (x < 0) return false;
        std::string s = std::to_string(x);
        int j = s.length() - 1;
        for (int i = 0; i < s.length(); ++i) {
            if (s.at(i) == s.at(j)) {
                j--;
                continue;
            }
            return false;
        }
        return true;
    }
    // Another method would be:
    // add reversely and check if the sum equals x
};

int main() {
    palindrome_number p;
    int a = -123454321;
    bool b = p.isPalindrome(a);
    std::cout << std::boolalpha << a << " is palindrome: " << b << std::endl;
}