package p1846
/*
 * @lc app=leetcode id=1846 lang=kotlin
 *
 * [1846] Maximum Element After Decreasing and Rearranging
 */
// @lc code=start
class Solution {
    fun maximumElementAfterDecrementingAndRearranging(arr: IntArray): Int {
        arr.sort()
        arr[0] = 1
        for (i in 1 until arr.size) {
            if (arr[i] - arr[i - 1] > 1) {
                arr[i] = arr[i - 1] + 1
            }
        }
        return arr.last()
    }
}
// @lc code=end

