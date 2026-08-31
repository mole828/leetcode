package p2058

/*
 * @lc app=leetcode id=2058 lang=kotlin
 *
 * [2058] Find the Minimum and Maximum Number of Nodes Between Critical Points
 */
class ListNode(var `val`: Int) {var next: ListNode? = null}
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
    fun nodesBetweenCriticalPoints(head: ListNode?): IntArray {
        var left = head ?: return intArrayOf(-1,-1)
        var mid = head.next ?: return intArrayOf(-1,-1)
        var right = mid.next
        
        val points = mutableListOf<Int>()
        var midIndex = 1
        while (right != null) {
            val other = listOf(left.`val`, right.`val`)
            if (other.all { it > mid.`val` } || other.all { it < mid.`val` }) {
                points.add(midIndex)
            }
            left = mid
            mid = right
            right = right.next
            midIndex++
        }
        println("points: $points")
        if (points.size < 2) return intArrayOf(-1,-1)
        return intArrayOf(
            (1..<points.size).minOf { points[it] - points[it-1] },
            points.last() - points.first(),    
        )
    }
}
// @lc code=end

