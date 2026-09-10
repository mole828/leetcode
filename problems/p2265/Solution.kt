package p2265

/*
 * @lc app=leetcode id=2265 lang=kotlin
 *
 * [2265] Count Nodes Equal to Average of Subtree
 */
import tools.TreeNode
// @lc code=start
/**
 * Example:
 * var ti = TreeNode(5)
 * var v = ti.`val`
 * Definition for a binary tree node.
 * class TreeNode(var `val`: Int) {
 *     var left: TreeNode? = null
 *     var right: TreeNode? = null
 * }
 */
class Solution {
    data class Result(val sum: Int, val count: Int, val equalCount: Int)
    fun dfs(node: TreeNode?): Result {
        var sum = 0
        var count = 0
        var equalCount = 0
        if (node != null) {
            val left = dfs(node.left)
            val right = dfs(node.right)
            sum = left.sum + right.sum + node.`val`
            count = left.count + right.count + 1
            equalCount = left.equalCount + right.equalCount
            if (sum / count == node.`val`) {
                equalCount++
            }
        }
        return Result(sum, count, equalCount)
    }
    fun averageOfSubtree(root: TreeNode?): Int {
        return dfs(root).equalCount
    }
}
// @lc code=end

