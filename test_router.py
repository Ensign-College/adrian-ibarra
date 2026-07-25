import pytest
from structures.static_array import StaticArray
from structures.dynamic_linked_list import DoublyLinkedList
from structures.custom_hash_table import SensorRegistryHashTable
from router import TelemetryBufferQueue, EmergencyOverrideStack

def test_emergency_stack_lifo_and_overflow():
    # Capacity restricted to 3 for strict memory testing
    stack = EmergencyOverrideStack(max_capacity=3)
    
    stack.push_critical_signal("ERR_001")
    stack.push_critical_signal("ERR_002")
    stack.push_critical_signal("ERR_003")
    
    # Test Enforced Memory Ceiling
    with pytest.raises(OverflowError):
        stack.push_critical_signal("ERR_004")
        
    # Test LIFO Behavior
    assert stack.pop_critical_signal() == "ERR_003"
    assert stack.pop_critical_signal() == "ERR_002"
    assert stack.pop_critical_signal() == "ERR_001"

def test_telemetry_queue_fifo():
    queue = TelemetryBufferQueue()
    queue.enqueue_packet({"sensor": "S1", "val": 22.5})
    queue.enqueue_packet({"sensor": "S2", "val": 24.1})
    
    # Test FIFO Behavior
    first = queue.dequeue_packet()
    assert first["sensor"] == "S1"
    
    second = queue.dequeue_packet()
    assert second["sensor"] == "S2"

def test_hash_table_chaining():
    registry = SensorRegistryHashTable(num_buckets=2) # Small buckets to force collisions
    
    registry.put("TEMP_SENSOR_1", "Zone A")
    registry.put("VOLT_SENSOR_2", "Zone B") # Will likely collide into same bucket index
    
    assert registry.get("TEMP_SENSOR_1") == "Zone A"
    assert registry.get("VOLT_SENSOR_2") == "Zone B"
    
    # Test update capability
    registry.put("TEMP_SENSOR_1", "Zone C")
    assert registry.get("TEMP_SENSOR_1") == "Zone C"
