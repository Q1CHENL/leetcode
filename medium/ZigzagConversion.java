public class ZigzagConversion {
    public String convert(String s, int numRows) {
        if (numRows == 1) return s;
        //One builder for each row
        StringBuilder[] listOfSb = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            listOfSb[i] = new StringBuilder();
        }
        int k = (numRows - 1) * 2;
        for (int i = 0; i < s.length(); i++) {
            int rest = i % k;
            //i-th char in row [0, numRows-1] when rest < numRows
            int row = rest < numRows ? rest : k - rest;
            listOfSb[row].append(s.charAt(i));
        }
        StringBuilder sb = new StringBuilder();
        //combine all builders
        for (StringBuilder b : listOfSb) {
            sb.append(b);
        }
        return sb.toString();
    }
    
    // other thoughts:
    // 1. Use one StringBuilder, access row by row, not from s.start to end
    // 2. create one char[]/ArrayList, which holds 1.row+last.row+middle.rows*2, and then remove 0s

    public static void main(String[] args) {
        ZigzagConversion z = new ZigzagConversion();
        String s = "PAYPALISHIRING";
        String b = z.convert(s, 4);
        System.out.println(b);
    }


}
