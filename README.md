# Knapsack Problem Solver

This repository contains a short Python implementation of the **Knapsack problem**. The goal is to maximize the value of items you can carry in a knapsack with a fixed weight capacity, while considering constraints on the number of copies you can take for each item.

### How It Works
The solver addresses the **0-1 knapsack** problem with an added twist: it allows up to **two copies** of each item. The dynamic programming algorithm builds a table that tracks the maximum value achievable for every possible capacity from 0 to the specified max capacity.

### Key Features
- **Dynamic Programming Table:**  
  The `knapsack()` function constructs a 2D table where each entry `table[i][j]` represents the maximum value that can be obtained with the first `i` items and a knapsack capacity of `j`.
  
- **Multiple Copy Consideration:**  
  The solver allows you to take 0, 1, or 2 copies of each item, and dynamically selects the optimal choice based on the remaining capacity.
  
- **Randomized Input Generation:**  
  The item values and weights are generated randomly for each run of the program, allowing for various test cases to be explored.

### File Overview
- **main.py**:  
  Contains all the core functions:
  - `knapsack()`: Implements the dynamic programming solution that handles 0, 1, or 2 copies of each item.
  
### Example Run
1. **Randomized Input Generation:**  
   The script generates random values and weights for `N = 15` items with capacities between 1 and 10. Example values:
   ```python
   values = [3, 8, 2, 5, 7, ...]  
   weights = [5, 3, 7, 2, 6, ...]  
   capacity = 25
   ```

2. **Dynamic Programming Table Output:**  
   The table constructed by the dynamic programming algorithm is printed, allowing you to visually see the decisions made at each step.

3. **Final Output:**  
   The program prints the maximum value that can be achieved with the given item weights, values, and the specified capacity.

### How to Use
1. Clone the repository.
2. Run the script using Python:
   ```bash
   python main.py
   ```
   The program will generate a random knapsack problem and solve it, displaying the dynamic programming table and the final result.

### Future Improvements
- Extend the algorithm to handle **multiple copies** beyond 2, allowing more flexibility in how items can be packed.
- Add a **user input feature** to specify values, weights, and capacities manually.
- Implement a **graphical visualization** for the table-building process.
