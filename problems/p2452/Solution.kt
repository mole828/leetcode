package problems.p2452
/*
 * @lc app=leetcode id=2452 lang=kotlin
 *
 * [2452] Words Within Two Edits of Dictionary
 */

// @lc code=start
class Solution {
    fun twoEditWords(queries: Array<String>, dictionary: Array<String>): List<String> {
        return queries.filter { query ->
            dictionary.any { dictWord ->
                query.indices.count { i -> query[i] != dictWord[i] } <= 2
            }
        }
    }
}
// @lc code=end

