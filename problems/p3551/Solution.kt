package p3551
/*
 * @lc app=leetcode id=3551 lang=kotlin
 *
 * [3551] Minimum Swaps to Sort by Digit Sum
 *
 * https://leetcode.com/problems/minimum-swaps-to-sort-by-digit-sum/description/
 *
 * algorithms
 * Medium (50.07%)
 * Likes:    191
 * Dislikes: 6
 * Total Accepted:    33.3K
 * Total Submissions: 62K
 * Testcase Example:  '[37,100]'
 *
 * You are given an array nums of distinct positive integers. You need to sort
 * the array in increasing order based on the sum of the digits of each number.
 * If two numbers have the same digit sum, the smaller number appears first in
 * the sorted order.
 * 
 * Return the minimum number of swaps required to rearrange nums into this
 * sorted order.
 * 
 * A swap is defined as exchanging the values at two distinct positions in the
 * array.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [37,100]
 * 
 * Output: 1
 * 
 * Explanation:
 * 
 * 
 * Compute the digit sum for each integer: [3 + 7 = 10, 1 + 0 + 0 = 1] → [10,
 * 1]
 * Sort the integers based on digit sum: [100, 37]. Swap 37 with 100 to obtain
 * the sorted order.
 * Thus, the minimum number of swaps required to rearrange nums is 1.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [22,14,33,7]
 * 
 * Output: 0
 * 
 * Explanation:
 * 
 * 
 * Compute the digit sum for each integer: [2 + 2 = 4, 1 + 4 = 5, 3 + 3 = 6, 7
 * = 7] → [4, 5, 6, 7]
 * Sort the integers based on digit sum: [22, 14, 33, 7]. The array is already
 * sorted.
 * Thus, the minimum number of swaps required to rearrange nums is 0.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [18,43,34,16]
 * 
 * Output: 2
 * 
 * Explanation:
 * 
 * 
 * Compute the digit sum for each integer: [1 + 8 = 9, 4 + 3 = 7, 3 + 4 = 7, 1
 * + 6 = 7] → [9, 7, 7, 7]
 * Sort the integers based on digit sum: [16, 34, 43, 18]. Swap 18 with 16, and
 * swap 43 with 34 to obtain the sorted order.
 * Thus, the minimum number of swaps required to rearrange nums is 2.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 10^5
 * 1 <= nums[i] <= 10^9
 * nums consists of distinct positive integers.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun digitSum(num: Int): Int {
        var n = num
        var sum = 0
        while (n > 0) {
            sum += n % 10
            n /= 10
        }
        return sum
    }
    fun minSwaps(nums: IntArray): Int { 
        val sorted = nums.sortedWith(
            compareBy<Int> { digitSum(it) }
                .thenBy { it }
        )
        val targetIndex = sorted.withIndex().associate { it.value to it.index }
        val visisted = BooleanArray(nums.size)
        var swaps = 0
        for (i in nums.indices) {
            if (visisted[i]) continue

            var j = i
            var size = 0

            while (!visisted[j]) {
                visisted[j] = true
                size += 1
                j = targetIndex.getValue(nums[j])
            }

            swaps += size - 1
        }
        return swaps
    }
}
// @lc code=end

