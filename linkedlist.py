from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        node = Node(data)

        def insert(self, data):
            new_node = Node(data)
            new_node.set_next(self.head)
            self.head = new_node

        if self.head is None:
            self.head = node
            return

        temporary_node = self.head

        while temporary_node.next is not None:
            temporary_node = temporary_node.next

        temporary_node.next = node



