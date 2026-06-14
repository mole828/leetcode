package p2130
/*
 * @lc app=leetcode id=2130 lang=kotlin
 *
 * [2130] Maximum Twin Sum of a Linked List
 */
import tools.ListNode
// @lc code=start
/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class Solution {
    fun pairSum(head: ListNode?): Int {
        var left = head?: return 0
        var ans = 0
        fun dfs(right: ListNode) {
            right.next?.let { dfs(it) }
            ans = maxOf(ans, left.`val` + right.`val`)
            left = left.next ?: return
        }
        dfs(head)
        return ans
    }
}
// @lc code=end

