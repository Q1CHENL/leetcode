public class TwoSum {
    public int[] twoSum(int[] nums, int target) {
        int len = nums.length;
        for (int firstIndex = 0; firstIndex < len - 1; firstIndex++) {
            for (int secondIndex = firstIndex + 1; secondIndex < len; secondIndex++) {
                if(target == nums[firstIndex] + nums[secondIndex]){
                    return new int[]{firstIndex, secondIndex};
                }
            }
        }
        return null;
    }
}