package p1833
/*
 * @lc app=leetcode id=1833 lang=kotlin
 *
 * [1833] Maximum Ice Cream Bars
 */
// @lc code=start
class Solution {
    fun maxIceCream(costs: IntArray, coins: Int): Int {
        costs.sort()
        var iceCreams = 0
        var remainingCoins = coins
        for (cost in costs) {
            if (remainingCoins >= cost) {
                remainingCoins -= cost
                iceCreams++
            } else {
                break
            }
        }
        return iceCreams
    }
}
// @lc code=end

