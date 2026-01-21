import numpy as np
from enum import Enum

class QubitState(Enum):
    GROUND = 0
    EXCITED = 1

class VirtualQubit:
    """Simplified virtual qubit for demonstration"""
    def __init__(self, qubit_id: int):
        self.qubit_id = qubit_id
        self.state = QubitState.GROUND
    
    def apply_gate(self, gate_type: str, time_ns: float) -> float:
        return 0.0  # Demo error prob
    
    def measure(self) -> tuple[int, float]:
        return 0, 0.99  # Demo measurement

class QuantumProcessor:
    """Simplified processor for demonstration"""
    def __init__(self, num_qubits: int = 32):
        self.num_qubits = num_qubits
        self.qubits = [VirtualQubit(i) for i in range(num_qubits)]
    
    def execute_gate(self, gate_type: str, targets: list[int]) -> float:
        return 0.0  # Demo error
    
    def get_processor_fidelity(self) -> float:
        return 0.99  # Demo fidelity
    
    def measure_all(self) -> tuple[list[int], float]:
        return [0] * self.num_qubits, 0.99
