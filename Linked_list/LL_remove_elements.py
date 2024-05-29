 Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy_head = ListNode()
        dummy_head.next = head
        temp = dummy_head

        while temp.next:
            if temp.next.val == val:
                temp.next = temp.next.next if temp.next.next else None
            else:
                temp = temp.next

        return dummy_head.next