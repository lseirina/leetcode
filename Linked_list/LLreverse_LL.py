
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node


    # def reverse(self):
    #     before = None
    #     while self.head:
    #         temp = self.head
    #         self.head = self.head.next
    #         temp.next = before
    #         before = temp
    def reverse1(self):
        temp = self.head
        self.head = self.tail
        self.tail = temp
        before = None
        after = temp.next
        for _ in range(self.length):
            after = temp.next
            temp.next = before
            before = temp
            temp = after

linkedlist = LinkedList(11)
linkedlist.append(7)
linkedlist.append(23)
linkedlist.append(4)
linkedlist.reverse()
linkedlist.print_list()





