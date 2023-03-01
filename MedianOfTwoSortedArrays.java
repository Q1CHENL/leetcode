public class MedianOfTwoSortedArrays {
    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] merged = new int[nums1.length + nums2.length];
        if (nums1.length == 0) {
            return medianOfIntArray(nums2);
        } else if (nums2.length == 0) {
            return medianOfIntArray(nums1);
        }
        int smaller = Math.min(nums1[0], nums2[0]);
        int curr1 = nums1[0];
        int curr2 = nums2[0];
        int i1 = 1, i2 = 1;
        for (int i = 0; i < merged.length; i++) {
            merged[i] = smaller;
            //update curr1/2
            if (smaller == curr1) {
                curr1 = i1 < nums1.length ? nums1[i1++] : nums2[nums2.length - 1] + 1;
            } else {
                curr2 = i2 < nums2.length ? nums2[i2++] : nums1[nums1.length - 1] + 1;
            }
            //update smaller
            smaller = Math.min(curr1, curr2);
        }
        return medianOfIntArray(merged);
    }

    public double medianOfIntArray(int[] arr) {
        return arr.length % 2 == 0 ? (double) (arr[arr.length / 2 - 1] + arr[arr.length / 2]) / 2 : arr[arr.length / 2];
    }

    public static void main(String[] args) {
        MedianOfTwoSortedArrays m = new MedianOfTwoSortedArrays();
        double a = m.findMedianSortedArrays(new int[]{1}, new int[]{2, 3, 4, 5, 6});
        // 1, 2, 3, 3,
        System.out.println("Median: " + a);
    }
}
