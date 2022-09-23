package java_ps.neetcode.arrayNhash;

import java.util.Arrays;

public class LeetCode128 {
    public int longestConsecutive(int[] nums) {
        if(nums.length == 0) return 0;
        Arrays.sort(nums);
        int max = 1;
        int curr = 1;

        for(int i = 1; i < nums.length; i++) {
            if(nums[i] == nums[i-1] + 1) {
                curr++;
                max = Math.max(curr, max);
            }
            else if(nums[i] == nums[i-1]) continue;
            else {
                curr = 1;
            }
        }
        return max;
    }
}
