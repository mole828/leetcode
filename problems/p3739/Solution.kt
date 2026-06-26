package p3739

/*
 * @lc app=leetcode id=3739 lang=kotlin
 *
 * [3739] Count Subarrays With Majority Element II
 */

// @lc code=start
class Solution {
    fun countMajoritySubarrays(nums: IntArray, target: Int): Long {
        val offset = nums.size + 1
        val bit = Fenwick(offset * 2 + 1)
        var prefix = 0
        var result = 0L

        bit.add(offset, 1)
        for (num in nums) {
            prefix += if (num == target) 1 else -1
            val index = prefix + offset
            result += bit.query(index - 1)
            bit.add(index, 1)
        }
        return result
    }

    private class Fenwick(size: Int) {
        private val tree = IntArray(size + 1)

        fun add(index: Int, delta: Int) {
            var i = index + 1
            while (i < tree.size) {
                tree[i] += delta
                i += i and -i
            }
        }

        fun query(index: Int): Int {
            var i = index + 1
            var sum = 0
            while (i > 0) {
                sum += tree[i]
                i -= i and -i
            }
            return sum
        }
    }
}
// @lc code=end
