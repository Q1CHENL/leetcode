#include <iostream>
// Given two integers dividend and divisor, divide two integers without using
// multiplication, division, and mod operator.

// The integer division should truncate toward zero, which means losing its
// fractional part. For example, 8.345 would be truncated to 8, and -2.7335
// would be truncated to -2.

// Return the quotient after dividing dividend by divisor.

// Note: Assume we are dealing with an environment that could only store
// integers within the 32-bit signed integer range: [−2^31, 2^31 − 1]. For this
// problem, if the quotient is strictly greater than 2^31 - 1, then return
// 2^31 - 1, and if the quotient is strictly less than -2^31, then return -2^31.

class IntegerDivider {
   public:
    // My solution, normal division, passed but slow
    // int divide(int dividend, int divisor) {
    //     if (divisor == 1) {
    //         return dividend;
    //     }
    //     if (divisor == -1) {
    //         return dividend == INT32_MIN ? INT32_MAX : -dividend;
    //     }

    //     if (divisor == INT32_MIN) {
    //         if (dividend == INT32_MIN) {
    //             return 1;
    //         }
    //         return 0;
    //     }

    //     int quotient = 0;
    //     if (dividend == INT32_MIN) {
    //         dividend += abs(divisor);
    //         quotient++;
    //     }
    //     bool sign = (dividend < 0 && divisor >= 0) || (divisor < 0 && dividend >= 0);

    //     if (dividend < 0) {
    //         dividend = -dividend;
    //     }
    //     if (divisor < 0) {
    //         divisor = -divisor;
    //     }
    //     if (divisor > dividend) {
    //         return sign ? -quotient : quotient;
    //     }
    //     while (divisor <= dividend) {
    //         dividend -= divisor;
    //         quotient++;
    //     }
    //     return sign ? -quotient : quotient;
    // }

    // Sample solution from leetcode: using 2^n(bit shifting) instead of add to approach the quotient faster
    int divide(int dividend, int divisor) {
        if (dividend == divisor)
            return 1;
        bool isPositive = (dividend < 0 == divisor < 0);  // if both are of same sign, answer is positive
        unsigned int a = abs(dividend);
        unsigned int b = abs(divisor);
        unsigned int ans = 0;
        while (a >= b) {  // while dividend is greater than or equal to divisor
            short q = 0;
            while (a > (b << (q + 1)))
                q++;
            ans += (1 << q);   // add the power of 2 found to the answer
            a = a - (b << q);  // reduce the dividend by divisor * power of 2 found
        }
        if (ans == (1 << 31) and isPositive)  // if ans cannot be stored in signed int
            return INT32_MAX;
        return isPositive ? ans : -ans;
    }
};

int main(int argc, char const *argv[]) {
    IntegerDivider divider;
    int quotient = divider.divide(INT32_MAX, 2);
    std::cout << quotient << std::endl;
}
