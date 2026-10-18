package p1569
/*
 * @lc app=leetcode id=1569 lang=kotlin
 *
 * [1569] Number of Ways to Reorder Array to Get Same BST
 *
 * https://leetcode.com/problems/number-of-ways-to-reorder-array-to-get-same-bst/description/
 *
 * algorithms
 * Hard (54.22%)
 * Likes:    1886
 * Dislikes: 214
 * Total Accepted:    68.3K
 * Total Submissions: 123.4K
 * Testcase Example:  '[2,1,3]'
 *
 * Given an array nums that represents a permutation of integers from 1 to n.
 * We are going to construct a binary search tree (BST) by inserting the
 * elements of nums in order into an initially empty BST. Find the number of
 * different ways to reorder nums so that the constructed BST is identical to
 * that formed from the original array nums.
 * 
 * 
 * For example, given nums = [2,1,3], we will have 2 as the root, 1 as a left
 * child, and 3 as a right child. The array [2,3,1] also yields the same BST
 * but [3,2,1] yields a different BST.
 * 
 * 
 * Return the number of ways to reorder nums such that the BST formed is
 * identical to the original BST formed from nums.
 * 
 * Since the answer may be very large, return it modulo 10^9 + 7.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: nums = [2,1,3]
 * Output: 1
 * Explanation: We can reorder nums to be [2,3,1] which will yield the same
 * BST. There are no other ways to reorder nums which will yield the same
 * BST.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: nums = [3,4,5,1,2]
 * Output: 5
 * Explanation: The following 5 arrays will yield the same BST: 
 * [3,1,2,4,5]
 * [3,1,4,2,5]
 * [3,1,4,5,2]
 * [3,4,1,2,5]
 * [3,4,1,5,2]
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: nums = [1,2,3]
 * Output: 0
 * Explanation: There are no other orderings of nums that will yield the same
 * BST.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= nums.length <= 1000
 * 1 <= nums[i] <= nums.length
 * All integers in nums are distinct.
 * 
 * 
 */

// @lc code=start
class Solution {
    val mod = 1_000_000_007
    fun pow(base: Long, exponent: Int, mod: Int): Long {
        var a = base % mod
        var e = exponent
        var result = 1L
        while (e > 0) {
            if ((e and 1) != 0) result = result*a%mod
            a = a * a % mod
            e = e shr 1
        }
        return result

    }
    fun numOfWays(nums: IntArray): Int {
        val n = nums.size
        val prev = (-1..n).toList().toIntArray()
        val next = (1..n+2).toList().toIntArray()
        val size = IntArray(n+2)
        var prod = 1L
        nums.reversed().forEach { x ->
            size[x] = 1
            
            val left = prev[x]
            if (size[left] > 0) {
                size[x] += size[left]
                val pl = prev[left]
                prev[x] = pl
                next[pl] = x
            }

            val right = next[x]
            if (size[right] > 0) {
                size[x] += size[right]
                val nr = next[right]
                prev[nr] = x
                next[x] = nr
            }

            prod = prod * size[x] % mod
        }

        var fac = 1L
        (2..n).forEach { fac = fac * it % mod }

        return ((fac * pow(prod, mod - 2, mod) - 1 + mod) % mod).toInt()
    }
}
// @lc code=end

