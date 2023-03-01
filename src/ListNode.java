
public class ListNode {
    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }

//    Input: l1 = [2,4,3], l2 = [5,6,4]
//    Output: [7,0,8]
//    Explanation: 342 + 465 = 807.

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // check null
        if (l1 == null || l2 == null) {
            return null;
        }
        //ret
        ListNode sum = new ListNode();
        // cursors
        ListNode curSum = sum;
        ListNode cur1 = l1;
        ListNode cur2 = l2;

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
                curSum.next = new ListNode();
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
