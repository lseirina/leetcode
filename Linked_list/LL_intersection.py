# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


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
