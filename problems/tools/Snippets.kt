// ===== heap (min-heap on MutableList<Int>, pure Kotlin, O(log n)) =====
fun MutableList<Int>.heappush(x: Int) {
    add(x); var i = lastIndex
    while (i > 0) { val p = (i - 1) / 2; if (this[p] <= this[i]) break; swap(i, p); i = p }
}
fun MutableList<Int>.heappop(): Int {
    val t = this[0]; this[0] = removeAt(lastIndex)
    var i = 0; while (true) {
        var s = i; val l = i * 2 + 1; val r = l + 1
        if (l < size && this[l] < this[s]) s = l
        if (r < size && this[r] < this[s]) s = r
        if (s == i) break; swap(i, s); i = s
    }
    return t
}
private fun MutableList<Int>.swap(i: Int, j: Int) { this[i] = this[j].also { this[j] = this[i] } }

// ===== bisect (pure Kotlin, O(log n)) =====
fun <T : Comparable<T>> List<T>.bisectLeft(x: T): Int {
    var (l, r) = 0 to size
    while (l < r) { val m = (l + r) ushr 1; if (this[m] < x) l = m + 1 else r = m }
    return l
}
fun <T : Comparable<T>> List<T>.bisectRight(x: T): Int {
    var (l, r) = 0 to size
    while (l < r) { val m = (l + r) ushr 1; if (this[m] <= x) l = m + 1 else r = m }
    return l
}
fun <T : Comparable<T>> MutableList<T>.insort(x: T) { add(bisectLeft(x), x) }

// ===== SortedList (pure Kotlin, index O(1) / insert O(n)) =====
class SL<E : Comparable<E>>(private val d: ArrayList<E> = ArrayList()) : List<E> by d {
    fun add(x: E) { d.add(d.binarySearch(x).let { if (it < 0) -it - 1 else it }, x) }
    fun remove(x: E): Boolean { val i = d.binarySearch(x); return if (i < 0) false else { d.removeAt(i); true } }
}
