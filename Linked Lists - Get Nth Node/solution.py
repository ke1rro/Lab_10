"""
Lenyk Nikita
Solution: Linked Lists - Get Nth Node

"""


class Node:
    """
    Linked list representation
    """

    def __init__(self, data: str | int, next: "Node" | None = None):
        self.data = data
        self.next = next


def get_nth(node: "Node", index: int) -> "Node":
    """
    Gets the nth element from the linked list.

    Args:
        node (Node): the head node.
        index (int): the index to find the element.

    Raises:
        IndexError: If the index is out of bounds

    Returns:
        Node: Node if found otherwise IndexError
    """
    i = 0
    current = node
    while current:
        if i == index:
            return current
        i += 1
        current = current.next

    raise IndexError
