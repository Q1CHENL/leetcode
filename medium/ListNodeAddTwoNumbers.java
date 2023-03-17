
public class ListNodeAddTwoNumbers {
    int val;
    ListNodeAddTwoNumbers next;

    ListNodeAddTwoNumbers() {
    }

    ListNodeAddTwoNumbers(int val) {
        this.val = val;
    }

    ListNodeAddTwoNumbers(int val, ListNodeAddTwoNumbers next) {
        this.val = val;
        this.next = next;
    }

//    Input: l1 = [2,4,3], l2 = [5,6,4]
//    Output: [7,0,8]
//    Explanation: 342 + 465 = 807.

    public ListNodeAddTwoNumbers addTwoNumbers(ListNodeAddTwoNumbers l1, ListNodeAddTwoNumbers l2) {
        // check null
        if (l1 == null || l2 == null) {
            return null;
        }
        //ret
        ListNodeAddTwoNumbers sum = new ListNodeAddTwoNumbers();
        // cursors
        ListNodeAddTwoNumbers curSum = sum;
        ListNodeAddTwoNumbers cur1 = l1;
        ListNodeAddTwoNumbers cur2 = l2;

        // values
        int val1;
        int val2;
        int carry = 0;

        while (cur1 != null || cur2 != null) {
            val1 = cur1 == null ? 0 : cur1.val;
            val2 = cur2 == null ? 0 : cur2.val;

            int curVal = val1 + val2 + carry;
            curSum.val = curVal % 10;

            //compute new carry
            carry = curVal >= 10 ? 1 : 0;

            cur1 = cur1 == null ? null : cur1.next;
            cur2 = cur2 == null ? null : cur2.next;

            // create new node only when not both null or both null but carry
            if ((cur1 != null || cur2 != null) || carry == 1) {
                curSum.next = new ListNodeAddTwoNumbers();
                curSum = curSum.next;
            }
        }

        // when sum of last 2 digits creates carry
        if (carry == 1) {
            curSum.val = 1;
        }

        return sum;
    }
}
