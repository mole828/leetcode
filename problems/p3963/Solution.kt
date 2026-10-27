package p3963

/*
 * @lc app=leetcode id=3963 lang=kotlin
 *
 * [3963] Create Grid With Exactly One Path
 *
 * https://leetcode.com/problems/create-grid-with-exactly-one-path/description/
 *
 * algorithms
 * Easy (76.27%)
 * Likes:    43
 * Dislikes: 6
 * Total Accepted:    47.7K
 * Total Submissions: 61.3K
 * Testcase Example:  '2\n3'
 *
 * You are given two integers m and n, representing the number of rows and
 * columns of a grid.
 * 
 * Construct any m x n grid consisting only of the characters '.' and '#',
 * where:
 * 
 * 
 * '.' represents a free cell.
 * '#' represents an obstacle cell.
 * 
 * 
 * A valid path is a sequence of free cells that:
 * 
 * 
 * Starts at the top-left cell (0, 0).
 * Ends at the bottom-right cell (m - 1, n - 1).
 * Moves only:
 * 
 * Right, from (i, j) to (i, j + 1), or
 * Down, from (i, j) to (i + 1, j).
 * 
 * 
 * 
 * 
 * Return any grid such that there is exactly one valid path from the top-left
 * cell to the bottom-right cell.
 * 
 * 
 * Example 1:
 * 
 * 
 * Input: m = 2, n = 3
 * 
 * Output: ["..#","#.."]
 * 
 * Explanation:
 * 
 * 
 * 
 * The only valid path is: (0,0) → (0,1) → (1,1) → (1,2)
 * 
 * 
 * Example 2:
 * 
 * 
 * Input: m = 3, n = 3
 * 
 * Output: ["..#","#..","##."]
 * 
 * Explanation:
 * 
 * 
 * 
 * The only valid path is: (0,0) → (0,1) → (1,1) → (1,2) → (2,2)
 * 
 * 
 * Example 3:
 * 
 * 
 * Input: m = 1, n = 4
 * 
 * Output: ["...."]
 * 
 * Explanation:
 * 
 * The only valid path is: (0,0) → (0,1) → (0,2) → (0,3)
 * 
 * 
 * 
 * Constraints:
 * 
 * 
 * 1 <= m, n <= 25
 * 
 * 
 */

// @lc code=start
class Solution {
    fun createGrid(m: Int, n: Int): Array<String> {
        val firstRow = ".".repeat(n)
        if (m == 1) return arrayOf(firstRow)

        // String 不可变，后续各行可以安全地共享同一个字符串。
        val otherRow = "#".repeat(n - 1) + "."
        return Array(m) { if (it == 0) firstRow else otherRow }
    }

    @Deprecated(
        message = "保留原实现用于参考和行为对照；重复构造相同行，增加时间和内存分配，请使用 createGrid。",
        replaceWith = ReplaceWith("createGrid(m, n)")
    )
    fun createGridReference(m: Int, n: Int): Array<String> {
        return Array<String>(m) { "" }.apply {
            this.indices.forEach { i ->
                if (i == 0) this[i] = ".".repeat(n)
                else this[i] = "#".repeat(n - 1) + "."
            }
        }
    }
}
// @lc code=end

