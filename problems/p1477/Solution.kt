package p1477

/*
 * @lc app=leetcode id=1477 lang=kotlin
 *
 * [1477] Find Two Non-overlapping Sub-arrays Each With Target Sum
 */

// @lc code=start
class Solution {
    fun minSumOfLengths(arr: IntArray, target: Int): Int {
        val inf = arr.size + 1
        val best = IntArray(arr.size + 1) { inf }
        var leftIndex = 0
        var windowSum = 0
        var answer = inf

        for (rightIndex in arr.indices) {
            windowSum += arr[rightIndex]
            while (windowSum > target) {
                windowSum -= arr[leftIndex]
                leftIndex++
            }

            best[rightIndex + 1] = best[rightIndex]
            if (windowSum == target) {
                val length = rightIndex - leftIndex + 1
                if (best[leftIndex] != inf) {
                    answer = minOf(answer, best[leftIndex] + length)
                }
                best[rightIndex + 1] = minOf(best[rightIndex + 1], length)
            }
        }

        return if (answer == inf) -1 else answer
    }
}
// @lc code=end
