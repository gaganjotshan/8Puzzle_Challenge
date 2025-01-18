import os
from pathlib import Path

project_name = "8-puzzle-solver"

list_of_files = [
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/puzzle_solver.py",
    f"src/{project_name}/gui.py",
    f"src/{project_name}/heuristics.py",
    f"src/{project_name}/search_algorithms.py",
    f"src/{project_name}/config.py",
    "tests/__init__.py",
    "tests/test_solver.py",
    "tests/test_gui.py",
    "tests/test_heuristics.py",
    "tests/test_search_algorithms.py",
    "requirements.txt",
    "run.py",
    "LICENSE"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        print(f"Creating directory: {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        print(f"Creating empty file: {filepath}")
    else:
        print(f"{filename} already exists")

print(f"Project structure for '{project_name}' has been created.")
