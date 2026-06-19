"""Pytest bootstrap for running tests from arbitrary launchers.

Some Windows setups invoke pytest through a global/Anaconda console script even
when the shell prompt is inside this repo. Keep the project root importable so
`from pipeline import ...` works consistently during collection.
"""
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parent.parent
root_str = str(ROOT)
if root_str not in sys.path:
    sys.path.insert(0, root_str)
