"""
Lenyk Nikita
Solution: Parse a linked list from a string
"""


class Node:
    """
    Linked list representation.
    """

    def __init__(self, data: str | int, next: "Node" | None = None):
        self.data = data
        self.next = next


def linked_list_from_string(s: str) -> "Node" | None:
    """
    Parses linked list from the given string.

    Returns:
        Node: the head element of linked list.
    """
    if s.strip() in ("None", "null"):
        return None

    values = s.split(" -> ")
    values = [v for v in values if v not in ("None", "null")]

    if not values:
        return None

    head = Node(int(values[0]))
    current = head

    for value in values[1:]:
        current.next = Node(int(value))
        current = current.next

    return head
