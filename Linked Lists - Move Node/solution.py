"""
Lenyk Nikita
Solution: Linked Lists - Move Node
"""


class Node:
    """
    Linked list representation.
    """

    def __init__(self, data: str | int, next: "Node" | None = None):
        self.data = data
        self.next = next


class Context(object):
    """
    The Context to interact with the two lists easier.
    """

    def __init__(self, source, dest):
        self.source = source
        self.dest = dest


def move_node(source: "Node", dest: "Node") -> "Context":
    """
    Moves the first element from the source
    to the first element of the destination.

    Args:
        source (Node): The source linked list.
        dest (Node): The destination to move the first element to.

    Raises:
        TypeError: If the source is None

    Returns:
        Context: if first element moved succesfully.
    """
    if source is None:
        raise TypeError
    new_node = source
    source = source.next

    new_node.next = dest
    dest = new_node

    return Context(source, dest)
