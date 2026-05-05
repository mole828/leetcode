package problems.tools

class ListNode(var `val`: Int = 0, var next: ListNode? = null) {
    override fun toString(): String = "$`val`->$next"

    companion object {
        fun build(values: Iterable<Int>): ListNode? {
            val iterator = values.iterator()
            if (!iterator.hasNext()) return null

            val head = ListNode(iterator.next())
            var node = head
            while (iterator.hasNext()) {
                node.next = ListNode(iterator.next())
                node = node.next!!
            }
            return head
        }
    }
}
