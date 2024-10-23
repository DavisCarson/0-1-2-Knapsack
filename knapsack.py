import random

def knapsack(values, weights, max_capacity):
    n = len(values)
    table = [[0 for x in range(max_capacity+1)] for y in range(n+1)]

    for i in range(1, n+1):
        for j in range(1, max_capacity+1):
            if weights[i-1] > j:
                # If even one copy is too heavy, skip
                table[i][j] = table[i-1][j]
            else:
                # Consider all three possibilities:
                options = [
                    table[i-1][j],  # Take 0 copies
                    values[i-1] + table[i-1][j-weights[i-1]]  # Take 1 copy
                ]

                # Only consider 2 copies if there's enough capacity
                if 2 * weights[i-1] <= j:
                    options.append(2 * values[i-1] + table[i-1][j-2*weights[i-1]])  # Take 2 copies

                table[i][j] = max(options)

    print("Final matrix:")
    for row in table:
        print(row)
    return table[n][max_capacity]

if __name__ == '__main__':
    N = 15
    values = [random.randint(1, 10) for i in range(N)]
    weights = [random.randint(1, 10) for i in range(N)]
    capacity = 25
    print(knapsack(values, weights, capacity))
