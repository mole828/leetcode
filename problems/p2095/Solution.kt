package p2095

/*
 * @lc app=leetcode id=2095 lang=kotlin
 *
 * [2095] Delete the Middle Node of a Linked List
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
    fun deleteMiddle(head: ListNode?): ListNode? {
        val dummy = ListNode(0, head)
        var prev = dummy
        var slow = head ?: return null
        var fast = head

        while (fast?.next != null) {
            prev = slow
            slow = slow.next ?: return dummy.next
            fast = fast.next?.next
        }

        prev.next = slow.next
        return dummy.next
    }
}
// @lc code=end
