#https://leetcode.com/problems/reverse-linked-list/
#O(n)

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        preptr = None
        ptr = head
        while ptr:
            next = ptr.next
            ptr.next = preptr
            preptr = ptr
            ptr = next
        return preptr
