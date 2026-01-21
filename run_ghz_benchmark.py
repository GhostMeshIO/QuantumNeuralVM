#!/usr/bin/env python3
"""
Run GHZ benchmark for QuantumNeuralVM
"""

import argparse
import json
import time
import os
from qnvm import MemoryEfficientSimulator

def run_ghz_benchmark(qubits: int, method: str = 'auto', output_dir: str = 'benchmarks/results'):
    """Run GHZ benchmark and save results"""
    sim = MemoryEfficientSimulator(max_memory_gb=8.0)
    
    start_time = time.time()
    result = sim.simulate_ghz_circuit(num_qubits=qubits, method=method)
    elapsed = time.time() - start_time
    
    # Add timestamp
    result['timestamp'] = time.strftime("%Y-%m-%d %H:%M:%S")
    result['execution_time_sec'] = elapsed
    
    # Save to JSON
    os.makedirs(output_dir, exist_ok=True)
    filename = f'ghz_{qubits}_qubits_{method}.json'
    with open(os.path.join(output_dir, filename), 'w') as f:
        json.dump(result, f, indent=4)
    
    print(f"Benchmark saved to {os.path.join(output_dir, filename)}")
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run GHZ benchmark")
    parser.add_argument("--qubits", type=int, default=16, help="Number of qubits")
    parser.add_argument("--method", type=str, default="auto", help="Simulation method")
    
    args = parser.parse_args()
    run_ghz_benchmark(args.qubits, args.method)
