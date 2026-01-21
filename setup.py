setup.py
```python
from setuptools import setup, find_packages

setup(
    name="quantumneuralvm",
    version="5.1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "numpy>=1.24.0",
        "scipy>=1.11.0",
        "psutil>=5.9.0",
    ],
    python_requires=">=3.10",
    entry_points={
        'console_scripts': [
            'qnvm-benchmark = benchmarks.run_ghz_benchmark:run_ghz_benchmark',
        ],
    },
)
