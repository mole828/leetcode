package p1096
/*
 * @lc app=leetcode id=1096 lang=kotlin
 *
 * [1096] Brace Expansion II
 */
// @lc code=start
class Solution {
    sealed interface Node {
        val parent: Node?

        class CharNode(
            override val parent: NodeList.Concat,
            val char: Char
        ) : Node

        @Suppress("JavaDefaultMethodsNotOverriddenByDelegation")
        sealed interface NodeList : Node, MutableList<Node> {
            override val parent: NodeList?

            class Union(
                override val parent: Concat? = null
            ) : NodeList, MutableList<Node> by mutableListOf()

            class Concat(
                override val parent: Union
            ) : NodeList, MutableList<Node> by mutableListOf()
        }
    }

    fun braceExpansionII(expression: String): List<String> {
        val root = Node.NodeList.Union()
        var node = Node.NodeList.Concat(root)
        root.add(node)

        for (char in expression) {
            when (char) {
                '{' -> {
                    val union = Node.NodeList.Union(node)
                    node.add(union)
                    node = Node.NodeList.Concat(union)
                    union.add(node)
                }
                '}' -> {
                    node = requireNotNull(node.parent.parent)
                }
                ',' -> {
                    val union = node.parent
                    node = Node.NodeList.Concat(union)
                    union.add(node)
                }
                else -> node.add(Node.CharNode(node, char))
            }
        }

        fun dfs(node: Node): Set<String> = when (node) {
            is Node.CharNode -> setOf(node.char.toString())
            is Node.NodeList.Union -> {
                val result = mutableSetOf<String>()
                for (child in node) {
                    result.addAll(dfs(child))
                }
                result
            }
            is Node.NodeList.Concat -> {
                var result = setOf("")
                for (child in node) {
                    val suffixes = dfs(child)
                    val next = mutableSetOf<String>()
                    for (prefix in result) {
                        for (suffix in suffixes) {
                            next.add(prefix + suffix)
                        }
                    }
                    result = next
                }
                result
            }
        }

        return dfs(root).sorted()
    }
}
// @lc code=end
