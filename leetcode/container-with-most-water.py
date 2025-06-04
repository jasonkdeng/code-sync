class Solution {
    public int maxArea(int[] height) {
        int max = 0;
        int left = 0, right = height.length - 1;
        
        while (left < right) {
            int minHeight = Math.min(height[left], height[right]);
            max = Math.max(max, minHeight * (right - left));
            
            // Move the pointer with the smaller height
            if (height[left] < height[right]) {
                left++;
            } else {
                right--;
            }
        }
        
        return max;
    }
}