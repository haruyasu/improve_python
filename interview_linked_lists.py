# Singly Linked List
class LinkedListNone(object):
    def __init__(self, value):
        self.value = value
        self.nextnode = None

a = LinkedListNone(1)
b = LinkedListNone(2)
c = LinkedListNone(3)
a.nextnode = b
b.nextnode = c

# Doubly Linked List
class DoublyLinkedListNonde(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None
        self.prev_node = None

a = DoublyLinkedListNonde(1)
b = DoublyLinkedListNonde(2)
c = DoublyLinkedListNonde(3)
a.next_node = b
b.prev_node = a
b.next_node = c
c.prev_node = b


