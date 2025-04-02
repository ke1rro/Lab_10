"""
Lenyk Nikita
Solution: Linked Lists - Alternating Split
"""


class Node:
    """
    Linked list representation.
    """

    def __init__(self, data: str | int, next: "Node" | None = None):
        self.data = data
        self.next = next


class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second


def alternating_split(head: "Node") -> "Context":
    if not head or not head.next:
        raise ValueError

    first = head
    second = head.next

    first_current = first
    second_current = second

    current = head.next.next
    toggle = True

    while current:
        if toggle:
            first_current.next = current
            first_current = first_current.next
        else:
            second_current.next = current
            second_current = second_current.next
        toggle = not toggle
        current = current.next

    first_current.next = None
    second_current.next = None

    return Context(first, second)
