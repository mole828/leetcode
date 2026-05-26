/*
 * @lc app=leetcode id=3120 lang=kotlin
 *
 * [3120] Count the Number of Special Characters I
 *
 * https://leetcode.com/problems/count-the-number-of-special-characters-i/description/
 *
 * algorithms
 * Easy (66.92%)
 * Likes:    181
 * Dislikes: 6
 * Total Accepted:    66.9K
 * Total Submissions: 99.4K
 * Testcase Example:  '"aaAbcBC"'
 *
 * You are given a string word. A letter is called special if it appears both
 * in lowercase and uppercase in word.
 * 
 * Return the number of special letters in word.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: word = "aaAbcBC"
 * 
 * Output: 3
 * 
 * Explanation:
 * 
 * The special characters in word are 'a', 'b', and 'c'.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: word = "abc"
 * 
 * Output: 0
 * 
 * Explanation:
 * 
 * No character in word appears in uppercase.
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: word = "abBCab"
 * 
 * Output: 1
 * 
 * Explanation:
 * 
 * The only special character in word is 'b'.
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= word.length <= 50
 * word consists of only lowercase and uppercase English letters.
 * 
 * 
 */
package p3120
// @lc code=start
class Solution {
    fun numberOfSpecialChars(word: String): Int {
        return ('a'..'z').count { it in word && it.uppercaseChar() in word }
    }
}
// @lc code=end
