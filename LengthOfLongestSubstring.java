import java.util.Arrays;
import java.util.HashSet;
import java.util.Set;

public class LengthOfLongestSubstring {

    //Fixed size sliding window: size starts from 0 to length
    public int lengthOfLongestSubstring(String s) {
        if (s == null || s.equals("")) {
            return 0;
        }
        int ret = 1;
        int len = s.length();
        boolean found = false;
        String substring;
        for (int i = 2; i <= len; i++) {
            int k = i;
            for (int j = 0; j <= len - i; j++) {
                substring = s.substring(j, k);
                k++;
                if (!containsRepeatingChar(substring)) {
                    ret++;
                    found = true;
                    break;
                }
                found = false;
            }
            if (!found) {
                return ret;
            }
        }
        return ret;
    }

    public boolean containsRepeatingChar(String str) {
        Set<Character> set = new HashSet<>();
        for (int i = 0; i < str.length(); i++) {
            char curr = str.charAt(i);
            if(set.contains(curr)){
                return true;
            }
            set.add(curr);
        }
        return false;
    }

// My original solution, somehow this is faster
//    public boolean containsRepeatingChar(String str) {
//        char[] arr = str.toCharArray();
//        Arrays.sort(arr);
//        for (int i = 0; i < arr.length - 1; i++) {
//            if (arr[i] == arr[i + 1]) {
//                return true;
//            }
//        }
//        return false;
//    }


// Solution from discussion: variable sliding window
//    public int lengthOfLongestSubstring(String s) {
//        Set<Character>set=new HashSet<>();
//        int maxLength=0;
//        int left=0;
//        for(int right=0;right<s.length();right++){
//
//            if(!set.contains(s.charAt(right))){
//                set.add(s.charAt(right));
//                maxLength=Math.max(maxLength,right-left+1);
//
//            }else{
//                while(s.charAt(left)!=s.charAt(right)){
//                    set.remove(s.charAt(left));
//                    left++;
//                }
//                set.remove(s.charAt(left));left++;
//                set.add(s.charAt(right));
//            }
//        }
//        return maxLength;
//    }


}
