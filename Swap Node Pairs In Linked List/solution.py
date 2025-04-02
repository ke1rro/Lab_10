"""
Lenyk Nikita
Solution: Swap Node Pairs In Linked List
"""


class Node:
    """
    Linked list representation.
    """

    def __init__(self, data: str | int, next: "Node" | None = None):
        self.data = data
        self.next = next



def swap_pairs(head: "Node") -> "Node":
    """
    that swaps each pair of nodes in the list,
    then returns the head node of the list.

    Args:
        head (Node): The head of the linked list
    """
    if not head or not head.next:
        return head


    new_head = head.next
    prev = None

    while head and head.next:
        first = head
        second = head.next

        first.next = second.next
        second.next = first

        if prev:
            prev.next = second

        prev = first
        head = first.next

    return new_head