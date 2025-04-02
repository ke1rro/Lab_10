"""
Lenyk Nikita
Solution: Convert a linked list to a string
"""

class Node:
    """
    Linked list representation
    """

    def __init__(self, data: str | int, next: "Node" | None = None):
        self.data = data
        self.next = next


def stringify(node: "Node") -> str:
    """
    Converts linkes list into string
    """
    nodes = []
    try:
        while node.data is not None:
            nodes.append(node.data)
            node = node.next
    except Exception:
        nodes.append(None)
        return " -> ".join(map(str, nodes))
