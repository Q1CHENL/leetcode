public class LongestPalindrome {
    public String longestPalindrome(String s) {
        int len = s.length();
        char curr;
        // tmp cursors
        int begin, end;
        // odd/even palidrome cursor
        int begin_odd = 0, end1_odd = 1, begin_even = 0, end_even = 1;
        // final start and end
        int begin_ret = 0, end_ret = 1;
        for (int i = 1; i < len; i++) {
            curr = s.charAt(i);
            // possible odd palidrome like aba
            if (i - 2 >= 0 && curr == s.charAt(i - 2)) {
                begin = i - 2;
                end = i + 1;
                while (begin >= 0 && end <= s.length() && s.charAt(begin) == s.charAt(end - 1)) {
                    // update odd max
                    if (end - begin > end_ret - begin_ret) {
                        begin_odd = begin;
                        end1_odd = end;
                    }
                    // expand
                    begin--;
                    end++;
                }
            }
            // possible even palindrome like aa
            if (i - 1 >= 0 && curr == s.charAt(i - 1)) {
                begin = i - 1;
                end = i + 1;
                while (begin >= 0 && end <= s.length() && s.charAt(begin) == s.charAt(end - 1)) {
                    // update even max
                    if (end - begin > end_ret - begin_ret) {
                        begin_even = begin;
                        end_even = end;
                    }
                    // expand
                    begin--;
                    end++;
                }
            }
            //take the max of odd and even as final
            begin_ret = end1_odd - begin_odd >= end_even - begin_even ? begin_odd : begin_even;
            end_ret = end1_odd - begin_odd >= end_even - begin_even ? end1_odd : end_even;
        }
        return s.substring(begin_ret, end_ret);
    }


    public static void main(String[] args) {
        String s = "ccc";
        LongestPalindrome l = new LongestPalindrome();
        System.out.println(l.longestPalindrome(s));
    }
}
