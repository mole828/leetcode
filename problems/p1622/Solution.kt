package problems.p1622
/*
 * @lc app=leetcode id=1622 lang=kotlin
 *
 * [1622] Fancy Sequence
 */

// @lc code=start
class Fancy() {
    private val vals = mutableListOf<Long>()
    private var add = 0L
    private var mul = 1L
    private val mod = 1000000007L

    fun append(value: Int) {
        // 计算逆元并存储转换后的值
        val invMul = powMod(mul, mod - 2)
        val transformedValue = ((value - add % mod + mod) % mod * invMul % mod)
        vals.add(transformedValue)
    }

    fun addAll(inc: Int) {
        add = (add + inc) % mod
    }

    fun multAll(m: Int) {
        mul = mul * m % mod
        add = add * m % mod
    }

    fun getIndex(idx: Int): Int {
        if (idx >= vals.size) return -1
        return ((vals[idx] * mul % mod + add) % mod).toInt()
    }

    // 快速幂取模计算
    private fun powMod(base: Long, exp: Long): Long {
        var result = 1L
        var b = base % mod
        var e = exp
        while (e > 0) {
            if (e % 2 == 1L) {
                result = result * b % mod
            }
            b = b * b % mod
            e /= 2
        }
        return result
    }
}
// @lc code=end
