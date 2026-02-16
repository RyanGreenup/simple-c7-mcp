### Install CPMpy Library (Bash)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/quickstart_sudoku.ipynb

Installs the core CPMpy library using `pip3`, which is essential for defining and solving constraint programming problems.

```bash
pip3 install cpmpy
```

--------------------------------

### Install CPMpy and Visualization Libraries (Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/quickstart_sudoku.ipynb

Installs CPMpy along with `pandas`, `matplotlib`, and `seaborn` using pip, which are used for data handling and graphical visualization of the Sudoku solution.

```python
!pip install cpmpy pandas matplotlib seaborn --quiet
```

--------------------------------

### Install CPMpy with pip

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

Installs the CPMpy library along with its default ORTools solver using Python's package installer, pip. This is the standard way to get started with CPMpy.

```commandline
pip install cpmpy
```

--------------------------------

### List All Installed CPMpy Solvers and Subsolvers (Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

This Python example illustrates how to get a comprehensive list of all installed solvers and their subsolvers on your system. Calling `cp.SolverLookup.solvernames()` returns a flattened list, including both base solver names and specific subsolver names (e.g., 'minizinc:chuffed'). This provides a complete overview of all callable solver options.

```python
import cpmpy as cp
cp.SolverLookup.solvernames()
```

--------------------------------

### Managing CPMpy Solvers

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/summary.rst

Illustrates how to list all installed solvers accessible by CPMpy and how to initialize a specific solver instance. This is useful for explicitly selecting a solver other than the default one.

```python
import cpmpy as cp

# List all available solvers (including subsolvers)
solvers = cp.SolverLookup.solvernames()
print(f"Available solvers: {solvers}")

# Initialize a specific solver (e.g., 'ortools')
# This often requires a model object to associate with the solver
# x = cp.intvar(1, 10)
# model = cp.Model(x > 5)
# specific_solver = cp.SolverLookup.get("ortools", model=model)
# print(f"Initialized solver: {specific_solver}")
```

--------------------------------

### Install Python Packaging Build Tools

Source: https://github.com/cpmpy/cpmpy/wiki/Packaging-Releasing-Publishing

These commands install or upgrade the necessary Python packages for building and distributing the project. `build` is used for PyPA builds, `wheel` for Setuptools, and `twine` for securely uploading packages to PyPI.
Run these commands in your development environment to prepare for package building.

```bash
python3 -m pip install --upgrade build
```

```bash
python3 -m pip install --upgrade wheel
```

```bash
python3 -m pip install --upgrade twine
```

--------------------------------

### Python: Example of Full Sudoku Explanation Sequence Generation

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/tutorial_ijcai22/6_explain_sudoku.ipynb

This example showcases the usage of the `explain_full_sudoku` function to generate a complete, stepwise explanation for a given 4x4 Sudoku puzzle. It sets up the Sudoku problem, determines initial clues and the variables requiring explanation, and then invokes `explain_full_sudoku`. The function returns a sequence of explanations that detail the solution process from start to finish.

```python
given = given_4x4

cells, facts, constraints = model_sudoku(given)

clues = {var : val for var, val in zip(cells.flatten(), given.flatten()) if val != e}
vars_to_expl = set(get_variables(constraints)) - set(clues.keys())

start = time()
explain_full_sudoku(clues, vars_to_expl, constraints, verbose=True)
```

--------------------------------

### Install NetworkX and Matplotlib Libraries

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/graph_coloring.ipynb

This command installs the `networkx` library, essential for creating and manipulating graph structures, and `matplotlib` for plotting and visualization of graphs, which are core dependencies for this graph coloring example.

```python
! pip install networkx matplotlib --quiet
```

--------------------------------

### Solve Sudoku Model and Print Result (CPMpy Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/quickstart_sudoku.ipynb

Invokes the solver on the `cpmpy.Model` to find a solution. If successful, it prints the solved Sudoku grid; otherwise, it reports that no solution was found.

```python
# Solve and print
if model.solve():
    print(puzzle.value())
else:
    print("No solution found")
```

--------------------------------

### Provide Solution Hints to OR-Tools Solver in CPMpy

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

This Python example shows how to use the `solution_hint()` method in CPMpy for OR-Tools. It allows the solver to start its search from a given set of variable-value assignments, potentially speeding up the search process by guiding it with a previous solution or a good starting point. This feature is specific to certain solvers like OR-Tools.

```python
import cpmpy as cp
x = cp.intvar(0,10, shape=3)
s = cp.SolverLookup.get("ortools")
s += cp.sum(x) <= 5
# we are operating on an ortools' interface here
s.solution_hint(x, [1,2,3])
s.solve()
print(x.value())
```

--------------------------------

### Display Solved Sudoku Grid Graphically (Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/quickstart_sudoku.ipynb

Calls the previously defined `visu_sudoku` function, passing the solved `puzzle.value()` to render a graphical representation of the Sudoku solution using `matplotlib` and `seaborn`.

```python
visu_sudoku(puzzle.value())
```

--------------------------------

