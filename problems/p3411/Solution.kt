package p3411

/*
 * @lc app=leetcode id=3411 lang=kotlin
 *
 * [3411] Maximum Subarray With Equal Products
 *
 * https://leetcode.com/problems/maximum-subarray-with-equal-products/description/
 *
 * algorithms
 * Easy (47.05%)
 * Likes:    137
 * Dislikes: 55
 * Total Accepted:    37.6K
 * Total Submissions: 75.5K
 * Testcase Example:  '[1,2,1,2,1,1,1]'
 *
 * You are given an array of positive integers nums.
 * 
 * An array arr is called product equivalent if prod(arr) == lcm(arr) *
 * gcd(arr), where:
 * 
 * 
 * prod(arr) is the product of all elements of arr.
 * gcd(arr) is the GCD of all elements of arr.
 * lcm(arr) is the LCM of all elements of arr.
 * 
 * 
 * Return the length of the longest product equivalent subarray of nums.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [1,2,1,2,1,1,1]
 * 
 * Output: 5
 * 
 * Explanation: 
 * 
 * The longest product equivalent subarray is [1, 2, 1, 1, 1], where prod([1,
 * 2, 1, 1, 1]) = 2, gcd([1, 2, 1, 1, 1]) = 1, and lcm([1, 2, 1, 1, 1]) = 2.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [2,3,4,5,6]
 * 
 * Output: 3
 * 
 * Explanation: 
 * 
 * The longest product equivalent subarray is [3, 4, 5].
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,2,3,1,4,5,1]
 * 
 * Output: 5
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 2 <= nums.length <= 100
 * 1 <= nums[i] <= 10
 * 
 * 
 */

// @lc code=start
class Solution {
    fun maxLength(nums: IntArray): Int {
        var ans = 2
        var mul = 1
        var left = 0
        for (right in nums.indices) {
            while (gcd(mul, nums[right]) > 1) {
                mul /= nums[left]
                left += 1
            }
            mul *= nums[right]
            ans = maxOf(ans, right - left + 1)
        }
        return ans
    }

    fun gcd(a: Int, b: Int): Int {
        var a = a
        var b = b
        while (a != 0) {
            a = b.also { b = a } % a
        }
        return b
    }
}
// @lc code=end

