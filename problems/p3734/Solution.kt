package p3734

/*
 * @lc app=leetcode id=3734 lang=kotlin
 *
 * [3734] Lexicographically Smallest Palindromic Permutation Greater Than Target
 */

// @lc code=start
class Solution {
    fun lexPalindromicPermutation(s: String, target: String): String {
        val n = s.length
        val count = IntArray(26)
        s.forEach { count[it - 'a']++ }

        if (count.count { it % 2 == 1 } > 1) return ""

        val middle = count.indices
            .firstOrNull { count[it] % 2 == 1 }
            ?.let { ('a' + it).toString() }
            ?: ""

        val pairs = IntArray(26) { count[it] / 2 }
        val halfLength = n / 2
        for (i in 0 until halfLength) {
            pairs[target[i] - 'a']--
        }

        var invalid = pairs.count { it < 0 }

        if (invalid == 0) {
            val leftHalf = target.substring(0, halfLength)
            val candidate = leftHalf + middle + leftHalf.reversed()
            if (candidate > target) return candidate
        }

        for (i in halfLength - 1 downTo 0) {
            val current = target[i] - 'a'
            pairs[current]++
            if (pairs[current] == 0) invalid--

            if (invalid > 0) continue

            var replacement = current + 1
            while (replacement < 26 && pairs[replacement] == 0) replacement++
            if (replacement == 26) continue

            pairs[replacement]--
            val leftHalf = StringBuilder(target.substring(0, i))
            leftHalf.append('a' + replacement)
            for (j in 0 until 26) {
                repeat(pairs[j]) {
                    leftHalf.append('a' + j)
                }
            }

            val left = leftHalf.toString()
            return left + middle + left.reversed()
        }
        return ""
    }
}
// @lc code=end
