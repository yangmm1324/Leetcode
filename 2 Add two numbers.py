2. Add Two Numbers
Medium

Description
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order, and each of their nodes contains a single digit.
Add the two numbers and return the sum as a linked list.
You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example 1:
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.

1. 澄清:


2. 易错点:


3. 思路
   if any of the two lists still have nodes left or still have carry over,
          calculate the current value mod 10 and recalculate the carry over
          create the node and set the result pointer list next to current node value
          move the list and the result pointer to the next



4.1. algorithm: iterative method, o(max(m,n)) time and o(max(m, n)) space
def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        carry = 0
        dummy = ListNode(0)
        root = dummy
        
        while l1 or l2 or carry:

            cur = carry

            if l1:
                cur += l1.val
                l1 = l1.next
            if l2:
                cur += l2.val
                l2 = l2.next

            carry = cur // 10
            cur = cur % 10
            cur = ListNode(cur)

            root.next = cur
            root = root.next

        return dummy.next
