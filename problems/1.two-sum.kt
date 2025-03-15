package p1

class Solution {
    fun twoSum(nums: IntArray, target: Int): IntArray {
        val map = mutableMapOf<Int, Int>()
        nums.forEachIndexed { index, i ->
            val j = map[i]
            j?.run {
                return@twoSum intArrayOf(j, index)
            }
            map.put(target-i, index)
        }
        return intArrayOf()
    }
}

fun main() {
    println(Solution().twoSum(intArrayOf(2,7,11,13), 9).map { it })
}