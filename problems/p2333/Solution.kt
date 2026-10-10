package p2333

import java.util.PriorityQueue
import kotlin.math.absoluteValue

/*
 * @lc app=leetcode id=2333 lang=kotlin
 *
 * [2333] Minimum Sum of Squared Difference
 *
 * https://leetcode.com/problems/minimum-sum-of-squared-difference/description/
 *
 * algorithms
 * Medium (26.93%)
 * Likes:    691
 * Dislikes: 54
 * Total Accepted:    22.5K
 * Total Submissions: 78.5K
 * Testcase Example:  '[1,2,3,4]\n[2,10,20,19]\n0\n0'
 *
 * You are given two positive 0-indexed integer arrays nums1 and nums2, both of
 * length n.
 * 
 * The sum of squared difference of arrays nums1 and nums2 is defined as the
 * sum of (nums1[i] - nums2[i])^2 for each 0 <= i < n.
 * 
 * You are also given two positive integers k1 and k2. You can modify any of
 * the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can
 * modify any of the elements of nums2 by +1 or -1 at most k2 times.
 * 
 * Return the minimum sum of squared difference after modifying array nums1 at
 * most k1 times and modifying array nums2 at most k2 times.
 * 
 * Note: You are allowed to modify the array elements to become negative
 * integers.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums1 = [1,2,3,4], nums2 = [2,10,20,19], k1 = 0, k2 = 0
 * Output: 579
 * Explanation: The elements in nums1 and nums2 cannot be modified because k1 =
 * 0 and k2 = 0. 
 * The sum of square difference will be: (1 - 2)^2 + (2 - 10)^2 + (3 - 20)^2 +
 * (4 - 19)^2 = 579.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
 * Output: 43
 * Explanation: One way to obtain the minimum sum of square difference is: 
 * - Increase nums1[0] once.
 * - Increase nums2[2] once.
 * The minimum of the sum of square difference will be: 
 * (2 - 5)^2 + (4 - 8)^2 + (10 - 7)^2 + (12 - 9)^2 = 43.
 * Note that, there are other ways to obtain the minimum of the sum of square
 * difference, but there is no way to obtain a sum smaller than 43.
 * 
 * 
 * Constraints:
 * 
 * 
 * n == nums1.length == nums2.length
 * 1 <= n <= 10^5
 * 0 <= nums1[i], nums2[i] <= 10^5
 * 0 <= k1, k2 <= 10^9
 * 
 * 
 */

// @lc code=start
class Solution {
    fun minSumSquareDiff(nums1: IntArray, nums2: IntArray, k1: Int, k2: Int): Long {
        val count = IntArray(100001)
        nums1.indices.forEach { 
            val d = (nums1[it]-nums2[it]).absoluteValue
            count[d] += 1
        }
        
        var k = k1 + k2
        for (i in 99999 downTo 0) {
            val c = count[i+1]
            if (c > k) {
                count[i+1] -= k
                count[i] += k
                k -= k
            } else {
                count[i+1] -= c
                count[i] += c
                k -= c
            }
            if (k==0) break
        }
        
        return count.mapIndexed { index, i -> index.toLong()*index*i }.sum()
    }
}
// @lc code=end

