8-puzzle-solver/
│
├── src/
│   ├── __init__.py
│   ├── puzzle_solver.py               # Core solver logic
│   ├── gui.py                         # GUI implementation using Tkinter
│   ├── heuristics.py                  # Heuristic functions for A* or other algorithms
│   ├── search_algorithms.py           # Contains various search algorithms (A*, BFS, etc.)
│   └── config.py                      # Configuration file for default states, constraints, etc.
│
├── tests/
│   ├── __init__.py
│   ├── test_solver.py                 # Unit tests for the solver
│   ├── test_gui.py                    # Unit tests for the GUI
│   ├── test_heuristics.py             # Unit tests for heuristic functions
│   └── test_search_algorithms.py      # Unit tests for search algorithms
│
├── assets/                            # Assets for GUI, if needed (icons, images, etc.)
│   └── logo.png                       # Example asset (logo or other images)
│
├── docs/                              # Documentation
│   ├── README.md                      # Project overview, installation, and setup
│   ├── INSTALL.md                     # Installation instructions
│   └── USER_GUIDE.md                  # User manual for interacting with the GUI
│
├── requirements.txt                   # Project dependencies (e.g., tkinter, psutil)
├── run.py                             # Main script to run the GUI or solver
└── LICENSE                            # License file for the project
