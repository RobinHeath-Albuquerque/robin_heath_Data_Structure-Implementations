from node import Node


class LinkedList:
    def __init__(self):
        self.head = None

    def append_node(self, data):
        node = Node
        self.head = node

        if self.head is None:
            self.head = node

            temporary_node = self.head

            while temporary_node.next is not None:
                temporary_node = temporary_node.next

            temporary_node.next = node
            return

    def prepend_node(self, data):
        node = Node

        if self.head is None:
            return
        else:
            node.next = self.head
            self.head = node
