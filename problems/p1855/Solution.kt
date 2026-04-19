package problems.p1855
/*
 * @lc app=leetcode id=1855 lang=kotlin
 *
 * [1855] Maximum Distance Between a Pair of Values
 */
// @lc code=start
class Solution {
    fun maxDistance(nums1: IntArray, nums2: IntArray): Int {
        var maxDistance = 0
        nums1.forEachIndexed { i, a ->
            for (j in i until nums2.size) {
                val b = nums2[j]
                // println("""
                //     i = $i
                //     j = $j
                //     a = $a
                //     b = $b
                //     pass = ${ (i<=j) and (a<=b) }
                // """)
                if (a <= b) {
                    maxDistance = maxOf(maxDistance, j - i)
                } else {
                    break
                }
            }
        }
        return maxDistance
    }
}
// @lc code=end

