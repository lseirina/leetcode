# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next




















class Solution(object):
    def getDecimalValue(self, head):
        decimal_val = 0
        temp = head
        while temp:
            decimal_val = decimal_val*2 + temp.val
            temp = temp.next

        return decimal_val
