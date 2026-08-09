/*
 * @lc app=leetcode id=1140 lang=kotlin
 *
 * [1140] Stone Game II
 *
 * https://leetcode.com/problems/stone-game-ii/description/
 *
 * algorithms
 * Medium (72.82%)
 * Likes:    3577
 * Dislikes: 946
 * Total Accepted:    216.8K
 * Total Submissions: 295.5K
 * Testcase Example:  '[2,7,9,4,4]'
 *
 * Alice and Bob continue their games with piles of stones. There are a number
 * of piles arranged in a row, and each pile has a positive integer number of
 * stones piles[i]. The objective of the game is to end with the most stones.
 * 
 * Alice and Bob take turns, with Alice starting first.
 * 
 * On each player's turn, that player can take all the stones in the first X
 * remaining piles, where 1 <= X <= 2M. Then, we set M = max(M, X). Initially,
 * M = 1.
 * 
 * The game continues until all the stones have been taken.
 * 
 * Assuming Alice and Bob play optimally, return the maximum number of stones
 * Alice can get.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: piles = [2,7,9,4,4]
 * 
 * Output: 10
 * 
 * Explanation:
 * 
 * 
 * If Alice takes one pile at the beginning, Bob takes two piles, then Alice
 * takes 2 piles again. Alice can get 2 + 4 + 4 = 10 stones in total.
 * If Alice takes two piles at the beginning, then Bob can take all three piles
 * left. In this case, Alice get 2 + 7 = 9 stones in total.
 * 
 * 
 * So we return 10 since it's larger.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: piles = [1,2,3,4,5,100]
 * 
 * Output: 104
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= piles.length <= 100
 * 1 <= piles[i] <= 10^4
 * 
 * 
 */
package p1140

import kotlin.math.max

// @lc code=start
class Solution {
    fun stoneGameII(piles: IntArray): Int {
        val n = piles.size
        for(i in (n-2) downTo 0) piles[i] += piles[i+1]

        val memo = Array(n) { IntArray(n/2+1){ -1 } }
        fun dfs(i: Int, m: Int): Int {
            if (i + m * 2 >= n) return piles[i]
            if (memo[i][m] != -1) return memo[i][m]
            val res = piles[i] - (1..(m*2)).minOf { x ->
                dfs(i+x, max(m,x))
            }
            memo[i][m] = res
            return res
        }
        return dfs(0,1)
    }
}
// @lc code=end

