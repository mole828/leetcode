package p2948
/*
 * @lc app=leetcode id=2948 lang=kotlin
 *
 * [2948] Make Lexicographically Smallest Array by Swapping Elements
 */
// @lc code=start
class Solution {
    fun lexicographicallySmallestArray(nums: IntArray, limit: Int): IntArray {
        val result = IntArray(nums.size)
        val sorted = nums.mapIndexed { index, value -> index to value }.sortedBy { it.second }.toMutableList()
        sorted.add(Int.MAX_VALUE to Int.MAX_VALUE)

        var seg = mutableListOf(sorted[0])
        for (idx in 1..<sorted.size) {
            if (sorted[idx].second - seg.last().second <= limit) 
                seg.add(sorted[idx])
            else 
                seg.sortedBy { it.first }
                    .forEachIndexed { i, pair -> 
                        result[pair.first] = seg[i].second
                    }.also { seg = mutableListOf(sorted[idx]) }
        }
        return result
    }
}
// @lc code=end

