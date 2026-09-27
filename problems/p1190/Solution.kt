package p1190
/*
 * @lc app=leetcode id=1190 lang=kotlin
 *
 * [1190] Reverse Substrings Between Each Pair of Parentheses
 */
// @lc code=start
class Solution {
    fun reverseParentheses(s: String): String {
        val stack = mutableListOf<Char>()
        s.forEach { char ->
            when(char) {
                ')' -> {
                    val buf = mutableListOf<Char>()
                    while (stack.isNotEmpty()) {
                        when(val pop = stack.removeLast()) {
                            '(' -> break
                            else -> buf.add(pop)
                        }
                    }
                    stack.addAll(buf)
                }
                else -> stack.add(char)
            }
        }
        return stack.joinToString("")
    }
}
// @lc code=end

