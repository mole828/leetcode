class Solution {
    fun minChanges(s: String): Int = run {
        (0..(s.length/2-1)).sumOf { i ->
            val a = s[i*2]
            val b = s[i*2+1]
            (if (a == b) 0 else 1).toInt()
        }
    }
}

println(Solution().minChanges("1010"))