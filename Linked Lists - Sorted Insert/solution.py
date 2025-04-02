"""
Lenyk Nikita
Solution: Linked Lists - Sorted Insert
"""


class Node:
    """
    Linked list representation
    """

    def __init__(self, data: str | int, next: "Node" | None = None):
        self.data = data
        self.next = next


def sorted_insert(head: "Node", data: "Node") -> "Node":
    """
    Inserts the given number in descending order.

    Args:
        head (Node): The head node on linked list.
        data (Node): the data to insert in right order.

    Returns:
        Node: The head Node if done succesfully
    """
    new_node = Node(data)

    if head is None:
        return new_node

    if data < head.data:
        new_node.next = head
        return new_node

    curr = head
    while curr.next is not None and data > curr.next.data:
        curr = curr.next

    new_node.next = curr.next
    curr.next = new_node
    return head
