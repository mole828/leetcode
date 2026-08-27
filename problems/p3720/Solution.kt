package p3720

/*
 * @lc app=leetcode id=3720 lang=kotlin
 *
 * [3720] Lexicographically Smallest Permutation Greater Than Target
 */

// @lc code=start
class Solution {
    fun lexGreaterPermutation(s: String, target: String): String {
        val n = s.length
        val left = IntArray(26)
        (0 until n).forEach { 
            left[s[it] - 'a']++
            left[target[it] - 'a']--
        }
        next@for (i in n-1 downTo 0) {
            val rightIndex = target[i] - 'a'
            left[rightIndex]++
            left.all { it >= 0 } || continue
            for (j in rightIndex + 1 until 26) {
                if (left[j] == 0) continue
                left[j]--
                val ans = StringBuilder(target.substring(0, i+1))
                ans.setCharAt(i, 'a' + j)
                for (k in 0 until 26) {
                    repeat(left[k]) {
                        ans.append('a' + k)
                    }
                }
                return ans.toString()
            }
        }
        return ""
    }
}
// @lc code=end

