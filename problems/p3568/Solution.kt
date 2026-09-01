package p3568

/*
 * @lc app=leetcode id=3568 lang=kotlin
 *
 * [3568] Minimum Moves to Clean the Classroom
 */

// @lc code=start
class Solution {
    data class State(
        val position: Int,
        val energy: Int,
        val litterMask: Int
    )

    fun minMoves(classroom: Array<String>, energy: Int): Int {
        val rowCount = classroom.size
        val columnCount = classroom[0].length

        val litterIndexes = Array(rowCount) { IntArray(columnCount) { -1 } }

        var startPosition = 0
        var litterCount = 0

        classroom.forEachIndexed { row, line ->
            line.forEachIndexed { column, cell ->
                when (cell) {
                    'S' -> startPosition = row * columnCount + column
                    'L' -> litterIndexes[row][column] = litterCount++
                }
            }
        }

        if (litterCount == 0) return 0

        val targetLitterMask = (1 shl litterCount) - 1
        val maximumEnergy = Array(rowCount * columnCount) {
            IntArray(1 shl litterCount) { -1 }
        }

        val queue = ArrayDeque<State>().apply {
            add(State(startPosition, energy, 0))
        }

        maximumEnergy[startPosition][0] = energy

        val directions = arrayOf(
            -1 to 0,
            1 to 0,
            0 to -1,
            0 to 1
        )

        var moves = 0

        while (queue.isNotEmpty()) {
            repeat(queue.size) {
                val (position, currentEnergy, litterMask) = queue.removeFirst()

                if (litterMask == targetLitterMask) return moves
                if (currentEnergy == 0) return@repeat

                val row = position / columnCount
                val column = position % columnCount

                for ((rowOffset, columnOffset) in directions) {
                    val nextRow = row + rowOffset
                    val nextColumn = column + columnOffset

                    if (
                        nextRow !in classroom.indices ||
                        nextColumn !in classroom[0].indices ||
                        classroom[nextRow][nextColumn] == 'X'
                    ) continue

                    val cell = classroom[nextRow][nextColumn]
                    val nextPosition = nextRow * columnCount + nextColumn

                    val nextEnergy =
                        if (cell == 'R') energy else currentEnergy - 1

                    val nextLitterMask =
                        if (cell == 'L')
                            litterMask or (1 shl litterIndexes[nextRow][nextColumn])
                        else
                            litterMask

                    if (nextLitterMask == targetLitterMask)
                        return moves + 1

                    if (maximumEnergy[nextPosition][nextLitterMask] >= nextEnergy)
                        continue

                    maximumEnergy[nextPosition][nextLitterMask] = nextEnergy
                    queue += State(nextPosition, nextEnergy, nextLitterMask)
                }
            }

            moves++
        }

        return -1
    }
}
// @lc code=end

