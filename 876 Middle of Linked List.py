876. Middle of the Linked List
Easy

Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.

Input: [1,2,3,4,5]
Output: Node 3 from this list (Serialization: [3,4,5])
The returned node has value 3.  (The judge's serialization of this node is [3,4,5]).
Note that we returned a ListNode object ans, such that:
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, and ans.next.next.next = NULL.

1. 澄清:
   in the case for even number, which index to return-- two different method

2. 易错点:


3. 思路
   3.1 fast and slow pointer,
       if asks for 1st middle in the case of even number:
                method 1: fast = slow = head
                          while fast.next and fast.next.next:
                              fast = fast.next.next
                              slow = slow.next
                method 2: fast = head.next
                          slow = head
                          while fast and fast.next:
                              fast = fast.next.next
                              slow = slow.next
      elif asks for the 2nd middle node in case of even number:
                fast = slow = head
                while fast and fast.next:
                    fast = fast.next.next
                    slow = slow.next
      difference is the initialization of fast to head.next or while condition need to fast.next and fast.next.next


4.1.algorithm: o(n) time | o(1) space
# right middle
def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
# left middle
def middleNode(self, head: ListNode) -> ListNode:
    slow = fast = head
    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    return slow

def middleNode(self, head: ListNode) -> ListNode:
    slow = head
    fast = head.next
    while fast and fast.next:
        fast = fast.next.next 
        slow = slow.next

    return slow
