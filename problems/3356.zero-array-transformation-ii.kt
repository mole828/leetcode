/*
 * @lc app=leetcode id=3356 lang=kotlin
 *
 * [3356] Zero Array Transformation II
 */
package p3356

import kotlin.collections.mutableSetOf
// @lc code=start
class Solution {
    // Time Limit Exceeded
    // 623/627 cases passed
    fun _minZeroArray(nums: IntArray, queries: Array<IntArray>): Int {
        var notZero = nums.count { it!=0 }
        if (notZero==0)return 0
        fun down(index: Int, value: Int) {
            val oldValue = nums[index]
            val newValue = listOf(oldValue-value, 0).max()
            nums[index] = newValue
            if ((oldValue!=0)and(newValue==0)){
                notZero -= 1
            }
        }
        var round = 0
        for(querie in queries) {
            if(notZero == 0) break
            val v = querie[2]
            querie[0].rangeTo(querie[1]).forEach {
                down(it, v)
            }
            round += 1
            // println(nums.toList())
        }
        if(notZero!=0)return -1
        return round
    }
    fun __minZeroArray(nums: IntArray, queries: Array<IntArray>): Int {
        val notDown = nums.mapIndexed { i,v->i to v }.filter { it.second!=0 }.map{it.first}.toMutableSet()
        var round = 0
        for(querie in queries) {
            if (notDown.isEmpty()){break}
            val v = querie[2]
            querie[0].rangeTo(querie[1]).forEach {
                if(it in notDown) {
                    val newValue = listOf(nums[it]-v, 0).max()
                    nums[it] = newValue
                    if (newValue==0) {
                        notDown.remove(it)
                    }
                }
            }
            round += 1
        }
        if (notDown.isEmpty())return round
        return -1
    }

    fun minZeroArray(nums: IntArray, queries: Array<IntArray>): Int {
        val n = nums.size
        val diff = (0..(n+1)).map{0}.toMutableList()
        var (sumD, k) = listOf(0 , 0)
        nums.forEachIndexed { index, value -> 
            sumD += diff[index]
            while (k < queries.size && sumD < value) {
                val (left, right, diffValue) = queries[k]
                diff[left] += diffValue
                diff[right+1] -= diffValue
                if (left<=index && index<=right) sumD += diffValue
                k+=1
            }
            if (sumD < value) return -1
        }
        return k
    }
}
// @lc code=end

fun main() {
    println(Solution().minZeroArray(intArrayOf(2,0,2), arrayOf(
        intArrayOf(0,2,1),
        intArrayOf(0,2,1),
        intArrayOf(1,1,3),
    )))
}