### Change and Re-solve CPMpy Optimization Model Objective

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/beginner_tutorial.rst

This example demonstrates the flexibility of CPMpy by showing how to change the objective of an already defined model without redefining all constraints. Here, the objective is switched from maximizing 'MONEY' to maximizing 'MOST' using `model.maximize()`. The model is then re-solved, and the new optimal solution for the updated objective is printed, showcasing the ability to easily iterate on optimization problems.

```python
model.maximize(sum( [m, o, s, t] * np.array([1000, 100, 10, 1]) ) )
model.solve()
print("  S,E,N,D =   ", [x.value() for x in [s, e, n, d]])
print("  M,O,S,T =   ", [x.value() for x in [m, o, s, t]])
print("M,O,N,E,Y =", [x.value() for x in [m, o, n, e, y]])
```

--------------------------------

### Install CPMpy with specific optional solvers

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/installation_instructions.rst

Installs CPMpy along with a chosen subset of optional solver backends as additional dependencies. Users can specify multiple solvers in square brackets to extend CPMpy's capabilities with different technologies.

```bash
# Choose any subset of solvers to install
$ pip install cpmpy[choco, cpo, exact, gcs, gurobi, minizinc, pysat, pysdd, z3]
```

--------------------------------

### Install a local copy of CPMpy for development

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/installation_instructions.rst

Installs the CPMpy package from the current local directory, typically used when developing the library itself. This allows local changes to be tested as if the package were formally installed.

```console
$ pip install .
```

--------------------------------

### Solve a CPMpy Satisfaction Problem Model

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/beginner_tutorial.rst

This snippet demonstrates the basic way to solve a CPMpy model. Calling `.solve()` on the model automatically searches for an installed solver and attempts to find a solution. For satisfaction problems, it returns True if a solution is found, False otherwise.

```python
model.solve()
```

--------------------------------

### Create GitHub Release Using GitHub CLI

Source: https://github.com/cpmpy/cpmpy/wiki/Packaging-Releasing-Publishing

This command automates the creation of a new release on GitHub using the `gh` command-line interface. It uses the specified version tag and populates the release notes from a `changelog.md` file.
Before running, ensure `github-cli` is installed and a `changelog.md` file with release details exists.

```bash
gh release create v0.5.5 -F changelog.md
```

--------------------------------

### Install CPMpy directly from a Git repository

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/installation_instructions.rst

Installs the CPMpy package directly from its GitHub repository, enabling access to the very latest code or specific development branches. The command can be modified to target a different branch or commit hash.

```console
$ pip install git+https://github.com/cpmpy/cpmpy@master
```

--------------------------------

### Common CPMpy Model Setup for Solution Enumeration

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/multiple_solutions.md

This Python code defines a basic CPMpy model with an integer variable array 'x' and a constraint 'x[0] > x[1]'. This setup serves as the foundation for the subsequent `solveAll()` examples demonstrating various ways to retrieve solutions.

```python
from cpmpy import *
x = intvar(0, 3, shape=2)
m = Model(x[0] > x[1])
```

--------------------------------

### CPMpy Model Creation and Basic Operations

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/summary.rst

Demonstrates how to initialize a CPMpy model, add constraints to it, define objective functions (maximization or minimization), and execute the solving process. It also illustrates retrieving the solver's status and the obtained objective value after a run.

```python
import cpmpy as cp

# Example setup for constraint and objective
x = cp.intvar(1, 10, name="x")
y = cp.intvar(1, 10, name="y")
constraint = (x + y == 15)
obj = x * y

model = cp.Model()
model += constraint # Add a constraint to the model
model.maximize(obj) # Set an objective to maximize
# To minimize: model.minimize(obj)

result = model.solve() # Solve the model
print(f"Solve successful: {result}")

# To enumerate all solutions:
# num_solutions = model.solveAll()
# print(f"Number of solutions found: {num_solutions}")

status = model.status() # Get solver status
print(f"Solver status: {status}")

objective_val = model.objective_value() # Get the objective value
print(f"Objective value: {objective_val}")

# To access variable values after solving
if result:
    print(f"x value: {x.value()}")
    print(f"y value: {y.value()}")
```

--------------------------------

### Build Python Distribution with PyPA Build

Source: https://github.com/cpmpy/cpmpy/wiki/Packaging-Releasing-Publishing

This command uses the PyPA `build` tool to create both source archives (`.tar.gz`) and built distributions (`.whl`). It generates files in the `dist/` directory suitable for PyPI.
Ensure `PyPA build` is installed before executing this command.

```bash
python3 -m build
```

--------------------------------

### Build Python Distribution with Setuptools

Source: https://github.com/cpmpy/cpmpy/wiki/Packaging-Releasing-Publishing

These commands utilize `setuptools` to create different types of Python package distributions. `sdist` generates a source archive, while `bdist_wheel` creates a built distribution (`.whl`).
The output files are placed in the `dist/` directory, similar to PyPA builds.

```bash
python3 setup.py sdist
```

```bash
python3 setup.py bdist_wheel
```

