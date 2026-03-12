import kotlin.math.min

/*
 * @lc app=leetcode id=3600 lang=kotlin
 *
 * [3600] Maximize Spanning Tree Stability with Upgrades
 */

// @lc code=start
class UnionFind (
    val n: Int,
) {
    var count = n
    val parent = IntArray(n) { it }
    fun find(x: Int): Int {
        return if (parent[x] == x) x else find(parent[x])
    }
    fun merge(from: Int, to: Int): Boolean {
        val x = find(from)
        val y = find(to)
        if (x==y) return false
        parent[x] = y
        count -= 1
        return true
    }
}
class Solution {
    fun maxStability(n: Int, edges: Array<IntArray>, k: Int): Int {
        val uf = UnionFind(n)
        val allUf = UnionFind(n)
        var minS1 = Int.MAX_VALUE
        for ((x,y,s,must) in edges) {
            if (must > 0) {
                if (uf.merge(x,y).not()) return -1
                minS1 = min(minS1, s)
            }
            allUf.merge(x,y)
        }
        if (allUf.count > 1) return -1
        var left = uf.count - 1
        if (left == 0) return minS1
        edges.sortBy { -it[2] }
        var ans = minS1
        for ((x,y,s,must) in edges) {
            if ((must>0).not() and uf.merge(x,y)) {
                ans = min(ans, (if (left > k) s else s * 2))
                left -= 1
                if (left == 0) break
            }
        }
        return ans
    }
}
// @lc code=end

