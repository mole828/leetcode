/*
 * @lc app=leetcode id=3093 lang=kotlin
 *
 * [3093] Longest Common Suffix Queries
 *
 * https://leetcode.com/problems/longest-common-suffix-queries/description/
 *
 * algorithms
 * Hard (35.89%)
 * Likes:    214
 * Dislikes: 23
 * Total Accepted:    18.3K
 * Total Submissions: 46.8K
 * Testcase Example:  '["abcd","bcd","xbcd"]\n["cd","bcd","xyz"]'
 *
 * You are given two arrays of strings wordsContainer and wordsQuery.
 * 
 * For each wordsQuery[i], you need to find a string from wordsContainer that
 * has the longest common suffix with wordsQuery[i]. If there are two or more
 * strings in wordsContainer that share the longest common suffix, find the
 * string that is the smallest in length. If there are two or more such strings
 * that have the same smallest length, find the one that occurred earlier in
 * wordsContainer.
 * 
 * Return an array of integers ans, where ans[i] is the index of the string in
 * wordsContainer that has the longest common suffix with wordsQuery[i].
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: wordsContainer = ["abcd","bcd","xbcd"], wordsQuery =
 * ["cd","bcd","xyz"]
 * 
 * Output: [1,1,1]
 * 
 * Explanation:
 * 
 * Let's look at each wordsQuery[i] separately:
 * 
 * 
 * For wordsQuery[0] = "cd", strings from wordsContainer that share the longest
 * common suffix "cd" are at indices 0, 1, and 2. Among these, the answer is
 * the string at index 1 because it has the shortest length of 3.
 * For wordsQuery[1] = "bcd", strings from wordsContainer that share the
 * longest common suffix "bcd" are at indices 0, 1, and 2. Among these, the
 * answer is the string at index 1 because it has the shortest length of 3.
 * For wordsQuery[2] = "xyz", there is no string from wordsContainer that
 * shares a common suffix. Hence the longest common suffix is "", that is
 * shared with strings at index 0, 1, and 2. Among these, the answer is the
 * string at index 1 because it has the shortest length of 3.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: wordsContainer = ["abcdefgh","poiuygh","ghghgh"], wordsQuery =
 * ["gh","acbfgh","acbfegh"]
 * 
 * Output: [2,0,2]
 * 
 * Explanation:
 * 
 * Let's look at each wordsQuery[i] separately:
 * 
 * 
 * For wordsQuery[0] = "gh", strings from wordsContainer that share the longest
 * common suffix "gh" are at indices 0, 1, and 2. Among these, the answer is
 * the string at index 2 because it has the shortest length of 6.
 * For wordsQuery[1] = "acbfgh", only the string at index 0 shares the longest
 * common suffix "fgh". Hence it is the answer, even though the string at index
 * 2 is shorter.
 * For wordsQuery[2] = "acbfegh", strings from wordsContainer that share the
 * longest common suffix "gh" are at indices 0, 1, and 2. Among these, the
 * answer is the string at index 2 because it has the shortest length of
 * 6.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= wordsContainer.length, wordsQuery.length <= 10^4
 * 1 <= wordsContainer[i].length <= 5 * 10^3
 * 1 <= wordsQuery[i].length <= 5 * 10^3
 * wordsContainer[i] consists only of lowercase English letters.
 * wordsQuery[i] consists only of lowercase English letters.
 * Sum of wordsContainer[i].length is at most 5 * 10^5.
 * Sum of wordsQuery[i].length is at most 5 * 10^5.
 * 
 * 
 */
package p3093
// @lc code=start
class Solution {
    private class Node {
        val son = arrayOfNulls<Node>(26)
        var minLen = Int.MAX_VALUE
        var bestIndex = 0
    }
    fun stringIndices(wordsContainer: Array<String>, wordsQuery: Array<String>): IntArray {
        val root = Node()
        val ordA = 'a'.code

        for ((i, s) in wordsContainer.withIndex()) {
            val len = s.length

            if (len < root.minLen) {
                root.minLen = len
                root.bestIndex = i
            }

            var cur = root
            for (idx in s.length - 1 downTo 0) {
                val c = s[idx].code - ordA

                if (cur.son[c] == null) {
                    cur.son[c] = Node()
                }

                cur = cur.son[c]!!

                if (len < cur.minLen) {
                    cur.minLen = len
                    cur.bestIndex = i
                }
            }
        }

        val ans = IntArray(wordsQuery.size)

        for ((qi, s) in wordsQuery.withIndex()) {
            var cur = root

            for (idx in s.length - 1 downTo 0) {
                val c = s[idx].code - ordA
                val next = cur.son[c] ?: break
                cur = next
            }

            ans[qi] = cur.bestIndex
        }

        return ans
    }
}
// @lc code=end

