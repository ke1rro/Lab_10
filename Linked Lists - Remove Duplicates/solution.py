"""
Lenyk Nikita
Solution: Linked Lists - Remove Duplicates
"""


class Node:
    """
    Linked list representation.
    """

    def __init__(self, data: str | int, next: "Node" | None = None):
        self.data = data
        self.next = next


def remove_duplicates(head: "Node") -> "Node":
    """
    Removes the duplicates from the given linked list

    Args:
        head (Node): The head of the list

    Returns:
        Node: The current node of the list
    """
    traversed = set()
    curr = head
    prev = None
    while curr:
        if curr.data in traversed:
            prev.next = curr.next
        else:
            traversed.add(curr.data)
            prev = curr
        curr = curr.next

    return head
