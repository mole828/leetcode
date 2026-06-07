package problems.p2196
/*
 * @lc app=leetcode id=2196 lang=kotlin
 *
 * [2196] Create Binary Tree From Descriptions
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
    fun createBinaryTree(descriptions: Array<IntArray>): TreeNode? {
        val nodes = mutableMapOf<Int, TreeNode>()
        descriptions.forEach { (parent, child, isLeft) ->
            val parentNode = nodes.getOrPut(parent) { TreeNode(parent) }
            val childNode = nodes.getOrPut(child) { TreeNode(child) }
            if (isLeft == 1) {
                parentNode.left = childNode
            } else {
                parentNode.right = childNode
            }
        }
        val children = descriptions.map { it[1] }.toSet()
        return nodes.values.firstOrNull { it.`val` !in children }
    }
}
// @lc code=end