--------------------------------

### Iterate and Solve CPMpy Model with Multiple Solvers (Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

This Python example shows how to systematically solve the same CPMpy model using all installed solvers and subsolvers. By iterating through the list returned by `cp.SolverLookup.solvernames()`, you can solve the model with each available option and then print the model's status. This is useful for benchmarking different solvers or identifying the best-performing solver for a specific problem.

```python
# m = same model as above
for solvername in cp.SolverLookup.solvernames(): # all solvers (+subsolvers) installed on the system
    m.solve(solver=solvername)
    print(m.status())
```

--------------------------------

### Define Initial Sudoku Puzzle Grid (Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/quickstart_sudoku.ipynb

Initializes a 9x9 NumPy array representing the Sudoku puzzle. `e` (defined as 0) marks empty cells that need to be filled, while other numbers represent given values.

```python
e = 0 # value for empty cells
given = np.array([
    [e, e, e,  2, e, 5,  e, e, e],
    [e, 9, e,  e, e, e,  7, 3, e],
    [e, e, 2,  e, e, 9,  e, 6, e],

    [2, e, e,  e, e, e,  4, e, 9],
    [e, e, e,  e, 7, e,  e, e, e],
    [6, e, 9,  e, e, e,  e, e, 1],

    [e, 8, e,  4, e, e,  1, e, e],
    [e, 6, 3,  e, e, e,  e, 8, e],
    [e, e, e,  6, e, 8,  e, e, e]])
```

--------------------------------

### Model and solve a 4x4 Sudoku example with CPMpy

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/tutorial_ijcai22/6_explain_sudoku.ipynb

This example demonstrates the complete workflow for solving a 4x4 Sudoku puzzle. It initializes a sample `given_4x4` grid, displays the input, then uses `model_sudoku` to create the constraint model and `extract_solution` to find the solution. Finally, `print_sudoku` is called to display the solved 4x4 grid.

```python
e = 0
given_4x4 = np.array([
    [ e, 3, 4, e ],
    [ 4, e, e, 2 ],
    [ 1, e, e, 3 ],
    [ e, 2, 1, e ],
])

display(HTML('<h3> INPUT SUDOKU</h3>'))
print_sudoku(given_4x4)

sudoku_4x4_vars, sudoku_4x4_facts, sudoku_4x4_constraints = model_sudoku(given_4x4)

sudoku_4x4_solution = extract_solution(
    constraints=sudoku_4x4_constraints + sudoku_4x4_facts, 
    variables=sudoku_4x4_vars
)

display(HTML('<h3> SOLUTION </h3>'))
print_sudoku(sudoku_4x4_solution)
```

--------------------------------

### Define Sudoku Visualization Function (Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/quickstart_sudoku.ipynb

Defines `visu_sudoku`, a Python function that uses `matplotlib` and `seaborn` to create a visual representation of a Sudoku grid. It highlights 3x3 blocks with alternating background colors for better readability.

```python
import matplotlib.pyplot as plt
import seaborn as sns
import math

# matplotlib/seaborn graphical visualisation
def visu_sudoku(grid, figsize=(6,6)):
    N = int(math.sqrt(grid.shape[0]))

    # block-by-block alternation
    bg = np.zeros(grid.shape)
    for i in range(0,9, 3):
        for j in range(0,9, 3):
            if (i+j) % 2:
                bg[i:i+3, j:j+3] = 1
        
    # the figure
    fig, ax = plt.subplots(1, 1, figsize=figsize)
    sns.set(font_scale=2)
    sns.heatmap(bg, annot=grid,
                cbar=False, linewidths=1, xticklabels=False, yticklabels=False)
    
    plt.title(f"Sudoku {grid.shape[0]}x{grid.shape[1]}", fontsize=15)
    plt.show()
```

--------------------------------

### Initialize Array of Integer Variables

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/tutorial/part2.ipynb

This snippet initializes an array of four integer variables, named 'x', where each variable has a domain ranging from 0 to 3. This setup provides a basic set of variables to which constraints can be applied in subsequent CPMpy model definitions.

```python
x = intvar(0,3, shape=4, name="x")
```

--------------------------------

### Install CPMpy for Development with pip

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/developers.md

Explains how to perform an editable installation of CPMpy using pip. This command links your local CPMpy folder to your Python environment, allowing any code changes to be automatically reflected without reinstallation, which is essential for active development.

```python
pip install --editable .
```

--------------------------------

### Model Sudoku Constraints (CPMpy Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/quickstart_sudoku.ipynb

Constructs the `cpmpy.Model` by applying `AllDifferent` constraints to each row, column, and 3x3 block of the `puzzle` variables. Additionally, it enforces that the `puzzle` variables match the initial `given` values for non-empty cells.

```python
# we create a model with the row/column constraints
model = Model(
    # Constraints on rows and columns
    [AllDifferent(row) for row in puzzle],
    [AllDifferent(col) for col in puzzle.T], # numpy's Transpose
)

# we extend it with the block constraints
# Constraints on blocks
for i in range(0,9, 3):
    for j in range(0,9, 3):
        model += AllDifferent(puzzle[i:i+3, j:j+3]) # python's indexing

# Constraints on values (cells that are not empty)
model += (puzzle[given!=e] == given[given!=e])
```

