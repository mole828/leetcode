package p1967

/*
 * @lc app=leetcode id=1967 lang=kotlin
 *
 * [1967] Number of Strings That Appear as Substrings in Word
 */

// @lc code=start
class Solution 
fun Solution.numOfStrings(patterns: Array<String>, word: String): Int = patterns.count { word.contains(it) }
// @lc code=end

