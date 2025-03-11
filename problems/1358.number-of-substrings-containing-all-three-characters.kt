/*
 * @lc app=leetcode id=1358 lang=kotlin
 *
 * [1358] Number of Substrings Containing All Three Characters
 */

package p1358

// @lc code=start
class Solution {
    // Time Limit Exceeded
    // 23/54 cases passed (N/A)
    fun _numberOfSubstrings(s: String): Int {
        var ans = 0
        for(left in 0.until(s.length)) {
            for(right in left..s.length) {
                val sub = s.substring(left, right)
                val set = sub.toSet()
                // println("$left $right $sub $set")
                if (set.size==3) {
                    ans += 1
                }
            }
        }
        return ans
    }

    // Time Limit Exceeded
    // 48/54 cases passed (N/A)
    fun __numberOfSubstrings(s: String): Int {
        var ans = 0
        for(left in 0.until(s.length)) {
            var ca = 0
            var cb = 0
            var cc = 0
            for(right in left.until(s.length)) {
                val char = s[right]
                when (char) {
                    'a' -> ca += 1
                    'b' -> cb += 1
                    'c' -> cc += 1
                }
                if ((ca>0) and (cb>0) and (cc>0)) {
                    ans += 1
                }
            }
        }
        return ans
    }

    fun numberOfSubstrings(s: String): Int { 
        var ans = 0
        val count = emptyMap<Char, Int>().toMutableMap()
        var left = 0
        var right = 0
        while (right<s.length) {
            val newChar = s[right]
            right += 1
            count.set(newChar, count.getOrDefault(newChar, 0)+1)
            while((count.keys.size==3)and(left<right)) {
                ans += s.length - right + 1
                // println("$left $right $count")
                val popChar = s[left]
                left += 1
                val last = count.getValue(popChar) - 1
                if (last == 0) {
                    count.remove(popChar)
                } else {
                    count.set(popChar, last)
                }
            }
        }
        return ans
    }
}
// @lc code=end

fun main() {
    println(Solution().numberOfSubstrings("abcabc"))
}