--------------------------------

### Install Python Libraries for VRP

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/vehicle_routing.ipynb

Installs the necessary Python packages, including `pandas` for data manipulation, `matplotlib` and `plotly` for visualization, and `geopy` for geographic distance calculations, which are required to run the VRP example.

```python
! pip install pandas matplotlib plotly geopy --quiet
```

--------------------------------

### Solve Basic Constraint Problem with CPMpy in Python

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/summary.rst

This Python example demonstrates how to define boolean and integer decision variables, formulate various constraints (e.g., equality, all-different, count, implication), and solve a simple optimization problem using the CPMpy library. It illustrates model creation, objective function definition for maximization, and how to print the solution values.

```python
import cpmpy as cp

# Decision Variables
b = cp.boolvar()
x1, x2, x3 = x = cp.intvar(1, 10, shape=3)

# Constraints
model = cp.Model()

model += (x[0] == 1)
model += cp.AllDifferent(x)
model += cp.Count(x, 9) == 1
model += b.implies(x[1] + x[2] > 5)

# Objective
model.maximize(cp.sum(x) + 100 * b)

# Solving
solved = model.solve()
if solved:
    print("Solution found:")
    print('b:', b.value(), ' x:', x.value().tolist())
else:
    print("No solution found.")
```

--------------------------------

### Install Map Coloring Dependencies (Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/map_coloring_oz.ipynb

Installs or upgrades necessary Python libraries like geopandas, shapely, and matplotlib. These packages are essential for handling geographical data and plotting maps, ensuring the environment is prepared for the visualization steps.

```python
! pip install --upgrade geopandas shapely matplotlib --quiet  # make sure they are at their latest version
```

--------------------------------

### Define CPMpy Model for SEND+MOST=MONEY Optimization Problem

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/beginner_tutorial.rst

This Python code defines a CPMpy model for an optimization variant of the cryptarithmetic puzzle, SEND+MOST=MONEY. It includes necessary imports for `numpy` and `cpmpy`, declares integer variables, applies the `AllDifferent` constraint, and sets up the arithmetic relation and leading digit constraints. This setup forms the basis for an optimization problem where an objective will be maximized.

```python
import numpy as np
from cpmpy import *

s, e, n, d, m, o, t, y = intvar(0, 9, shape=8)

model = Model(
    AllDifferent(s, e, n, d, m, o, t, y),
    (    sum(    [s, e, n, d] * np.array([       1000, 100, 10, 1]) ) \
       + sum(    [m, o, s, t] * np.array([       1000, 100, 10, 1]) ) \
      == sum( [m, o, n, e, y] * np.array([10000, 1000, 100, 10, 1]) ) ),
    s > 0,
    m > 0,
)
```

--------------------------------

### Check Installed CPMpy Solvers and Versions via CLI (Bash & Console)

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

This snippet illustrates how to use the CPMpy command-line interface to inspect the installed status and versions of available solvers on your system. The `cpmpy version` command provides a formatted table, detailing whether each solver and its subsolvers are installed, along with their respective versions. This is useful for quickly diagnosing solver availability.

```bash
cpmpy version
```

```console
CPMpy version: 0.9.26
Solver               Installed  Version        
--------------------------------------------------
ortools              Yes        9.12.4544
z3                   Yes        4.14.1.0       
minizinc             Yes        0.10.0
 ↳ cplex             Yes        22.1.2.0
 ↳ gecode            Yes        6.3.0
 ↳ cp-sat            Yes        9.12.4544
 ↳ highs             Yes        1.9.0
 ↳ chuffed           Yes        0.13.2
 ↳ coin-bc           Yes        2.10.12/1.17.10
gcs                  No         -
gurobi               No         -
pysat                No         -    
pysdd                No         -
exact                Yes        2.1.0
choco                No         -
cpo                  No         -
...                  ...        ...
```

--------------------------------

### Find All Solutions to a CPMpy Model

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/tutorial/part2.ipynb

This example demonstrates how to enumerate all distinct solutions for a given CPMpy model. It initializes integer variables, defines a simple constraint, and then iteratively solves the model, printing each solution found. Each solution is subsequently blocked to prevent duplicates and ensure all unique solutions are discovered.

```python
x = intvar(0,3, shape=2)
m = Model(x[0] > x[1])

while m.solve():
    print(x.value())
    m += ~all(x == x.value()) # block solution
```

--------------------------------

### Install additional CPMpy solvers via pip

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

Installs CPMpy along with specified optional solver backends like Gurobi, Choco, and Exact. This command allows users to leverage different optimization engines for their combinatorial problems.

```commandline
pip install cpmpy[gurobi, choco, exact]
```

--------------------------------

### Solve a CPMpy Model and Get Status

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

