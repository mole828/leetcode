/*
 * @lc app=leetcode id=3306 lang=kotlin
 *
 * [3306] Count of Substrings Containing Every Vowel and K Consonants II
 */

package p3306

// @lc code=start
class Solution {
    val vowels = setOf('a', 'e', 'i', 'o', 'u')
    
    /*
    "iqeaouqi", 2
    包括了 "iqeaouq" "qeaouqi" "iqeaouqi"
    */
    fun _countOfSubstrings(word: String, k: Int): Long {
        val len = vowels.size + k
        var ans = 0L
        for (left in 0..(word.length - len)) {
            val sub = word.substring(left, left + len)
            println("left: $left, sub: $sub")
            if ((vowels - sub.toSet()).isEmpty()) {
                ans += 1
            }
        }
        return ans
    }

    fun f(word: String, k: Int): Long {
        var ans = 0L
        var left = 0
        val counter = emptyMap<Char, Int>().toMutableMap()
        var nonVowelsCount = 0
        for ( char in word ) {
            if (char in vowels) counter[char] = counter.getOrDefault(char, 0) + 1
            else nonVowelsCount += 1
            while ((counter.keys.size == vowels.size)and(nonVowelsCount >= k)) {
                val out = word[left]
                if (out in vowels) {
                    val newVal = counter.getValue(out) - 1
                    if (newVal == 0) {
                        counter.remove(out)
                    } else {
                        counter[out] = newVal
                    }
                } else {
                    nonVowelsCount -= 1
                }
                left += 1
            }
            ans += left
        }
        return ans
    }
    fun countOfSubstrings(word: String, k: Int): Long {
        return f(word, k) - f(word, k+1)
    }
}
// @lc code=end

fun main() {
    println(Solution().countOfSubstrings("aeiou", 0)) // 1
    println(Solution().countOfSubstrings("ieaouqqieaouqq", 1)) // 3
}