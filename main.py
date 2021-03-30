from linkedlist import LinkedList


if __name__ == '__main__':
    linked_list = LinkedList()

    linked_list.append_node(55)
    linked_list.append_node(60)
    linked_list.append_node(65)
    linked_list.prepend_node(45)


from searchtree import BinarySearchTree
if __name__ == '__main__':
    binary_search_tree = BinarySearchTree()

    items = [50, 99, 37, 41, 12, 22]
    for item in items:
        binary_search_tree.insert(item)

from birthday import my_past_trips
from family import my_family
from months import months
from sweepstakes import contestants
