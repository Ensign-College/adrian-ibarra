class StaticArray:
    def __init__(self, capacity: int):
        self.capacity = capacity
        # Mimic raw hardware allocation: memory slots are fixed and pre-allocated
        self._memory = [None] * capacity
        self.size = 0

    def get(self, index: int):
        if index < 0 or index >= self.capacity:
            raise IndexError("Hardware Memory Access Violation: Out of Bounds")
        return self._memory[index]

    def set(self, index: int, value) -> None:
        if index < 0 or index >= self.capacity:
            raise IndexError("Hardware Memory Access Violation: Out of Bounds")
        if self._memory[index] is None and value is not None:
            self.size += 1
        elif self._memory[index] is not None and value is None:
            self.size -= 1
        self._memory[index] = value
