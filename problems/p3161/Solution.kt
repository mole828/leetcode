/*
 * @lc app=leetcode id=3161 lang=kotlin
 *
 * [3161] Block Placement Queries
 *
 * https://leetcode.com/problems/block-placement-queries/description/
 *
 * algorithms
 * Hard (18.50%)
 * Likes:    173
 * Dislikes: 33
 * Total Accepted:    16.9K
 * Total Submissions: 76.1K
 * Testcase Example:  '[[1,2],[2,3,3],[2,3,1],[2,2,2]]'
 *
 * There exists an infinite number line, with its origin at 0 and extending
 * towards the positive x-axis.
 * 
 * You are given a 2D array queries, which contains two types of queries:
 * 
 * 
 * For a query of type 1, queries[i] = [1, x]. Build an obstacle at distance x
 * from the origin. It is guaranteed that there is no obstacle at distance x
 * when the query is asked.
 * For a query of type 2, queries[i] = [2, x, sz]. Check if it is possible to
 * place a block of size sz anywhere in the range [0, x] on the line, such that
 * the block entirely lies in the range [0, x]. A block cannot be placed if it
 * intersects with any obstacle, but it may touch it. Note that you do not
 * actually place the block. Queries are separate.
 * 
 * 
 * Return a boolean array results, where results[i] is true if you can place
 * the block specified in the i^th query of type 2, and false otherwise.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: queries = [[1,2],[2,3,3],[2,3,1],[2,2,2]]
 * 
 * Output: [false,true,true]
 * 
 * Explanation:
 * 
 * 
 * 
 * For query 0, place an obstacle at x = 2. A block of size at most 2 can be
 * placed before x = 3.
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: queries = [[1,7],[2,7,6],[1,2],[2,7,5],[2,7,6]]
 * 
 * Output: [true,true,false]
 * 
 * Explanation:
 * 
 * 
 * 
 * 
 * Place an obstacle at x = 7 for query 0. A block of size at most 7 can be
 * placed before x = 7.
 * Place an obstacle at x = 2 for query 2. Now, a block of size at most 5 can
 * be placed before x = 7, and a block of size at most 2 before x = 2.
 * 
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= queries.length <= 15 * 10^4
 * 2 <= queries[i].length <= 3
 * 1 <= queries[i][0] <= 2
 * 1 <= x, sz <= min(5 * 10^4, 3 * queries.length)
 * The input is generated such that for queries of type 1, no obstacle exists
 * at distance x when the query is asked.
 * The input is generated such that there is at least one query of type 2.
 * 
 * 
 */
package p3161
// @lc code=start
class Solution {
    class Node(val key: Int) {
        val priority = nextRand()
        var left: Node? = null
        var right: Node? = null
    }

    companion object {
        var seed = 1

        fun nextRand(): Int {
            seed = seed * 1103515245 + 12345
            return seed
        }
    }

    var root: Node? = null

    fun rotateRight(o: Node): Node {
        val p = o.left!!
        o.left = p.right
        p.right = o
        return p
    }

    fun rotateLeft(o: Node): Node {
        val p = o.right!!
        o.right = p.left
        p.left = o
        return p
    }

    fun add(o: Node?, key: Int): Node {
        if (o == null) {
            return Node(key)
        }
        if (key < o.key) {
            o.left = add(o.left, key)
            if (o.left!!.priority > o.priority) {
                return rotateRight(o)
            }
        } else if (key > o.key) {
            o.right = add(o.right, key)
            if (o.right!!.priority > o.priority) {
                return rotateLeft(o)
            }
        }
        return o
    }

    fun lower(key: Int): Int {
        var o = root
        var res = 0
        while (o != null) {
            if (o.key < key) {
                res = o.key
                o = o.right
            } else {
                o = o.left
            }
        }
        return res
    }

    fun higher(key: Int): Int {
        var o = root
        var res = Int.MAX_VALUE
        while (o != null) {
            if (o.key > key) {
                res = o.key
                o = o.left
            } else {
                o = o.right
            }
        }
        return res
    }

    fun getResults(queries: Array<IntArray>): List<Boolean> {
        val m = queries.maxOf { it[1] } + 1
        var size = 1
        while (size <= m) {
            size = size shl 1
        }
        val tree = IntArray(size shl 1)

        fun update(index: Int, value: Int) {
            var i = index + size
            tree[i] = value
            i = i shr 1
            while (i > 0) {
                tree[i] = maxOf(tree[i shl 1], tree[i shl 1 or 1])
                i = i shr 1
            }
        }

        fun query(right: Int): Int {
            var l = size
            var r = right + size
            var res = 0
            while (l <= r) {
                if (l and 1 == 1) {
                    res = maxOf(res, tree[l])
                    l++
                }
                if (r and 1 == 0) {
                    res = maxOf(res, tree[r])
                    r--
                }
                l = l shr 1
                r = r shr 1
            }
            return res
        }

        root = null
        root = add(root, 0)
        root = add(root, m)

        val ans = mutableListOf<Boolean>()
        for (q in queries) {
            val x = q[1]
            val pre = lower(x)
            if (q[0] == 1) {
                val next = higher(x)
                root = add(root, x)
                update(x, x - pre)
                update(next, next - x)
            } else {
                val maxGap = maxOf(query(pre), x - pre)
                ans.add(maxGap >= q[2])
            }
        }
        return ans
    }
}
// @lc code=end
