package problems.p2840
/*
 * @lc app=leetcode id=2840 lang=kotlin
 *
 * [2840] Check if Strings Can be Made Equal With Operations II
 */
// @lc code=start

class Solution {
    fun checkStrings(s1: String, s2: String): Boolean {
        val evenCount = IntArray(26)
        val oddCount = IntArray(26)

        for (i in s1.indices) {
            if (i % 2 == 0) {
                evenCount[s1[i] - 'a']++
                evenCount[s2[i] - 'a']--
            } else {
                oddCount[s1[i] - 'a']++
                oddCount[s2[i] - 'a']--
            }
        }

        return evenCount.all { it == 0 } && oddCount.all { it == 0 }
    }
}
// @lc code=end

