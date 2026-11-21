package p3331

/*
 * @lc app=leetcode id=3331 lang=kotlin
 *
 * [3331] Find Subtree Sizes After Changes
 *
 * https://leetcode.com/problems/find-subtree-sizes-after-changes/description/
 *
 * algorithms
 * Medium (52.85%)
 * Likes:    131
 * Dislikes: 44
 * Total Accepted:    25.1K
 * Total Submissions: 42.5K
 * Testcase Example:  '[-1,0,0,1,1,1]\n"abaabc"'
 *
 * You are given a tree rooted at node 0 that consists of n nodes numbered from
 * 0 to n - 1. The tree is represented by an array parent of size n, where
 * parent[i] is the parent of node i. Since node 0 is the root, parent[0] ==
 * -1.
 * 
 * You are also given a string s of length n, where s[i] is the character
 * assigned to node i.
 * 
 * We make the following changes on the tree one time simultaneously for all
 * nodes x from 1 to n - 1:
 * 
 * 
 * Find the closest node y to node x such that y is an ancestor of x, and s[x]
 * == s[y].
 * If node y does not exist, do nothing.
 * Otherwise, remove the edge between x and its current parent and make node y
 * the new parent of x by adding an edge between them.
 * 
 * 
 * Return an array answer of size n where answer[i] is the size of the subtree
 * rooted at node i in the final tree.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: parent = [-1,0,0,1,1,1], s = "abaabc"
 * 
 * Output: [6,3,1,1,1,1]
 * 
 * Explanation:
 * 
 * The parent of node 3 will change from node 1 to node 0.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: parent = [-1,0,4,0,1], s = "abbba"
 * 
 * Output: [5,2,1,1,1]
 * 
 * Explanation:
 * 
 * The following changes will happen at the same time:
 * 
 * 
 * The parent of node 4 will change from node 1 to node 0.
 * The parent of node 2 will change from node 4 to node 1.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * n == parent.length == s.length
 * 1 <= n <= 10^5
 * 0 <= parent[i] <= n - 1 for all i >= 1.
 * parent[0] == -1
 * parent represents a valid tree.
 * s consists only of lowercase English letters.
 * 
 * 
 */

// @lc code=start
class Solution {
    fun findSubtreeSizes(parent: IntArray, s: String): IntArray {
        val n = parent.size
        val grahp = Array(n) { mutableListOf<Int>() }
        for (i in 1..<grahp.size) grahp[parent[i]].add(i)

        val ancestor = IntArray(26) { -1 }
        fun Char.key() = this - 'a'
        fun rebuild(x: Int) {
            val old = ancestor[s[x].key()]
            ancestor[s[x].key()] = x
            for (i in grahp[x].indices) {
                val y = grahp[x][i]
                val anc = ancestor[s[y].key()]
                if (anc != -1) {
                    grahp[anc].add(y)
                    grahp[x][i] = -1
                }
                rebuild(y)
            }
            ancestor[s[x].key()] = old
        }
        rebuild(0)
        
        val size = IntArray(n) {1}
        fun dfs(x: Int) {
            grahp[x].forEach { y -> 
                if (y != -1) {
                    dfs(y)
                    size[x] += size[y]
                }
            }
        }
        dfs(0)

        return size
    }
}
// @lc code=end

