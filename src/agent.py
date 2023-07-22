import os
import sys

# Get the absolute path of the parent directory
parent_dir = os.path.dirname(os.path.abspath(__file__))
print(parent_dir)

# Add the parent directory to PYTHONPATH
sys.path.append(parent_dir)

