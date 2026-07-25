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
        """TODO: Implement O(1) insertion at head"""
        pass

    def remove_from_tail(self):
        """TODO: Implement O(1) removal from tail (returns the data)"""
        pass

    def search(self, key_condition_func) -> Node:
        """TODO: Linear search O(n) using a lambda/condition function"""
        pass
