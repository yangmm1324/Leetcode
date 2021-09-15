23. Merge k Sorted Lists
Hard

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.
Merge all the linked-lists into one sorted linked-list and return it.

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

1. 澄清:
   edges cases

2. 易错点:
   edge cases
   when lists has length 1, should return lists[0] instead
   o(1) space

3. 思路
   3.1 use divide and conquer
       each list is sorted, we can treat is as the sorted sub array


4.1.algorithm: use divide and conquer method, o(nlogk) time--n is the total nodes, k is the number of list,
               o(1) space
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:

        if not lists: return None
        if len(lists) == 1: return lists[0]
        mid = len(lists)//2

        left = self.mergeKLists(lists[:mid])
        right = self.mergeKLists(lists[mid:])
        dummy = curr = ListNode(0)

        while left and right:
            if left.val<=right.val:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next

        curr.next = left or right
        return dummy.next
