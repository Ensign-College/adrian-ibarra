from structures.static_array import StaticArray
from structures.dynamic_linked_list import DoublyLinkedList

class TelemetryBufferQueue:
    """
    Behavior Requirement: FIFO (First In, First Out)
    Constraint: Data volume fluctuates intensely. 
    Selection: Should we use a Static Array or a Dynamic Linked List?
    """
    def __init__(self):
        # TODO: Instantiate the correct structure chosen from your tasks
        self.storage = DoublyLinkedList() 

    def enqueue_packet(self, packet: dict) -> None:
        """TODO: Add packet to the queue"""
        pass

    def dequeue_packet(self) -> dict:
        """TODO: Remove and return the oldest packet"""
        pass


class EmergencyOverrideStack:
    """
    Behavior Requirement: LIFO (Last In, First Out)
    Constraint: Memory is strictly limited to 10 slots for system stability.
    Selection: Array-based stack vs Linked List stack? 
    """
    def __init__(self, max_capacity=10):
        # TODO: Instantiate the correct structure to optimize access and enforce capacity limits
        self.storage = StaticArray(max_capacity)
        self.top_index = -1

    def push_critical_signal(self, error_code: str) -> None:
        """TODO: Push onto stack. Raise OverflowError if max_capacity exceeded."""
        pass

    def pop_critical_signal(self) -> str:
        """TODO: Pop from stack. Raise IndexError if empty."""
        pass


class GridZoneNode:
    """
    Behavior Requirement: Hierarchical / Non-Linear Tree Organization
    """
    def __init__(self, zone_name: str):
        self.zone_name = zone_name
        self.children = [] # Holds sub-zone nodes

    def add_sub_zone(self, child_node) -> None:
        self.children.append(child_node)
