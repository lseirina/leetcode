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
            if not tempA:
                tempA = headB
            else:
                tempA = tempA.next

            if not tempB:
                tempB = headA
            else:
                tempB = tempB.next 
                
        return tempA



























        tempA = headA
        tempB = headB
        while tempA != tempB:
            if tempA is None:
                tempA = headB
            else:
                tempA = tempA.next

            if tempB is None:
                tempB = headA
            else:
                tempB = tempB.next
        return tempA
