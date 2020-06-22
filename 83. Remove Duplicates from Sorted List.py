#https://leetcode.com/problems/remove-duplicates-from-sorted-list/
#O(n)

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        preptr, ptr = head, head
        while ptr.next:
            ptr = ptr.next
            if preptr.val != ptr.val:
                preptr.next = ptr
                preptr = ptr
        preptr.next = None
        return head
