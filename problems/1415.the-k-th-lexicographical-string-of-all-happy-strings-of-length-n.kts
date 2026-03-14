/*
 * @lc app=leetcode id=1415 lang=kotlin
 *
 * [1415] The k-th Lexicographical String of All Happy Strings of Length n
 */

// @lc code=start
class Solution {
    fun getHappyString(n: Int, k: Int): String {
        val charSet = ('a'..'c').toList()
        val allStr = mutableListOf<String>()
        fun dfs(str: String) {
            if (str.length == n) {
                allStr.add(str)
                return
            }
            for (c in charSet) {
                if (str.isNotEmpty() && c == str.last()) continue
                dfs(str+c)
            }
        }
        dfs("")
        return allStr.getOrElse(k-1) { "" }
    }
}
// @lc code=end

println(Solution().getHappyString(10, 100))