This Python example demonstrates how to create an integer programming model with `cpmpy`, add constraints and an objective function (maximization), solve it using `m.solve()`, and then inspect the solution status and objective value. It shows how to use `m.status()` for detailed solver state and `m.objective_value()` to retrieve the optimal value if a solution is found.

```python
import cpmpy as cp
xs = cp.intvar(1,10, shape=3)
m = cp.Model(cp.AllDifferent(xs), maximize=cp.sum(xs))

hassol = m.solve()
print("Status:", m.status())  # Status: ExitStatus.OPTIMAL (0.03033301 seconds)
if hassol:
    print(m.objective_value(), xs.value())  # 27 [10  9  8]
else:
    print("No solution found.")
```

--------------------------------

### Example Output of CPMPy Scheduling Solution

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/scheduling.ipynb

Displays the console output from the solved scheduling problem. This includes the minimized makespan (total time to complete all jobs) and the optimized start and end times for each task across all jobs.

```text
Output:
Makespan: 15
Start times: [[ 0  8 12]
 [ 0  5 11]
 [ 4  7 11]
 [ 0  7 10]]
End times: [[ 5 10 15]
 [ 4 10 12]
 [ 7 11 13]
 [ 1  8 11]]
```

--------------------------------

### Install Sphinx Python Documentation Generator

Source: https://github.com/cpmpy/cpmpy/wiki/Documentation-deployment

This command installs the Sphinx documentation generator for Python using pip. Sphinx is a powerful tool for creating structured and navigable project documentation.

```Shell
pip install sphinx
```

--------------------------------

### Naive MUS Extraction by Iterative Constraint Removal

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/tutorial/part2.ipynb

This example demonstrates a naive approach to finding a Minimal Unsatisfiable Set (MUS) from a set of constraints. It starts with an unsatisfiable model and iteratively removes one constraint at a time. If removing a constraint makes the model satisfiable, that constraint is considered part of the MUS; otherwise, it's discarded, and the process continues with the reduced set. This method can be computationally expensive.

```python
x = intvar(0,3, shape=4, name="x")
# circular 'bigger then', UNSAT
mus_cons = [
    x[0] > x[1],
    x[1] > x[2],
    x[2] > x[0],
    
    x[3] > x[0],
    (x[3] > x[1]).implies(x[3] > x[2]) & ((x[3] == 3) | (x[1] == x[2]))
]


i = 0 # we wil dynamically shrink mus_vars
while i < len(mus_cons):
    # add all other remaining constraints
    assum_cons = mus_cons[:i] + mus_cons[i+1:]

    if Model(assum_cons).solve():
        # with all but 'i' it is SAT, so 'i' belongs to the MUS
        print("\tSAT so in MUS:", mus_cons[i])
        i += 1
    else:
        # still UNSAT, 'i' does not belong to the MUS
        print("\tUNSAT so not in MUS:", mus_cons[i])
        # overwrite current 'i' and continue
        mus_cons = assum_cons
```

--------------------------------

### Install CPMpy for the current user

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/installation_instructions.rst

Installs the CPMpy Python package specifically for the current user. This command is useful when global package installation permissions are restricted, allowing installation without administrative privileges.

```console
$ pip install cpmpy --user
```

--------------------------------

### Handle Missing CPMpy Solver Package Exception (Console)

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

This console output demonstrates the error message received when attempting to use a CPMpy solver for which the underlying Python package has not been installed. For example, trying to use 'gurobi' without 'gurobipy' installed will raise an `Exception` with a helpful message. This highlights the dependency requirement for certain solvers.

```console
    Exception: CPM_gurobi: Install the python package 'gurobipy' to use this solver interface.
```

--------------------------------

### Solve Basic Knapsack Problem and Display Results

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/tutorial_ijcai22/7_counterfactual_explain.ipynb

Demonstrates how to instantiate and solve the knapsack problem generated by `get_knapsack_problem`. It calls the `solve()` method on the model and then prints the optimal objective value, the used capacity, and the arrays of item values, weights, and the original capacity. The output shows the resulting optimal item selection.

```python
model, (items, values, weights, capacity) = get_knapsack_problem()
assert model.solve()
print("Objective value:",model.objective_value())
print("Used capacity:", sum(items.value() * weights))

print(f"{values = }")
print(f"{weights = }")
print(f"{capacity = }")

items.value()
```

--------------------------------

### Visualize Example Sudoku Puzzle (Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/advanced/visual_sudoku.ipynb

This Python snippet demonstrates how to apply the previously defined functions to visualize a Sudoku puzzle. It first calls `sample_visual_sudoku` with a placeholder `numerical_sudoku` to generate its visual counterpart, then uses `show_grid_img` to display the resulting image grid. This provides a practical example of the visual Sudoku generation and display process.

```python
# Let's visualize a visual sudoku!
visual_sudoku = sample_visual_sudoku(numerical_sudoku)
show_grid_img(visual_sudoku)  # takes a few secs to display ImageGrid
```

--------------------------------

### Install CPMpy using pip

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/installation_instructions.rst

Installs the CPMpy Python package and its default 'ortools' solver using the pip package manager. This is the easiest and recommended method for setting up CPMpy.

