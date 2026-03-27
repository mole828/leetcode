package problems.p2946
/*
 * @lc app=leetcode id=2946 lang=kotlin
 *
 * [2946] Matrix Similarity After Cyclic Shifts
 */
// @lc code=start
class Solution {
    fun areSimilar(mat: Array<IntArray>, k: Int): Boolean {
        val n = mat[0].size
        return mat.all { row -> 
            row.indices.all { j -> row[j] == row[(j + k) % n] } 
        }
    }
}
// @lc code=end

