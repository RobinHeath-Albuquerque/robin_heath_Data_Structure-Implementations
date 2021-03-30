
class BinarySearchTree:
    def __init__(self, items=None):
        self.root = None
        self.let_child = None
        self.right_child = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def insert(self, item):
        pass


def insert(self, item):
    if self.is_empty():
        self.root = BinarySearchTree(item)
        self.size += 1
        return

    parent = self._find_parent_node_recursive(item, self.root)
    if parent.data > item:
        parent.left = BinarySearchTree(item)
    elif parent.data < item:
        parent.right = BinarySearchTree(item)
    self.size += 1


def _find_node_iterative(self, item):
    node = self.root

    while node is not None:
        if item == node.data:
            return node
        elif item < node.data:
            node = node.left
        elif item > node.data:
            node = node.right
