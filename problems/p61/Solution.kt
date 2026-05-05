package problems.p61

import problems.tools.ListNode

/*
 * @lc app=leetcode id=61 lang=kotlin
 *
 * [61] Rotate List
 */
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
    fun rotateRight(head: ListNode?, k: Int): ListNode? {
        if (head?.next == null || k == 0) return head

        var length = 1
        var tail = head
        while (tail?.next != null) {
            tail = tail.next
            length++
        }

        val stepsToNewTail = length - k % length
        if (stepsToNewTail == length) return head

        tail?.next = head

        var newTail = head
        repeat(stepsToNewTail - 1) {
            newTail = newTail?.next
        }

        val newHead = newTail?.next
        newTail?.next = null
        return newHead
    }
}
// @lc code=end
