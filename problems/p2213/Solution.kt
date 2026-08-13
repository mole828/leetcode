/*
 * @lc app=leetcode id=2213 lang=kotlin
 *
 * [2213] Longest Substring of One Repeating Character
 *
 * https://leetcode.com/problems/longest-substring-of-one-repeating-character/description/
 *
 * algorithms
 * Hard (34.65%)
 * Likes:    343
 * Dislikes: 84
 * Total Accepted:    9.1K
 * Total Submissions: 23K
 * Testcase Example:  '"babacc"\n"bcb"\n[1,3,3]'
 *
 * You are given a 0-indexed string s. You are also given a 0-indexed string
 * queryCharacters of length k and a 0-indexed array of integer indices
 * queryIndices of length k, both of which are used to describe k queries.
 * 
 * The i^th query updates the character in s at index queryIndices[i] to the
 * character queryCharacters[i].
 * 
 * Return an array lengths of length k where lengths[i] is the length of the
 * longest substring of s consisting of only one repeating character after the
 * i^th query is performed.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: s = "babacc", queryCharacters = "bcb", queryIndices = [1,3,3]
 * Output: [3,3,4]
 * Explanation: 
 * - 1^st query updates s = "bbbacc". The longest substring consisting of one
 * repeating character is "bbb" with length 3.
 * - 2^nd query updates s = "bbbccc". 
 * ⁠ The longest substring consisting of one repeating character can be "bbb"
 * or "ccc" with length 3.
 * - 3^rd query updates s = "bbbbcc". The longest substring consisting of one
 * repeating character is "bbbb" with length 4.
 * Thus, we return [3,3,4].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: s = "abyzz", queryCharacters = "aa", queryIndices = [2,1]
 * Output: [2,3]
 * Explanation:
 * - 1^st query updates s = "abazz". The longest substring consisting of one
 * repeating character is "zz" with length 2.
 * - 2^nd query updates s = "aaazz". The longest substring consisting of one
 * repeating character is "aaa" with length 3.
 * Thus, we return [2,3].
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= s.length <= 10^5
 * s consists of lowercase English letters.
 * k == queryCharacters.length == queryIndices.length
 * 1 <= k <= 10^5
 * queryCharacters consists of lowercase English letters.
 * 0 <= queryIndices[i] < s.length
 * 
 * 
 */
package p2213

// @lc code=start
class Solution {
    // 暴力做法：每次修改之后，都重新扫描整个字符串。
    fun longestRepeating0(s: String, queryCharacters: String, queryIndices: IntArray): IntArray {
        val n = queryCharacters.length
        val str = StringBuilder(s)
        fun maxRepeating(): Int {
            var maxRepeatTime = 0
            var lastChar = '@'
            var repeatTime = 0
            str.forEach { c ->
                if (c != lastChar) {
                    lastChar = c
                    repeatTime = 0
                }
                repeatTime += 1
                if (repeatTime > maxRepeatTime) maxRepeatTime = repeatTime
            }
            return maxRepeatTime
        }
        return (0..<n).map { i ->
            val index = queryIndices[i]
            val char = queryCharacters[i]
            str[index] = char
            maxRepeating()
        }.toIntArray()
    }

    // 线段树做法：每次修改一个位置之后，只更新从叶子到根的一条路径。
    fun longestRepeating(s: String, queryCharacters: String, queryIndices: IntArray): IntArray {
        val segmentTree = SegmentTree(s)

        return queryIndices.indices.map { i ->
            segmentTree.update(queryIndices[i], queryCharacters[i])
            segmentTree.longestRepeatingLength()
        }.toIntArray()
    }

    private class SegmentTree(private val source: String) {
        private val tree = arrayOfNulls<Node>(source.length * 4)

        init {
            build(node = 1, left = 0, right = source.lastIndex)
        }

        fun update(index: Int, character: Char) {
            update(node = 1, left = 0, right = source.lastIndex, index, character)
        }

        fun longestRepeatingLength(): Int {
            return getNode(1).best
        }

        private fun build(node: Int, left: Int, right: Int) {
            if (left == right) {
                tree[node] = Node(
                    length = 1,
                    leftChar = source[left],
                    rightChar = source[left],
                    prefix = 1,
                    suffix = 1,
                    best = 1
                )
                return
            }

            val middle = (left + right) / 2
            build(node * 2, left, middle)
            build(node * 2 + 1, middle + 1, right)
            tree[node] = merge(getNode(node * 2), getNode(node * 2 + 1))
        }

        private fun update(
            node: Int,
            left: Int,
            right: Int,
            index: Int,
            character: Char
        ) {
            if (left == right) {
                tree[node] = Node(
                    length = 1,
                    leftChar = character,
                    rightChar = character,
                    prefix = 1,
                    suffix = 1,
                    best = 1
                )
                return
            }

            val middle = (left + right) / 2
            if (index <= middle) {
                update(node * 2, left, middle, index, character)
            } else {
                update(node * 2 + 1, middle + 1, right, index, character)
            }

            tree[node] = merge(getNode(node * 2), getNode(node * 2 + 1))
        }

        private fun merge(leftNode: Node, rightNode: Node): Node {
            val length = leftNode.length + rightNode.length
            val sameBoundaryCharacter = leftNode.rightChar == rightNode.leftChar

            var prefix = leftNode.prefix
            if (leftNode.prefix == leftNode.length && sameBoundaryCharacter) {
                prefix = leftNode.length + rightNode.prefix
            }

            var suffix = rightNode.suffix
            if (rightNode.suffix == rightNode.length && sameBoundaryCharacter) {
                suffix = rightNode.length + leftNode.suffix
            }

            var best = maxOf(leftNode.best, rightNode.best)
            if (sameBoundaryCharacter) {
                best = maxOf(best, leftNode.suffix + rightNode.prefix)
            }

            return Node(
                length = length,
                leftChar = leftNode.leftChar,
                rightChar = rightNode.rightChar,
                prefix = prefix,
                suffix = suffix,
                best = best
            )
        }

        private fun getNode(index: Int): Node {
            return requireNotNull(tree[index])
        }

        private data class Node(
            val length: Int,
            val leftChar: Char,
            val rightChar: Char,
            val prefix: Int,
            val suffix: Int,
            val best: Int
        )
    }
}
// @lc code=end
