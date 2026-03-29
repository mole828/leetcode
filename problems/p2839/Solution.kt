package problems.p2839
/*
 * @lc app=leetcode id=2839 lang=kotlin
 *
 * [2839] Check if Strings Can be Made Equal With Operations I
 */
// @lc code=start
class Solution {
    fun canBeEqual(s1: String, s2: String): Boolean {
        fun getGroups(s: String): List<Set<Char>> {
            return s.mapIndexed { i,c -> 
                i to c 
            }.groupBy { 
                it.first % 2
            }.map { group ->
                group.value.map { it.second }.toSet()
            }
        }
        val g0 = getGroups(s1)
        val g1 = getGroups(s2)
        println("$g0, $g1")
        return g0 == g1
    }
}
// @lc code=end

