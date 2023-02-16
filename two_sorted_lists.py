#Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = temp = ListNode()
        if not list1 or not list2:
            return list1 or list2
        while list1 != None and list2 != None:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next
            else:
                temp.next = list2
                list2 = list2.next
            temp = temp.next

        temp.next = list1 or list2
        return dummy.next
    
solution = Solution()
print(solution.mergeTwoLists([2,4,6,9],[1,3,5,7,8]))