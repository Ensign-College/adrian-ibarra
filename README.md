# Module 2 Assignment: The Edge-Gateway Telemetry Router

## Setup

To install the required Python modules, run this command:

```bash
$ python -m pip install -r requirements.txt
```

*n.b. replace `python` with `python3` if required on your system*



## Context
You are deploying software on an IoT Edge Gateway device installed in a remote solar power grid. The device monitors live sensor telemetries, handles emergency override signals, and maps sensor IDs to system metadata. 

However, you have strict hardware constraints:
1. **Limited RAM:** You cannot let Python dynamically resize lists infinitely. Memory must be managed tightly.
2. **Predictable Runtime:** Emergency signals must be processed in $O(1)$ time. 
3. **Hierarchy Representation:** Sensors are grouped into geographical zones (hierarchical data).

To succeed, you cannot use Python's built-in `list` methods like `.append()`, `.insert()`, or `dict`. You must implement the underlying structures from scratch to respect these hardware constraints.

---

## Architectural Requirements & Core Tasks

### Task 1: Fixed-Size Static Array (`static_array.py`)
* **Topic Focus:** *Static Data Structures to Optimize Access Time*
* **Challenge:** Implement a true fixed-size array (`StaticArray`). If initialized with a capacity of 50, it reserves exactly 50 slots (using a low-level primitive style) and throws an `OverflowError` if a 51st element is added. It must offer $O(1)$ random access.

### Task 2: Dynamic Memory Packet Pool (`dynamic_linked_list.py`)
* **Topic Focus:** *Dynamic Data Structures (Linked List)*
* **Challenge:** When data burst sizes are unpredictable, static arrays waste space or overflow. Implement a `DoublyLinkedList` to store telemetry packets dynamically. You must implement `insert_at_head`, `remove_from_tail`, and a manual search loop.

### Task 3: The Fixed-Bucket Hash Table (`custom_hash_table.py`)
* **Topic Focus:** *Hash Table & Dynamic Queue for Optimization*
* **Challenge:** Build a `SensorRegistry` using a custom Hash Table with **Chaining (using your Linked List from Task 2)**. Python's native dictionaries automatically resize and consume huge memory overhead; your custom implementation will use a fixed number of buckets to optimize access time under strict memory ceilings.

### Task 4: Behavioral Integration (`router.py`)
* **Topic Focus:** *Stack, Queue, and Tree Selection*
* **Challenge:** Combine your structures to execute behavioral logic:
  1. **Telemetry Pipeline (Queue Behavior):** First-In, First-Out processing of standard sensor data.
  2. **Emergency Override Crash Log (Stack Behavior):** Last-In, First-First processing of emergency diagnostic codes (we need to inspect the absolute latest crash reason first).
  3. **Zone Topology (Tree Behavior):** Model how sensor groups roll up into regions (e.g., Global -> Country -> State -> Grid Zone).
