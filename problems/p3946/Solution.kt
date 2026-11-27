package p3946

import java.util.PriorityQueue

/*
 * @lc app=leetcode id=3946 lang=kotlin
 *
 * [3946] Maximum Number of Items From Sale I
 *
 * https://leetcode.com/problems/maximum-number-of-items-from-sale-i/description/
 *
 * algorithms
 * Medium (37.27%)
 * Likes:    100
 * Dislikes: 19
 * Total Accepted:    26.3K
 * Total Submissions: 64.8K
 * Testcase Example:  '[[6,2],[2,6],[3,4]]\n9'
 *
 * You are given a 2D integer array items, where items[i] = [factori, pricei]
 * represents the i^th item. You are also given an integer budget.
 * 
 * There are unlimited copies of each item available for purchase.You may buy
 * any number of copies of any items such that the total cost of the purchased
 * copies is at most budget.
 * 
 * After buying items, you may receive free copies according to the following
 * rules:
 * 
 * 
 * For each item i that you bought at least one copy of, you receive one free
 * copy of every item j such that j != i and factori divides factorj.
 * Buying multiple copies of the same item i does not give additional free
 * copies through item i.
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
 * Input: items = [[6,2],[2,6],[3,4]], budget = 9
 * 
 * Output: 4
 * 
 * Explanation:
 * 
 * 
 * You can buy 2 copies of item 0 and 1 copy of item 2 for a total cost of 2 *
 * 2 + 4 = 8, which is not greater than budget = 9.
 * Buying item 2 gives 1 free copy of item 0, because factor2 = 3 divides
 * factor0 = 6.
 * You leave with 3 purchased copies and 1 free copy, for a total of 4 item
 * copies.
 * 
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: items = [[2,4],[3,2],[4,1],[6,4],[12,4]], budget = 8
 * 
 * Output: 10
 * 
 * Explanation:
 * 
 * 
 * You can buy 1 copy of item 0, 1 copy of item 1, and 2 copies of item 2 for a
 * total cost of 4 + 2 + 2 * 1 = 8.
 * Buying item 0 gives 1 free copy of items 2, 3, and 4.
 * Buying item 1 gives 1 free copy of items 3 and 4.
 * Buying item 2 gives 1 free copy of item 4.
 * Thus, you receive 6 free copies. You leave with 4 purchased copies and 6
 * free copies, for a total of 10 item copies.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= items.length <= 1000
 * items[i] = [factori, pricei]
 * 1 <= factori, pricei <= 1500
 * 1 <= budget <= 1500
 * 
 * 
 */

// @lc code=start
class Solution {
    private data class Product(val cost: Int, val got: Int, val gotPerCost: Float)
    fun maximumSaleItems0(items: Array<IntArray>, budget: Int): Int {
        val que = PriorityQueue<Product>(
            compareBy<Product> { it.gotPerCost }
        )
        items.forEachIndexed { i, prodI -> 
            val (factorI, costI) = prodI
            var got = 1
            items.forEachIndexed { j, prodJ ->
                val (factorJ, costJ) = prodJ
                if (i == j) return@forEachIndexed
                if (factorJ % factorI == 0) got += 1
            }
            val firstProduct = Product(cost = costI, got = got, gotPerCost = costI.toFloat() / got)
            que.add(firstProduct)
            val normalProduct = Product(cost = costI, got = 1, gotPerCost = costI.toFloat())
            val addTime = budget / costI + 1
            repeat(addTime) { que.add(normalProduct) }
        }
        var ans = 0
        var lastBudget = budget
        while (que.isNotEmpty()) {
            val product = que.poll()!!
            if (lastBudget >= product.cost) {
                ans += product.got
                lastBudget -= product.cost
            }
        }
        return ans
    }

    fun maximumSaleItems(items: Array<IntArray>, budget: Int): Int {
        val f = IntArray(budget + 1)
        var mn = Int.MAX_VALUE
        for (item in items) {
            val (factor, price) = item
            mn = minOf(mn, price)
            val cnt = items.count { it[0] % factor == 0 }
            for (j in budget downTo price) {
                f[j] = maxOf(f[j], f[j - price] + cnt)
            }
        }
        return (0..budget).maxOf { f[it] + (budget - it) / mn }
    }
}
// @lc code=end

