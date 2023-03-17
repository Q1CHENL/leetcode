public class MyAtoi {
    public int myAtoi(String s) {
        if (s.length() == 0) return 0;
        char first = s.charAt(0);
        //check start char
        if (first != ' ' && (!Character.isDigit(first)) && first != '-' && first != '+') return 0;
        long ret = 0; //type > int
        boolean signed = false; // negative or positive
        boolean allZero = true; // all we met till now are '0'
        for (int i = 0; i < s.length(); i++) {
            char curr = s.charAt(i); //current char
            char last = i > 0 ? s.charAt(i - 1) : s.charAt(0); //last char
            if (curr == '0' && i < s.length() - 1 && !Character.isDigit(s.charAt(i + 1)) && allZero) return 0;
            //non-digit
            if (!Character.isDigit(curr)) {
                // leading 0s
                if (curr == ' ' && (i == 0 || last == ' ')) continue;
                if (curr == '+' || curr == '-') {
                    // 2 consecutive signs
                    if (i != 0 && (last == '-' || last == '+')) return 0;
                    // '-' in the end
                    if (i != 0 && Character.isDigit(last)) return (int) (signed ? -ret : ret);
                    //set sign
                    signed = curr != '+';
                    continue;
                }
                //letter
                return (int) (signed ? -ret : ret);
            }
            // met non-zero digit
            allZero = false;
            ret = ret * 10 + (curr - '0');
            // return if current value exceeds
            if (ret > Integer.MAX_VALUE) return signed ? Integer.MIN_VALUE : Integer.MAX_VALUE;
        }
        return (int) (signed ? -ret : ret);
    }
    
    // better solution would be:
    // have a int i = 0, and move it forward till valid start met
    // start loop until non-digit
    // this is better than directly loop through s.length

    public static void main(String[] args) {
        MyAtoi m = new MyAtoi();
        String a = " -1010023630-";
        System.out.println(m.myAtoi(a));
    }
}

//    ANY time a letter is encountered, it triggers the end
//    of valid input (i.e. don't ignore leading letters).
//    The only valid starts of a string are a space, '+', '-', or a digit.
