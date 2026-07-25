from structures.dynamic_linked_list import DoublyLinkedList


class KeyValuePair:
    def __init__(self, key: str, value: any):
        self.key = key
        self.value = value


class SensorRegistryHashTable:
    """
    Fixed-bucket hash table using linked-list chaining
    to resolve collisions.
    """

    def __init__(self, num_buckets: int = 10):
        if num_buckets <= 0:
            raise ValueError("The number of buckets must be greater than zero")

        self.num_buckets = num_buckets
        self.buckets = [
            DoublyLinkedList() for _ in range(num_buckets)
        ]

    def _hash_function(self, key: str) -> int:
        """Convert a string key into a valid bucket index."""
        return sum(ord(char) for char in key) % self.num_buckets

    def put(self, key: str, value: any) -> None:
        """Insert a new key-value pair or update an existing one."""
        bucket_index = self._hash_function(key)
        bucket = self.buckets[bucket_index]

        matching_node = bucket.search(
            lambda pair: pair.key == key
        )

        if matching_node is not None:
            matching_node.data.value = value
        else:
            new_pair = KeyValuePair(key, value)
            bucket.insert_at_head(new_pair)

    def get(self, key: str) -> any:
        """Return the value associated with a key."""
        bucket_index = self._hash_function(key)
        bucket = self.buckets[bucket_index]

        matching_node = bucket.search(
            lambda pair: pair.key == key
        )

        if matching_node is None:
            raise KeyError(f"Sensor ID not found: {key}")

        return matching_node.data.value