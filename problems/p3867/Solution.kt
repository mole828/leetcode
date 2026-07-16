package p3867

/*
 * @lc app=leetcode id=3867 lang=kotlin
 *
 * [3867] Sum of GCD of Formed Pairs
 */

// @lc code=start
class Solution {
    fun gcd(a: Int, b: Int): Int {
        if (b == 0) return a
        return gcd(b, a % b)
    }
    fun gcdSum(nums: IntArray): Long {
        var maxNum = 0
        val prefixGcd = mutableListOf<Int>()
        for (num in nums) {
            maxNum = maxOf(maxNum, num)
            prefixGcd.add(gcd(num, maxNum))
        }
        prefixGcd.sort()
        var answer = 0L
        while (prefixGcd.size > 1) {
            val a = prefixGcd.removeFirst()
            val b = prefixGcd.removeLast()
            answer += gcd(a, b)
        }
        return answer
    }
}
// @lc code=end

