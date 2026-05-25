/*
 * @lc app=leetcode id=2 lang=kotlin
 *
 * [2] Add Two Numbers
 *
 * https://leetcode.com/problems/add-two-numbers/description/
 *
 * algorithms
 * Medium (47.73%)
 * Likes:    36850
 * Dislikes: 7264
 * Total Accepted:    7.1M
 * Total Submissions: 14.6M
 * Testcase Example:  '[2,4,3]\n[5,6,4]'
 *
 * You are given two non-empty linked lists representing two non-negative
 * integers. The digits are stored in reverse order, and each of their nodes
 * contains a single digit. Add the two numbers and return the sum as a linked
 * list.
 * 
 * You may assume the two numbers do not contain any leading zero, except the
 * number 0 itself.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: l1 = [2,4,3], l2 = [5,6,4]
 * Output: [7,0,8]
 * Explanation: 342 + 465 = 807.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: l1 = [0], l2 = [0]
 * Output: [0]
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
 * Output: [8,9,9,9,0,0,0,1]
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * The number of nodes in each linked list is in the range [1, 100].
 * 0 <= Node.val <= 9
 * It is guaranteed that the list represents a number that does not have
 * leading zeros.
 * 
 * 
 */
package p2

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
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
        val dummy = ListNode()
        var p: ListNode = dummy
        var c = 0
        var l1 = l1
        var l2 = l2
        while (l1 != null && l2 != null) {
            c += l1.`val` + l2.`val`
            val next = ListNode(c % 10)
            p.next = next 
            c /= 10
            p = next
            l1 = l1.next
            l2 = l2.next
        }
        while (l1 != null) {
            c += l1.`val`
            val next = ListNode(c % 10)
            p.next = next
            c /= 10
            p = next
            l1 = l1.next
        }
        while (l2 != null) {
            c += l2.`val`
            val next = ListNode(c % 10)
            p.next = next
            c /= 10
            p = next
            l2 = l2.next
        }
        if (c > 0) {
            p.next = ListNode(c)
        }
        return dummy.next
    }
}
// @lc code=end

