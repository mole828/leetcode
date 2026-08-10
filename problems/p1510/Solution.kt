/*
 * @lc app=leetcode id=1510 lang=kotlin
 *
 * [1510] Stone Game IV
 *
 * https://leetcode.com/problems/stone-game-iv/description/
 *
 * algorithms
 * Hard (59.61%)
 * Likes:    1667
 * Dislikes: 76
 * Total Accepted:    91.1K
 * Total Submissions: 150.8K
 * Testcase Example:  '1'
 *
 * Alice and Bob take turns playing a game, with Alice starting first.
 * 
 * Initially, there are n stones in a pile. On each player's turn, that player
 * makes a move consisting of removing any non-zero square number of stones in
 * the pile.
 * 
 * Also, if a player cannot make a move, he/she loses the game.
 * 
 * Given a positive integer n, return true if and only if Alice wins the game
 * otherwise return false, assuming both players play optimally.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 1
 * Output: true
 * Explanation: Alice can remove 1 stone winning the game because Bob doesn't
 * have any moves.
 * 
 * Example 2:
 * 
 * 
 * Input: n = 2
 * Output: false
 * Explanation: Alice can only remove 1 stone, after that Bob removes the last
 * one winning the game (2 -> 1 -> 0).
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: n = 4
 * Output: true
 * Explanation: n is already a perfect square, Alice can win with one move,
 * removing 4 stones (4 -> 0).
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 10^5
 * 
 * 
 */
package p1510
// @lc code=start
class Solution {
    val squareSet = (1..320).map { it*it }.toSet()
    val memo = mutableMapOf<Int, Boolean>()
    fun winnerSquareGame(n: Int): Boolean {
        if (n<=0) return false
        if (n in squareSet) return true
        memo[n]?.let { return it }
        val res = squareSet.filter { it <= n }.any { winnerSquareGame(n-it).not() }
        memo[n] = res
        return res
    }
}
// @lc code=end

