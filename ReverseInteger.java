public class ReverseInteger {

    // inspired by ChatGPT
    public int reverse(int x) {
        boolean signed = false;
        String str = new StringBuilder(String.valueOf(x)).reverse().toString();
        if (str.charAt(str.length() - 1) == '-') {
            str = str.substring(0, str.length() - 1);
            signed = true;
        }
        int reversed = 0;
        for (int i = 0; i < str.length(); i++) {
            int digit = str.charAt(i) - '0';
            // check second condition if last char met
            if (reversed > Integer.MAX_VALUE / 10 || (reversed == Integer.MAX_VALUE / 10 && digit > 7)) {
                return 0;
            }
            reversed = reversed * 10 + digit;
        }
        if (signed) reversed = -reversed;
        return reversed;
    }

//    My original thought
//    public int reverse(int x) {
//        int reversed = 0;
//        boolean signed = false;
//        String s = String.valueOf(x);
//
//        if (s.charAt(0) == '-') {
//            s = s.substring(1);
//            signed = true;
//        }
//        if (s.length() > 10) {
//            return 0;
//        }
//        boolean exceeded = false;
//        if (s.length() == 10) {
//            int offset = signed ? 1 : 0;
//            String max = String.valueOf(signed ? Integer.MIN_VALUE : Integer.MAX_VALUE);
//            for (int i = s.length() - 1; i >= 0; i--) {
//                char curr = max.charAt(s.length() - 1 - i + offset);
//                if (s.charAt(i) == curr) {
//                    continue;
//                }
//                exceeded = s.charAt(i) > curr;
//                break;
//            }
//        }
//        if (exceeded) return 0;
//        for (int i = 0; i < s.length(); i++) {
//            reversed += ((int) s.charAt(i) - 48) * Math.pow(10, i);
//        }
//        if (signed) reversed = -reversed;
//        return reversed;
//    }

    public static void main(String[] args) {
        int a = -12300;
        //2147483648
        ReverseInteger r = new ReverseInteger();
        System.out.println(r.reverse(a));
    }
}
