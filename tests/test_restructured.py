#!/usr/bin/env python3
"""
Test QuantumNeuralVM modules
"""

import sys
import unittest
from qnvm import MemoryEfficientSimulator, QuantumProcessor, SparseQuantumState, QuantumStateValidator

class TestQNVM(unittest.TestCase):
    """Unit tests for QNVM components"""
    
    def test_simulator(self):
        """Test MemoryEfficientSimulator"""
        sim = MemoryEfficientSimulator(max_memory_gb=8.0)
        method = sim.select_simulation_method(num_qubits=16)
        self.assertIn(method, ['statevector', 'mps', 'sparse'])
        
        result = sim.simulate_ghz_circuit(num_qubits=4)
        self.assertIn('method', result)
        self.assertGreaterEqual(result['memory_used_gb'], 0)
    
    def test_processor(self):
        """Test QuantumProcessor"""
        proc = QuantumProcessor(num_qubits=4)
        self.assertEqual(len(proc.qubits), 4)
        
        error = proc.execute_gate('H', targets=[0])
        self.assertEqual(error, 0.0)
        
        fidelity = proc.get_processor_fidelity()
        self.assertEqual(fidelity, 0.99)
    
    def test_sparse_state(self):
        """Test SparseQuantumState"""
        state = SparseQuantumState(num_qubits=4)
        stats = state.get_stats()
        self.assertEqual(stats['num_qubits'], 4)
        self.assertEqual(stats['num_nonzero'], 1)
    
    def test_validator(self):
        """Test QuantumStateValidator"""
        validator = QuantumStateValidator()
        test_state = np.array([1/np.sqrt(2), 1/np.sqrt(2)], dtype=np.complex128)
        validation = validator.validate_state(test_state)
        self.assertTrue(validation['valid'])
        self.assertAlmostEqual(validation['norm'], 1.0)

if __name__ == "__main__":
    unittest.main()
