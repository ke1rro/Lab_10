"""
Lenyk Nikita
Solution: Parse a linked list from a string
"""


class Node:
    """
    Linked list representation
    """

    def __init__(self, data: str | int, next: "Node" | None = None):
        self.data = data
        self.next = next


def push(head: "Node", data: str | int) -> "Node":
    """
    Pushes the given data as element of linked list.

    Args:
        head (Node): the head to push the element.
        data (str | int): the data to create a node.

    Returns:
        Node: The new node added to linked list
    """
    new_node = Node(data)
    new_node.next = head
    return new_node


def build_one_two_three() -> "Node":
    """
    Creates a simple chain of linked list with three elements.
    """
    head = None
    head = push(head, 3)
    head = push(head, 2)
    head = push(head, 1)
    return head
