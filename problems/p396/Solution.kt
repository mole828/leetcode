package problems.p396
/*
 * @lc app=leetcode id=396 lang=kotlin
 *
 * [396] Rotate Function
 */
// @lc code=start
fun IntArray.rotateGet(d: Int, i: Int): Int {
    return this[(i+d)%this.size]
}
class Solution {
    @Deprecated("time limit exceeded")
    fun maxRotateFunction0(nums: IntArray): Int {
        var maxSum = Int.MIN_VALUE
        fun f(d: Int): Int = nums.indices.sumOf { it * nums.rotateGet(d, it) }
        for (i in nums.indices) {
            maxSum = maxOf(maxSum, f(i))
        }
        return maxSum
    }
    fun maxRotateFunction(nums: IntArray): Int {
        val numsSum = nums.sum()
        var sum = nums.mapIndexed { i, v -> i*v }.sum()
        var maxSum = sum
        for (i in nums.size-1 downTo 0) {
            sum += numsSum - nums.size * nums[i]
            maxSum = maxOf(maxSum, sum)
        }
        return maxSum
    }
}
// @lc code=end

