class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def insert_at_head(self, data) -> None:
        """Insert a new node at the head in O(1) time."""
        new_node = Node(data)

        if self.head is None:
            # The first node is both the head and the tail.
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

        self.size += 1

    def remove_from_tail(self):
        """Remove and return the tail node's data in O(1) time."""
        if self.tail is None:
            raise IndexError("Cannot remove from an empty linked list")

        removed_data = self.tail.data

        if self.head is self.tail:
            # The list contained only one node.
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

        self.size -= 1
        return removed_data

    def search(self, key_condition_func) -> Node:
        """Search nodes from the head and return the first match."""
        current = self.head

        while current is not None:
            if key_condition_func(current.data):
                return current

            current = current.next

        return None