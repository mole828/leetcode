class Solution {
    fun compressedString(word: String): String {
        var count = 0
        var last = word.first()
        var ans = ""
        for (char in word) {
            if(count == 9) {
                ans += "$count$last"
                count = 0
            }
            if(last != char) {
                if (count>0) {
                    ans += "$count$last"
                }
                count = 0
                last = char
            }
            count += 1
        }
        ans += "$count$last"
        return ans
    }
}

println(Solution().compressedString("aaaabbb"))
println(Solution().compressedString("aaaaaaaaaaaaaabb"))
println("done")