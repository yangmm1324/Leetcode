21. Merge Two Sorted Lists
Easy

Description
Merge two sorted linked lists and return it as a sorted list.
The list should be made by splicing together the nodes of the first two lists.

Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

1. 澄清:


2. 易错点:
   remember to feedback to the recursive call and make the connection
   be cautious of the return value under the condition

3. 思路
   3.1 use extra space to maintain a sorted list along the road,
       compare each element and advance with the smaller val
   3.2 compare the l1 and l2, if l1.val<=l2: then l1.next = recursive call, return l1
       else: l2.next = recursive call, return l2
       The recursive method should also be o(m+n), because of the stack call

4.1. algorithm: use iterative, extra space, o(m+n) time and space
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = current = ListNode(0)
        while l1 and l2:
            if l1.val<=l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        current.next = l1 or l2

        return dummy.next

def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2: return l1 or l2
    if l1.val <= l2.val:
        l1.next = self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next = self.mergeTwoLists(l1, l2.next)
        return l2
