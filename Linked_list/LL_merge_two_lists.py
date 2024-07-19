 def mergeTwoLists(self, list1, list2):
    


        if not list1 or not list2:
            return list1 or list2

        dummy = temp = ListNode()

        while list1 and list2:
            if list1.val < list2.val:
                temp.next = list1
                list1 = list1.next

            else:
                temp.next = list2
                list2 = list2.next

            temp = temp.next

        temp.next = list1 or list2


        return dummy.next
