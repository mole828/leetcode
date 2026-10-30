package p3841

/*
 * @lc app=leetcode id=3841 lang=kotlin
 *
 * [3841] Palindromic Path Queries in a Tree
 *
 * https://leetcode.com/problems/palindromic-path-queries-in-a-tree/description/
 *
 * algorithms
 * Hard (36.81%)
 * Likes:    70
 * Dislikes: 5
 * Total Accepted:    6.8K
 * Total Submissions: 15.4K
 * Testcase Example:  '3\n[[0,1],[1,2]]\n"aac"\n["query 0 2","update 1 b","query 0 2"]'
 *
 * You are given an undirected tree with n nodes labeled 0 to n - 1. This is
 * represented by a 2D array edges of length n - 1, where edges[i] = [ui, vi]
 * indicates an undirected edge between nodes ui and vi.
 * 
 * You are also given a string s of length n consisting of lowercase English
 * letters, where s[i] represents the character assigned to node i.
 * 
 * You are also given a string array queries, where each queries[i] is
 * either:
 * 
 * 
 * "update ui c": Change the character at node ui to c. Formally, update s[ui]
 * = c.
 * "query ui vi": Determine whether the string formed by the characters on the
 * unique path from ui to vi (inclusive) can be rearranged into a palindrome.
 * 
 * 
 * Return a boolean array answer, where answer[j] is true if the j^th query of
 * type "query ui vi"​​​​​​​ can be rearranged into a palindrome, and false
 * otherwise.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: n = 3, edges = [[0,1],[1,2]], s = "aac", queries = ["query 0
 * 2","update 1 b","query 0 2"]
 * 
 * Output: [true,false]
 * 
 * Explanation:
 * 
 * 
 * "query 0 2": Path 0 → 1 → 2 gives "aac", which can be rearranged to form
 * "aca", a palindrome. Thus, answer[0] = true.
 * "update 1 b": Update node 1 to 'b', now s = "abc".
 * "query 0 2": Path characters are "abc", which cannot be rearranged to form a
 * palindrome. Thus, answer[1] = false.
 * 
 * 
 * Thus, answer = [true, false].
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: n = 4, edges = [[0,1],[0,2],[0,3]], s = "abca", queries = ["query 1
 * 2","update 0 b","query 2 3","update 3 a","query 1 3"]
 * 
 * Output: [false,false,true]
 * 
 * Explanation:
 * 
 * 
 * "query 1 2": Path 1 → 0 → 2 gives "bac", which cannot be rearranged to form
 * a palindrome. Thus, answer[0] = false.
 * "update 0 b": Update node 0 to 'b', now s = "bbca".
 * "query 2 3": Path 2 → 0 → 3 gives "cba", which cannot be rearranged to form
 * a palindrome. Thus, answer[1] = false.
 * "update 3 a": Update node 3 to 'a', s = "bbca".
 * "query 1 3": Path 1 → 0 → 3 gives "bba", which can be rearranged to form
 * "bab", a palindrome. Thus, answer[2] = true.
 * 
 * 
 * Thus, answer = [false, false, true].
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= n == s.length <= 5 * 10^4
 * edges.length == n - 1
 * edges[i] = [ui, vi]
 * 0 <= ui, vi <= n - 1
 * s consists of lowercase English letters.
 * The input is generated such that edges represents a valid tree.
 * 1 <= queries.length <= 5 * 10^4​​​​​​​
 * 
 * queries[i] = "update ui c" or
 * queries[i] = "query ui vi"
 * 0 <= ui, vi <= n - 1
 * c is a lowercase English letter.
 * 
 * 
 * 
 * 
 */

