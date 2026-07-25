from structures.static_array import StaticArray
from structures.dynamic_linked_list import DoublyLinkedList


class TelemetryBufferQueue:
    """
    FIFO telemetry queue implemented with a doubly linked list.
    """

    def __init__(self):
        self.storage = DoublyLinkedList()

    def enqueue_packet(self, packet: dict) -> None:
        """Add a new packet to the head of the linked list."""
        self.storage.insert_at_head(packet)

    def dequeue_packet(self) -> dict:
        """Remove and return the oldest packet from the tail."""
        return self.storage.remove_from_tail()


class EmergencyOverrideStack:
    """
    Fixed-capacity LIFO stack implemented with a StaticArray.
    """

    def __init__(self, max_capacity=10):
        self.storage = StaticArray(max_capacity)
        self.top_index = -1

    def push_critical_signal(self, error_code: str) -> None:
        """Push a signal onto the stack."""
        if self.top_index + 1 >= self.storage.capacity:
            raise OverflowError("Emergency override stack capacity exceeded")

        self.top_index += 1
        self.storage.set(self.top_index, error_code)

    def pop_critical_signal(self) -> str:
        """Remove and return the latest signal."""
        if self.top_index < 0:
            raise IndexError("Cannot pop from an empty emergency stack")

        error_code = self.storage.get(self.top_index)
        self.storage.set(self.top_index, None)
        self.top_index -= 1

        return error_code


class GridZoneNode:
    """
    Represents one node in the geographical zone hierarchy.
    """

    def __init__(self, zone_name: str):
        self.zone_name = zone_name
        self.children = []

    def add_sub_zone(self, child_node) -> None:
        self.children.append(child_node)