```console
$ pip install cpmpy
```

--------------------------------

### Import necessary libraries for CPMpy modeling

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/beginner_tutorial.rst

This code snippet imports the 'numpy' library as 'np' for numerical operations and all components from the 'cpmpy' library, which is essential for building Constraint Programming models. These are the foundational imports required before defining variables or constraints.

```python
import numpy as np
from cpmpy import *
```

--------------------------------

### Install CPMpy XCSP3 tools dependencies

Source: https://github.com/cpmpy/cpmpy/blob/master/cpmpy/tools/xcsp3/README.md

This command installs the additional dependencies required for CPMpy's XCSP3 tooling. It ensures that all necessary packages for XCSP3 processing are available.

```console
pip install cpmpy[xcsp3]
```

--------------------------------

### Find All Solutions to a CPMpy Model

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

This Python example illustrates how to use `m.solveAll()` in `cpmpy` to find and count all feasible solutions for a given model. It sets up a simple model with two integer variables and a constraint, then calls `solveAll()` and prints the total number of solutions found.

```python
import cpmpy as cp
x = cp.intvar(0, 3, shape=2)
m = cp.Model(x[0] > x[1])

n = m.solveAll()
print("Nr of solutions:", n)  # Nr of solutions: 6
```

--------------------------------

### Perform Release Pre-Checks and GitHub Actions for CPMpy

Source: https://github.com/cpmpy/cpmpy/wiki/Packaging-Releasing-Publishing

These commands facilitate pre-release testing, version control updates, and initial GitHub release creation for the CPMpy project. They ensure code quality, proper versioning, and create the initial release draft on GitHub.
Before running, ensure `changelog.md` and `cpmpy/__init__.py` are updated.

```bash
python3 -m pytest tests
```

```bash
git commit -am "release X.Y.Z"
```

```bash
git push
```

```bash
python3 -m build
```

```bash
gh release create vX.Y.Z -F changelog.md
```

--------------------------------

### Find All Solutions with Display and Solution Limit in CPMpy

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

This Python example demonstrates advanced usage of `m.solveAll()` in `cpmpy`, showing how to use the `display` argument (with a list of expressions or a callback function) and `solution_limit` to control output and execution. The `display` argument can print specific expressions or execute a custom function for each found solution, while `solution_limit` restricts the number of solutions returned.

```python
# Using list of expressions
n = m.solveAll(display=[x,cp.sum(x)], solution_limit=3)
# [array([1, 0]), 1]
# [array([2, 0]), 2]
# [array([3, 0]), 3]

# Using callback function
n = m.solveAll(display=lambda: print([x.value(), cp.sum(x).value()]), solution_limit=3)
# ...
```

--------------------------------

### Python: Stand-alone OR-Tools Solver for Room Assignment (Commented)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/tutorial_ijcai22/1_room_assignment_incr.ipynb

Provides a commented-out example of a non-incremental approach to solving the room assignment problem using OR-Tools in `cpmpy` for a batch of 200 requests. It demonstrates model creation, solver instantiation, and a basic solve operation.

```python
print("Stand-alone, 200:")
(m, ordervars) = model_rooms(df_shuffle.iloc[:200,:], rooms, verbose=False)
s = SolverLookup.get('ortools', m)
if not s.solve():
        print("Got unsat?")
print("\t", s.status())
```

--------------------------------

### Install Python Dependencies for Sudoku Solver

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/advanced/visual_sudoku.ipynb

This command installs necessary Python packages required for the Sudoku solver, including `tqdm`, `torch`, `torchvision`, and `matplotlib`. These libraries support progress bars, deep learning components (for visual Sudoku), and plotting functionalities respectively.

```bash
! pip install tqdm>=4.40.0 torch torchvision matplotlib --quiet
```

--------------------------------

### Install Dependencies for Car Sequencing Model (Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/car_sequencing.ipynb

This command installs the necessary Python libraries, `pandas` and `matplotlib`, which are used for data manipulation and visualization of the car sequencing solution. The `--quiet` flag suppresses installation output.

```python
! pip install pandas matplotlib --quiet
```

--------------------------------

### Performing Incremental Solving with CPMpy and Gurobi

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

This example illustrates incremental solving using a Gurobi solver interface in CPMpy. It demonstrates adding an initial constraint, solving, then adding an additional constraint and solving again. CPMpy's eager translation and Gurobi's incremental nature allow the solver to reuse information from previous calls.

```python
s = SolverLookup.get("gurobi")

s += sum(ivar) <= 5 
s.solve()

s += sum(ivar) == 3
# the underlying gurobi instance is reused, only the new constraint is added to it.
# gurobi is an incremental solver and will look for solutions starting from the previous one.
s.solve()
```

--------------------------------

### Install Matplotlib for Visualization

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/packing_rectangles.ipynb

Installs the Matplotlib library, which is a critical dependency for generating graphical visualizations of the packed rectangles. The `--quiet` flag ensures a clean installation output.

```python
! pip install matplotlib --quiet
```

