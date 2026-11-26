package p3360

/*
 * @lc app=leetcode id=3360 lang=kotlin
 *
 * [3360] Stone Removal Game
 *
 * https://leetcode.com/problems/stone-removal-game/description/
 *
 * algorithms
 * Easy (42.60%)
 * Likes:    99
 * Dislikes: 6
 * Total Accepted:    42.9K
 * Total Submissions: 95K
 * Testcase Example:  '12'
 *
 * Alice and Bob are playing a game where they take turns removing stones from
 * a pile, with Alice going first.
 * 
 * 
 * Alice starts by removing exactly 10 stones on her first turn.
 * For each subsequent turn, each player removes exactly 1 fewer stone than the
 * previous opponent.
 * 
 * 
 * The player who cannot make a move loses the game.
 * 
 * Given a positive integer n, return true if Alice wins the game and false
 * otherwise.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 12
 * 
 * Output: true
 * 
 * Explanation:
 * 
 * 
 * Alice removes 10 stones on her first turn, leaving 2 stones for Bob.
 * Bob cannot remove 9 stones, so Alice wins.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 1
 * 
 * Output: false
 * 
 * Explanation:
 * 
 * 
 * Alice cannot remove 10 stones, so Alice loses.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n <= 50
 * 
 * 
 */

// @lc code=start
class Solution {
    fun canAliceWin(n: Int): Boolean {
        var aliceTurn = true
        var pickNum = 10
        var last = n
        while (last >= pickNum) {
            last -= pickNum
            pickNum -= 1
            aliceTurn = !aliceTurn
        }
        return !aliceTurn
    }
}
// @lc code=end

