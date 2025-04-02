"""
Lenyk Nikita
Solution: Linked Lists - Recursive Reverse
"""


class Node:
    """
    Linked list representation
    """

    def __init__(self, data: str | int, next: "Node" | None = None):
        self.data = data
        self.next = next


def reverse(head: "Node") -> "Node":
    """
    Recursively reverses the list

    Args:
        head (Node): The head of the current list

    Returns:
        Node: The head node
    """
    if head is None or head.next is None:
        return head

    def reverse_recursive(curr, prev=None):
        if curr is None:
            return prev
        next_node = curr.next
        curr.next = prev
        return reverse_recursive(next_node, curr)

    return reverse_recursive(head)
