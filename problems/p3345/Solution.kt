/*
 * @lc app=leetcode id=3345 lang=kotlin
 *
 * [3345] Smallest Divisible Digit Product I
 *
 * https://leetcode.com/problems/smallest-divisible-digit-product-i/description/
 *
 * algorithms
 * Easy (64.32%)
 * Likes:    89
 * Dislikes: 14
 * Total Accepted:    50.3K
 * Total Submissions: 75.4K
 * Testcase Example:  '10\n2'
 *
 * You are given two integers n and t. Return the smallest number greater than
 * or equal to n such that the product of its digits is divisible by t.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 10, t = 2
 * 
 * Output: 10
 * 
 * Explanation:
 * 
 * The digit product of 10 is 0, which is divisible by 2, making it the
 * smallest number greater than or equal to 10 that satisfies the condition.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 15, t = 3
 * 
 * Output: 16
 * 
 * Explanation:
 * 
 * The digit product of 16 is 6, which is divisible by 3, making it the
 * smallest number greater than or equal to 15 that satisfies the
 * condition.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 100
 * 1 <= t <= 10
 * 
 * 
 */
package p3345
// @lc code=start
class Solution {
    fun product(n: Int): Int {
        return n.toString().map { it - '0' }.reduce { a,b-> a*b }
    }
    fun smallestNumber(n: Int, t: Int): Int {
        var n = n
        while(product(n)%t!=0)n++
        return n
    }
}
// @lc code=end

