21. Merge Two Sorted Lists
Easy

Merge two sorted linked lists and return it as a sorted list. The list should be made by splicing together the nodes of the first two lists.
Example 1:
Input: l1 = [1,2,4], l2 = [1,3,4]
Output: [1,1,2,3,4,4]

1. 澄清:
   题目说两个list是sorted order，需要澄清一下是descending还是ascending order

2. 易错点：
   1. recursion 的方法，一定要建立connection，以及不同条件的返回值
   2. 空间复杂度，recursion的方法空间复杂度为o（n+m），因为call stack不断的需要存储直到底层返回

3. 思路
   如果有一个list是空的，返回另一个，否则判断当前两个值的大小，如果l1.val<=l2.val: l1.next = .... return l1; else: l2.next = ... return l2

3. algorithm:
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
    if not l1 or not l2: return l1 or l2
    if l1.val<=l2.val:
        l1.next=self.mergeTwoLists(l1.next, l2)
        return l1
    else:
        l2.next=self.mergeTwoLists(l1, l2.next)
        return l2


## iterative method
def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = cur = ListNode(0)
        while l1 and l2:
            if l1.val>l2.val:
                cur.next = l2
                l2 = l2.next
            else:
                cur.next = l1
                l1 = l1.next
            cur = cur.next
        cur.next = l1 or l2
        return dummy.next