// @lc code=start
class Solution {
    fun palindromePath(n: Int, edges: Array<IntArray>, s: String, queries: Array<String>): List<Boolean> {
        val neighbors = Array(n) { mutableListOf<Int>() }
        for ((a, b) in edges) {
            neighbors[a].add(b)
            neighbors[b].add(a)
        }
        val chars = s.toCharArray()
        fun letterMask(c: Char): Int = 1 shl (c - 'a')

        val parent = IntArray(n)
        val depth = IntArray(n)
        val initialRootPathMask = IntArray(n)
        val entry = IntArray(n)
        val subtreeSize = IntArray(n) { 1 }
        val dfsOrder = mutableListOf<Int>()

        // 按 DFS 顺序编号，同一子树的编号连续。使用显式栈避免深链栈溢出。
        val stack = java.util.ArrayDeque<Int>()
        initialRootPathMask[0] = letterMask(chars[0])
        stack.addLast(0)
        while (stack.isNotEmpty()) {
            val node = stack.removeLast()
            entry[node] = dfsOrder.size
            dfsOrder.add(node)
            for (next in neighbors[node]) {
                if (next == parent[node]) continue
                parent[next] = node
                depth[next] = depth[node] + 1
                initialRootPathMask[next] = initialRootPathMask[node] xor letterMask(chars[next])
                stack.addLast(next)
            }
        }
        for (i in dfsOrder.lastIndex downTo 1) {
            val node = dfsOrder[i]
            subtreeSize[parent[node]] += subtreeSize[node]
        }

        // ancestors[k][node] 表示向上走 2^k 步到达的祖先。
        var levels = 1
        while ((1 shl levels) <= n) levels++
        val ancestors = Array(levels) { IntArray(n) }
        parent.copyInto(ancestors[0])
        for (k in 1 until levels) {
            for (node in 0 until n) {
                val halfway = ancestors[k - 1][node]
                ancestors[k][node] = ancestors[k - 1][halfway]
            }
        }

        fun lowestCommonAncestor(a: Int, b: Int): Int {
            var u = a
            var v = b
            if (depth[u] < depth[v]) {
                val temp = u
                u = v
                v = temp
            }
            val difference = depth[u] - depth[v]
            for (k in 0 until levels) {
                if ((difference and (1 shl k)) != 0) u = ancestors[k][u]
            }
            if (u == v) return u
            // 保持两者不同，尽量向上跳；最后它们的父节点就是公共祖先。
            for (k in levels - 1 downTo 0) {
                if (ancestors[k][u] != ancestors[k][v]) {
                    u = ancestors[k][u]
                    v = ancestors[k][v]
                }
            }
            return parent[u]
        }

        val changes = SubtreeChanges(n)
        fun rootPathMask(node: Int): Int = initialRootPathMask[node] xor changes.at(entry[node])

        fun update(node: Int, newChar: Char) {
            val change = letterMask(chars[node]) xor letterMask(newChar)
            val start = entry[node]
            changes.xorRange(start, start + subtreeSize[node], change)
            chars[node] = newChar
        }

        val answer = mutableListOf<Boolean>()
        for (query in queries) {
            val (type, a, b) = query.split(' ')
            val node = a.toInt()
            when (type) {
                "update" -> update(node, b.first())
                "query" -> {
                    val other = b.toInt()
                    val ancestor = lowestCommonAncestor(node, other)
                    val pathMask = rootPathMask(node) xor rootPathMask(other) xor
                        letterMask(chars[ancestor])
                    answer.add(Integer.bitCount(pathMask) <= 1)
                }
                else -> error("Unknown query: $type")
            }
        }
        return answer
    }

    // 异或差分 + 树状数组：区间更新、单点查询，均为 O(log n)。
    private class SubtreeChanges(n: Int) {
        private val tree = IntArray(n + 1)

        // 更新区间 [start, endExclusive)。
        fun xorRange(start: Int, endExclusive: Int, mask: Int) {
            xorDifference(start, mask)
            xorDifference(endExclusive, mask)
        }

        private fun xorDifference(index: Int, mask: Int) {
            var i = index + 1
            while (i < tree.size) {
                tree[i] = tree[i] xor mask
                i += i and -i
            }
        }

        fun at(index: Int): Int {
            var i = index + 1
            var mask = 0
            while (i > 0) {
                mask = mask xor tree[i]
                i -= i and -i
            }
            return mask
        }
    }

