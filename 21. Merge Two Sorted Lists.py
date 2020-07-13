#https://leetcode.com/problems/merge-two-sorted-lists/

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        if l1.val <= l2.val:
            beg, end = l1, l1
            l1 = l1.next 
            end.next = None
        else:
            beg, end = l2, l2
            l2 = l2.next
            end.next = None
        while l1 is not None and l2 is not None :
            if l2.val <= l1.val:
                end.next = l2
                end = l2
                l2 = l2.next
                end.next = None
            else:
                end.next = l1
                end = l1
                l1 = l1.next
                end.next = None
        if l1:
            end.next = l1
        if l2:
            end.next = l2
        return beg
        
