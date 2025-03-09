/*
 * @lc app=leetcode id=3208 lang=kotlin
 * @lcpr version=30204
 *
 * [3208] Alternating Groups II
 */


// @lcpr-template-start

// @lcpr-template-end

package leetcode.problem_3208
// @lc code=start
class Solution {
    fun isAlternating(window: List<Int>): Boolean {
        var last = window[0]
        for (i in 1.until(window.size)) {
            if (window[i] == last) {
                return false
            }
            last = window[i]
        }
        return true
    }
    /*
    Time Limit Exceeded
    533/625 cases passed (N/A)
    */
    fun _numberOfAlternatingGroups(colors: IntArray, k: Int): Int {
        val fakeCircle = (colors + colors).toList()
        return (0.until(colors.size)).count { predicate ->
            val isA = isAlternating(fakeCircle.subList(predicate, predicate + k))
            // println("[${predicate}, ${predicate + k}]: ${fakeCircle.subList(predicate, predicate + k)} isA: $isA")
            isA
        }
    }

    fun numberOfAlternatingGroups(colors: IntArray, k: Int): Int {
        val fakeCircle = (colors + colors).toList().toMutableList()
        var left = 0
        var right = k - 1
        val sameWindow = emptyList<Boolean>().toMutableList()
        for (i in 0.until(right)) {
            sameWindow.add(if (fakeCircle[i] == fakeCircle[i+1]) true else false)
        }
        var sameCount = sameWindow.count { it }
        fun stepIn() {
            val newIsSame = if (fakeCircle[right] == fakeCircle[right+1]) true else false
            sameCount += if (newIsSame) 1 else 0
            sameWindow.add(newIsSame)
            right += 1
            left += 1
            val popIsSame = sameWindow.removeAt(0)
            sameCount -= if (popIsSame) 1 else 0
        }
        var total = 0
        while (left < colors.size) {
            // println("""
            //     window: ${fakeCircle.subList(left, right)} 
            //     sameWindow: $sameWindow
            //     sameCount: $sameCount
            // """.trimIndent())
            if (sameCount == 0) {

                total += 1
            }
            stepIn()
        }
        return total
    }
}
// @lc code=end

fun main() {
    println(Solution().numberOfAlternatingGroups(listOf(0,1,0,1,0).toIntArray(), 3))
    println(Solution().numberOfAlternatingGroups(listOf(0,1,0,0,1,0,1).toIntArray(), 6))
}

/*
// @lcpr case=start
// [0,1,0,1,0]\n3\n
// @lcpr case=end

// @lcpr case=start
// [0,1,0,0,1,0,1]\n6\n
// @lcpr case=end

// @lcpr case=start
// [1,1,0,1]\n4\n
// @lcpr case=end

 */

