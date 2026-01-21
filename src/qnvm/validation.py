import numpy as np

class QuantumStateValidator:
    """Simplified validator for demonstration"""
    def validate_state(self, state: np.ndarray) -> dict:
        norm = np.linalg.norm(state)
        return {
            'valid': abs(norm - 1.0) < 1e-10,
            'norm': norm
        }
