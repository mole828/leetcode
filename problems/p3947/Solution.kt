package p3947

/*
 * @lc app=leetcode id=3947 lang=kotlin
 *
 * [3947] Maximum Number of Items From Sale II
 *
 * https://leetcode.com/problems/maximum-number-of-items-from-sale-ii/description/
 *
 * algorithms
 * Medium (30.19%)
 * Likes:    68
 * Dislikes: 19
 * Total Accepted:    12.9K
 * Total Submissions: 30.9K
 * Testcase Example:  '[[1,6],[2,4],[3,5]]\n19'
 *
 * You are given a 2D integer array items, where items[i] = [factori, pricei]
 * represents the i^th item. You are also given an integer budget.
 * 
 * There are unlimited copies of each item available for purchase. You may buy
 * any number of copies of any items such that the total cost of the purchased
 * copies is at most budget.
 * 
 * After buying items, you may receive free copies according to the following
 * rules:
 * 
 * 
 * Each purchased copy of item i can give you at most one free copy of another
 * item j.
 * The free item must satisfy i != j and factori divides factorj.
 * For each ordered pair (i, j), you can receive a free copy of item j from
 * purchases of item i at most once, regardless of how many copies of item i
 * you buy.
 * The same item j can be received multiple times for free if it is received
 * from purchases of different item types.
 * 
 * 
 * Return the maximum total number of item copies you can obtain, including
 * both purchased copies and free copies, while spending at most budget on
 * purchased items.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: items = [[1,6],[2,4],[3,5]], budget = 19
 * 
 * Output: 5
 * 
 * Explanation:
 * 
 * 
 * You can buy 2 copies of item 0 and 1 copy of item 1 for a total cost of 2 *
 * 6 + 4 = 16, which is not greater than budget = 19.
 * One purchased copy of item 0 gives 1 free copy of item 1, because factor0 =
 * 1 divides factor1 = 2.
 * The other purchased copy of item 0 gives 1 free copy of item 2, because
 * factor0 = 1 divides factor2 = 3.
 * You leave with 3 purchased copies and 2 free copies, for a total of 5 item
 * copies.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: items = [[2,8],[1,10],[6,6],[4,12],[5,20],[5,17]], budget = 35
 * 
 * Output: 7
 * 
 * Explanation:
 * 
 * 
 * You can buy 2 copies of item 0, 1 copy of item 1, and 1 copy of item 2 for a
 * total cost of 2 * 8 + 10 + 6 = 32, which is not greater than budget =
 * 35.
 * One purchased copy of item 0 gives 1 free copy of item 2, because factor0 =
 * 2 divides factor2 = 6.
 * The other purchased copy of item 0 gives 1 free copy of item 3, because
 * factor0 = 2 divides factor3 = 4.
 * The purchased copy of item 1 gives 1 free copy of item 2, because factor1 =
 * 1 divides factor2 = 6.
 * Buying item 2 gives no free copy, because factor2 = 6 does not divide the
 * factor of any other item.
 * You leave with 4 purchased copies and 3 free copies, for a total of 7 item
 * copies.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= items.length <= 10^5
 * items[i] = [factori, pricei]
 * 1 <= factori <= items.length
 * 1 <= pricei <= 10^9
 * 1 <= budget <= 10^9
 * 
 * 
 */

// @lc code=start
class Solution {
    // TODO
    fun maximumSaleItems(items: Array<IntArray>, budget: Int): Int {
        val n = items.size
        val cntFactor = IntArray(n + 1)
        var minPrice = Int.MAX_VALUE
        for ((factor, price) in items) {
            cntFactor[factor]++
            minPrice = minOf(minPrice, price)
        }

        // deals: 价格 < 2 * minPrice 时，前 cnt 次购买每次得到 2 件（自己 + 1 件免费）
        val cntMulti = IntArray(n + 1)
        val deals = mutableListOf<Pair<Int, Int>>()
        for ((factor, price) in items) {
            if (price >= minPrice * 2) continue
            if (cntMulti[factor] == 0) {
                for (j in factor..n step factor) cntMulti[factor] += cntFactor[j]
            }
            if (cntMulti[factor] > 1) deals += price to cntMulti[factor] - 1
        }
        deals.sortBy { it.first }

        var ans = 0
        var rest = budget
        for ((price, cnt) in deals) {
            if (rest < price) break
            val c = minOf(cnt, rest / price)
            rest -= price * c
            ans += c * 2
        }
        return ans + rest / minPrice
    }
}
// @lc code=end

