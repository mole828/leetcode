package p3863

/*
 * @lc app=leetcode id=3863 lang=kotlin
 *
 * [3863] Minimum Operations to Sort a String
 *
 * https://leetcode.com/problems/minimum-operations-to-sort-a-string/description/
 *
 * algorithms
 * Medium (19.26%)
 * Likes:    123
 * Dislikes: 17
 * Total Accepted:    24.3K
 * Total Submissions: 106.8K
 * Testcase Example:  '"dog"'
 *
 * You are given a string s consisting of lowercase English letters.
 * 
 * In one operation, you can select any substring of s that is not the entire
 * string and sort it in non-descending alphabetical order.
 * 
 * Return the minimum number of operations required to make s sorted in
 * non-descending order. If it is not possible, return -1.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "dog"
 * 
 * Output: 1
 * 
 * Explanation:​​​​​​​
 * 
 * 
 * Sort substring "og" to "go".
 * Now, s = "dgo", which is sorted in ascending order. Thus, the answer is
 * 1.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "card"
 * 
 * Output: 2
 * 
 * Explanation:
 * 
 * 
 * Sort substring "car" to "acr", so s = "acrd".
 * Sort substring "rd" to "dr", making s = "acdr", which is sorted in ascending
 * order. Thus, the answer is 2.
 * 
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: s = "gf"
 * 
 * Output: -1
 * 
 * Explanation:
 * 
 * 
 * It is impossible to sort s under the given constraints. Thus, the answer is
 * -1.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s consists of only lowercase English letters.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun minOperations(s: String): Int {
        val list = s.map { it.code }
        val sorted = list.sorted()
        if (list == sorted) return 0
        if (list.size == 2) return -1
        return when {
            list.first() == sorted.first() || list.last() == sorted.last() -> 1
            list.first() == sorted.last() && list.last() == sorted.first() && 
                list.count { it == sorted.first() } == 1 &&
                list.count { it == sorted.last() } == 1 -> 3
            else -> 2
        }
    }
}
// @lc code=end