--------------------------------

### Using Core Expressions and Operators in CPMpy

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/summary.rst

Provides examples of constructing complex expressions by applying standard Python operators (comparison, arithmetic, logical) and CPMpy's built-in functions directly on decision variables or other expressions. It also covers logical implication and indexing into arrays using decision variables.

```python
import cpmpy as cp
from cpmpy.expressions.variables import cpm_array

# Assume x, y, z, bool_var1, bool_var2 are decision variables
x = cp.intvar(1, 10, name="x")
y = cp.intvar(1, 10, name="y")
z = cp.intvar(1, 10, name="z")
bool_var1 = cp.boolvar(name="b1")
bool_var2 = cp.boolvar(name="b2")
idx_var = cp.intvar(0, 2, name="idx")

# Comparison operators (create constraints)
constraint_eq = (x == y)
constraint_ne = (x != y)
constraint_lt = (x < y)
constraint_le = (x <= y)
constraint_gt = (x > y)
constraint_ge = (x >= y)

# Arithmetic operators (create expressions)
expression_sum = x + y
expression_diff = x - y
expression_prod = x * y
expression_div = x // y # Integer division
expression_mod = x % y
expression_pow = x ** 2

# Logical operators (on Boolean variables/expressions)
logical_and = (bool_var1 & bool_var2)
logical_or = (bool_var1 | bool_var2)
logical_not = (~bool_var1)
logical_xor = (bool_var1 ^ bool_var2)

# Logical implication
implication = bool_var1.implies(bool_var2)

# CPMpy built-in functions (vectorized operations)
total_sum = cp.sum([x, y, z])
absolute_val = cp.abs(x - y)
maximum_val = cp.max([x, y, z])
minimum_val = cp.min([x, y, z])
all_true = cp.all([bool_var1, bool_var2])
any_true = cp.any([bool_var1, bool_var2])

# Indexing CPMpy expressions or non-CPMpy arrays with decision variables
cpm_array_expr = cpm_array([10, 20, 30])
indexed_value = cpm_array_expr[idx_var]

```

--------------------------------

### MUS Extraction using OR-Tools Assumptions and Cores

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/tutorial/part2.ipynb

This more advanced example illustrates MUS extraction leveraging assumption variables and the UNSAT core capabilities of the 'CPM_ortools' solver. It reifies each constraint with a boolean indicator variable, obtains an initial UNSAT core, and then iteratively shrinks this core by testing assumptions. This method is generally more efficient than the naive approach for identifying minimal unsatisfiable subsets of constraints.

```python
x = intvar(0,3, shape=4, name="x")
# circular 'bigger then', UNSAT
mus_cons = [
    x[0] > x[1],
    x[1] > x[2],
    x[2] > x[0],
    
    x[3] > x[0],
    (x[3] > x[1]).implies(x[3] > x[2]) & ((x[3] == 3) | (x[1] == x[2]))
]


assum_model = Model()
# make assumption indicators, add reified constraints
ind = BoolVar(shape=len(mus_cons), name="ind")
for i,bv in enumerate(ind):
    assum_model += [bv.implies(mus_cons[i])]
# to map indicator variable back to soft_constraints
indmap = dict((v,i) for (i,v) in enumerate(ind))

assum_solver = CPM_ortools(assum_model)
assert (not assum_solver.solve(assumptions=ind)), "Model must be UNSAT"

# unsat core is an unsatisfiable subset
mus_vars = assum_solver.get_core()
print("UNSAT core of size", len(mus_vars))

# now we shrink the unsatisfiable subset further
i = 0 # we wil dynamically shrink mus_vars
while i < len(mus_vars):
    # add all other remaining constraints
    assum_vars = mus_vars[:i] + mus_vars[i+1:]

    if assum_solver.solve(assumptions=assum_vars):
        # with all but 'i' it is SAT, so 'i' belongs to the MUS
        print("\tSAT so in MUS:", mus_cons[i])
        i += 1
    else:
        # still UNSAT, 'i' does not belong to the MUS
        print("\tUNSAT so not in MUS:", mus_cons[i])
        # overwrite current 'i' and continue
        mus_vars = assum_vars
```

--------------------------------

### Retrieve and Print Solution from CPMpy Model

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/beginner_tutorial.rst

After solving a CPMpy model, this code shows how to check if a solution was found and then access the assigned values of the decision variables. The `.value()` method is used on each variable to retrieve its determined integer value. The results are printed for clarity.

```python
if model.solve():
    print("  S,E,N,D =   ", [x.value() for x in [s, e, n, d]])
    print("  M,O,R,E =   ", [x.value() for x in [m, o, r, e]])
    print("M,O,N,E,Y =", [x.value() for x in [m, o, n, e, y]])
else:
    print("No solution found")
```

--------------------------------

### Define Sudoku Decision Variables (CPMpy Python)

Source: https://github.com/cpmpy/cpmpy/blob/master/examples/quickstart_sudoku.ipynb

