package p3525

/*
 * @lc app=leetcode id=3525 lang=kotlin
 *
 * [3525] Find X Value of Array II
 */

// TODO: 线段树 + 前缀计数

// @lc code=start
class Solution {
    fun resultArray(nums: IntArray, k: Int, queries: Array<IntArray>): IntArray {
        val tree = SegmentTree(nums, k)
        return IntArray(queries.size) { queryIndex ->
            val (index, value, start, target) = queries[queryIndex]
            tree.update(index, value)
            tree.querySuffix(start).prefixCounts[target]
        }
    }

    private class Node(val prefixCounts: IntArray, val product: Int)

    private class SegmentTree(nums: IntArray, private val k: Int) {
        private val leafCount = generateSequence(1) { it * 2 }.first { it >= nums.size }
        // 空节点没有非空前缀，乘积为乘法单位元。
        private val tree = Array(leafCount * 2) { Node(IntArray(k), 1 % k) }

        init {
            nums.forEachIndexed { index, value -> tree[leafCount + index] = leaf(value) }
            for (node in leafCount - 1 downTo 1) maintain(node)
        }

        private fun leaf(value: Int) = Node(
            IntArray(k).apply { this[value % k] = 1 }, value % k
        )

        private fun merge(left: Node, right: Node): Node {
            val counts = left.prefixCounts.copyOf()
            for (remainder in 0 until k) {
                counts[left.product * remainder % k] += right.prefixCounts[remainder]
            }
            return Node(counts, left.product * right.product % k)
        }

        private fun maintain(node: Int) {
            tree[node] = merge(tree[node * 2], tree[node * 2 + 1])
        }

        fun update(index: Int, value: Int) {
            var node = leafCount + index
            tree[node] = leaf(value)
            node /= 2
            while (node > 0) {
                maintain(node)
                node /= 2
            }
        }

        fun querySuffix(start: Int): Node {
            var node = leafCount + start
            var result = tree[node]
            while (node > 1) {
                // 当前节点是左孩子时，右兄弟紧接在已收集的后缀之后。
                if (node % 2 == 0) result = merge(result, tree[node + 1])
                node /= 2
            }
            return result
        }
    }
}
// @lc code=end
