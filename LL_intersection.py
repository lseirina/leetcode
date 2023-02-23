# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        tempA = headA
        tempB = headB
        while tempA != tempB:
            if tempA == None:
                tempA = headB
            else:
                tempA = tempA.next
            
            if tempB == None:
                tempB = headA
            else:
                tempB = tempB.next
        return tempA
        