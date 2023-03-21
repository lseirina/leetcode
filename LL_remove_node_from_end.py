class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        

class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node

        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        return True
  


def remove_kth_from_end(ll, k):
    fast = slow = ll.head
    for _ in range(k):
        fast = fast.next
        
    if fast is None:
        return ll.head.next
    while fast.next:
        slow = slow.next
        fast = fast.next
    slow.next = slow.next
    
    return ll.head

my_linked_list = LinkedList(1)
my_linked_list.append(2)
my_linked_list.append(3)
my_linked_list.append(4)
my_linked_list.append(5)


k = 2
result = remove_kth_from_end(my_linked_list, k)

print(result.value)