    @Deprecated("time limit")
    fun palindromePathReadable(n: Int, edges: Array<IntArray>, s: String, queries: Array<String>): List<Boolean> {
        val neighbors = Array(n) { mutableListOf<Int>() }
        for ((a, b) in edges) {
            neighbors[a].add(b)
            neighbors[b].add(a)
        }
        val chars = s.toCharArray()

        fun letterMask(c: Char): Int = 1 shl (c - 'a')

        val parent = IntArray(n) { -1 }
        val depth = IntArray(n)
        val children = Array(n) { mutableListOf<Int>() }
        val rootPathMask = IntArray(n)

        val queue = java.util.ArrayDeque<Int>()
        rootPathMask[0] = letterMask(chars[0])
        queue.addLast(0)
        while (queue.isNotEmpty()) {
            val node = queue.removeFirst()
            for (next in neighbors[node]) {
                if (next == parent[node]) continue
                parent[next] = node
                depth[next] = depth[node] + 1
                children[node].add(next)
                rootPathMask[next] = rootPathMask[node] xor letterMask(chars[next])
                queue.addLast(next)
            }
        }

        fun update(node: Int, newChar: Char) {
            val change = letterMask(chars[node]) xor letterMask(newChar)
            chars[node] = newChar

            queue.addLast(node)
            while (queue.isNotEmpty()) {
                val current = queue.removeFirst()
                rootPathMask[current] = rootPathMask[current] xor change
                for (child in children[current]) queue.addLast(child)
            }
        }

        fun lowestCommonAncestor(a: Int, b: Int): Int {
            var u = a
            var v = b
            while (depth[u] > depth[v]) u = parent[u]
            while (depth[v] > depth[u]) v = parent[v]
            while (u != v) {
                u = parent[u]
                v = parent[v]
            }
            return u
        }

        val answer = mutableListOf<Boolean>()
        for (query in queries) {
            val (type, a, b) = query.split(' ')
            val node = a.toInt()
            when (type) {
                "update" -> update(node, b.first())
                "query" -> {
                    val other = b.toInt()
                    val ancestor = lowestCommonAncestor(node, other)
                    val pathMask = rootPathMask[node] xor rootPathMask[other] xor
                        letterMask(chars[ancestor])
                    val oddLetterCount = Integer.bitCount(pathMask)
                    answer.add(oddLetterCount <= 1)
                }
                else -> error("Unknown query: $type")
            }
        }
        return answer
    }

    private class State(val node: Int, val visited: BooleanArray)
    @Deprecated("memory limit")
    fun palindromePathReference(n: Int, edges: Array<IntArray>, s: String, queries: Array<String>): List<Boolean> {
        val mat = mutableMapOf<Int, MutableSet<Int>>()
        edges.forEach { arr -> 
            val (a,b) = arr
            mat.getOrPut(a) { mutableSetOf() }.add(b)
            mat.getOrPut(b) { mutableSetOf() }.add(a)
        }
        val charList = s.toMutableList()
        fun query(a: Int, b: Int): Boolean {
            val que = mutableListOf<State>(State(a, BooleanArray(n)))
            while (que.isNotEmpty()) {
                val state = que.removeFirst()
                val newVisited = state.visited.copyOf()
                newVisited[state.node] = true
                if (state.node == b) {
                    val count = IntArray(26)
                    newVisited.forEachIndexed { i,v ->
                        if (v) {
                            val char = charList[i]
                            val charNum = char - 'a'
                            count[charNum] += 1
                        }
                    }
                    return count.count { it%2 == 1 } <= 1
                }
                if (state.visited[state.node]) continue
                mat[state.node]!!.forEach { newNode ->
                    que.add(State(newNode, newVisited))
                }
            }
            error("?")
        }
        return queries.mapNotNull { querie ->
            val (q, u, v) = querie.split(' ')
            when (q) {
                "query" -> {
                    val u = u.toInt()
                    val v = v.toInt()
                    query(u,v)
                }
                "update" -> {
                    val u = u.toInt()
                    val c = v.first()
                    charList[u] = c
                    null
                }
                else -> error("?")
            }
        } 
    }
}
// @lc code=end