Creates a matrix of integer decision variables `puzzle` using `cpmpy.intvar`. Each variable can take values from 1 to 9, corresponding to the possible numbers in a Sudoku cell, and has the same shape as the `given` puzzle.

```python
puzzle = intvar(1, 9, shape=given.shape, name="puzzle")
```

--------------------------------

### Solve Flexible Jobshop Scheduling with CPMpy

Source: https://github.com/cpmpy/cpmpy/blob/master/README.md

This Python example demonstrates how to model and solve a flexible jobshop scheduling problem using the CPMpy library. It defines decision variables for start times, end times, and active tasks, sets up constraints for job completion, and non-overlapping machine usage using `cp.Cumulative`. The objective function minimizes a weighted sum of makespan and total energy consumption. It requires `cpmpy` and `pandas`.

```python
# Simple flexible job-shop: a set of jobs (each 1 task) must be run, each can be run on any of the machines,
# with different duration and energy consumption. Minimize makespan and total energy consumption
import cpmpy as cp
import pandas as pd
import random; random.seed(1)

# --- Data definition ---
num_jobs = 15
num_machines = 3
# Generate some data: [job_id, machine_id, duration, energy]
data = [[jobid, machid, random.randint(2, 8), random.randint(5, 15)]
        for jobid in range(num_jobs) for machid in range(num_machines)]
df_data = pd.DataFrame(data, columns=['job_id', 'machine_id', 'duration', 'energy'])

# Compute maximal horizon (crude upper bound) and number of alternatives
horizon = df_data.groupby('job_id')['duration'].max().sum()
num_alternatives = len(df_data.index)
assert list(df_data.index) == list(range(num_alternatives)), "Index must be default integer (0,1,..)"


# --- Decision variables ---
start = cp.intvar(0, horizon, name="start", shape=num_alternatives)
end   = cp.intvar(0, horizon, name="end", shape=num_alternatives)
active = cp.boolvar(name="active", shape=num_alternatives)

# --- Constraints ---
model = cp.Model()

# Each job must have one active alternative
for job_id, group in df_data.groupby('job_id'):
    model += (cp.sum(active[group.index]) == 1)

# For all jobs ensure start + dur = end (also for inactives, thats OK)
model += (start + df_data['duration'] == end)

# No two active alternatives on the same machine may overlap; (ab)use cumulative with 'active' as demand.
for mach_id, group in df_data.groupby('machine_id'):
    sel = group.index
    model += cp.Cumulative(start[sel], group['duration'].values, end[sel], active[sel], capacity=1)

# --- Objectives ---
# Makespan: max over all active alternatives
makespan = cp.intvar(0, horizon, name="makespan")
for i in range(num_alternatives):
    model += active[i].implies(makespan >= end[i])  # end times of actives determines makespan

# Total energy consumption
total_energy = cp.sum(df_data['energy'] * active)

# Minimize makespan first, then total energy
model.minimize(100 * makespan + total_energy)
```

--------------------------------

### Iterate and solve XCSP3 instances from dataset

Source: https://github.com/cpmpy/cpmpy/blob/master/cpmpy/tools/xcsp3/README.md

This example demonstrates how to iterate over an `XCSP3Dataset`, retrieving each instance's filename and metadata. It then uses `read_xcsp3` to load the instance into a CPMpy model and solves it, printing the solution status.

```python
from cpmpy.tools.xcsp3 import XCSP3Dataset, read_xcsp3

for filename, metadata in XCSP3Dataset(year=2024, track="COP", download=True): # auto download dataset and iterate over its instances
    # Do whatever you want here, e.g. reading to a CPMpy model and solving it:
    model = read_xcsp3(filename)
    model.solve()
    print(model.status())
```

--------------------------------

### Configure .pypirc for PyPI/TestPyPI Credentials

Source: https://github.com/cpmpy/cpmpy/wiki/Packaging-Releasing-Publishing

This configuration file stores PyPI and TestPyPI repository URLs and API tokens, allowing Twine to upload packages without requiring re-entry of credentials. It should be placed in the user's home directory (`$HOME/.pypirc`) to avoid repeated copy-pasting of tokens.

```ini
[distutils]
	index-servers =
	    pypi
	    testpypi
[pypi]
	repository = https://upload.pypi.org/legacy/
  username = __token__
  password = <the token value, including the `pypi-` prefix>
[testpypi]
	repository: https://test.pypi.org/legacy/
  username = __token__
  password = <the token value, including the `pypi-` prefix>
```

--------------------------------

### Directly Operating on a CPMpy Solver Interface

Source: https://github.com/cpmpy/cpmpy/blob/master/docs/modeling.md

This example illustrates how to directly obtain and interact with a CPMpy solver interface for OR-Tools. Constraints are added directly to the solver instance, and its status is queried after solving, showcasing that the solver interface supports the same functions as the `Model()` object.

```python
import cpmpy as cp
x = cp.intvar(0,10, shape=3) 
s = cp.SolverLookup.get("ortools")
# we are operating on the ortools interface here
s += (cp.sum(x) <= 5)
s.solve()
print(s.status())
```