/**
 * https://leetcode.cn/problems/add-two-numbers/
 */

/**
 * Example:
 * var li = ListNode(5)
 * var v = li.`val`
 * Definition for singly-linked list.
 * class ListNode(var `val`: Int) {
 *     var next: ListNode? = null
 * }
 */
class ListNode(var `val`: Int) {
   var next: ListNode? = null
}

class Solution {
    fun addTwoNumbers(l1: ListNode?, l2: ListNode?): ListNode? {
      var l1_pointer = l1
      var l2_pointer = l2

      var outList = ListNode(0)
      var pointer: ListNode? = outList
      var carry = 0
      
      while(l1_pointer != null || l2_pointer != null) {
        var val1 = l1_pointer?.`val` ?: 0
        var val2 = l2_pointer?.`val` ?: 0
        var calcVal = val1 + val2 + carry
        pointer?.next = ListNode(calcVal % 10)
        pointer = pointer.next
        carry = calcVal / 10
          
        println(calcVal)
        println(carry)
        
        l1_pointer = l1_pointer?.next
        l2_pointer = l2_pointer?.next
      }
      
      if (carry > 0) pointer?.next = ListNode(1)
      
      return outList.next
    }
}


fun main() {
    val l1 = ListNode(2)
    l1.next = ListNode(4)
    l1.next!!.next = ListNode(3)
    
    val l2 = ListNode(5)
    l2.next = ListNode(6)
    l2.next!!.next = ListNode(4)
    
    
    val solution = Solution()
    val result = solution.addTwoNumbers(l1, l2)
    println(result?.`val`)        // ...and use it!
    println(result?.next?.`val`)
    println(result?.next?.next?.`val`)
}