class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



def remove_dublicates(self, head):
    temp = head
    while temp and temp.next:
        if temp.val == temp.next.val:
            temp.next = temp.next.next
        else:
            temp = temp.next

    return head
































def deleteDuplicates(head: ListNode) -> ListNode:
    curr = head

    while curr and curr.next:
        if curr.val == curr.next.val:
            curr.next = curr.next.next
        else:
            curr = curr.next

    return head
