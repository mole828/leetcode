package problems.p3548
/*
 * @lc app=leetcode id=3548 lang=kotlin
 *
 * [3548] Equal Sum Grid Partition II
 */

// @lc code=start
class Solution {
    fun canPartitionGrid(grid: Array<IntArray>): Boolean {
        val longGrid = grid.map { it.map { x -> x.toLong() } }
        val total = longGrid.sumOf { row -> row.sum() }

        fun check(a: List<List<Long>>): Boolean {
            val m = a.size
            val n = a[0].size

            fun f(arr: List<List<Long>>): Boolean {
                val st = mutableSetOf<Long>(0L) // 0 表示不删除数字
                var s = 0L

                for (i in 0 until m - 1) {
                    val row = arr[i]
                    for (j in row.indices) {
                        val x = row[j]
                        s += x
                        // 第一行，不能删除中间元素
                        if (i > 0 || j == 0 || j == n - 1) {
                            st.add(x)
                        }
                    }

                    // 特殊处理只有一列的情况，此时只能删除第一个数或者分割线上那个数
                    if (n == 1) {
                        if (s * 2 == total ||
                            s * 2 - total == arr[0][0] ||
                            s * 2 - total == row[0]
                        ) {
                            return true
                        }
                        continue
                    }

                    if ((s * 2 - total) in st) {
                        return true
                    }

                    // 如果分割到更下面，那么可以删第一行的元素
                    if (i == 0) {
                        for (x in row) {
                            st.add(x)
                        }
                    }
                }
                return false
            }

            // 删除上半部分中的数 or 删除下半部分中的数
            return f(a) || f(a.asReversed())
        }

        val gridList = longGrid.map { row -> row.toList() }
        val transposed = List(longGrid[0].size) { j ->
            List(longGrid.size) { i -> longGrid[i][j] }
        }

        // 水平分割 or 垂直分割
        return check(gridList) || check(transposed)
    }
}
// @lc code=end

