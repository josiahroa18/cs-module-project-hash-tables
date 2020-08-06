"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

#q = set(range(1, 10))
#q = set(range(1, 200))
def f(x):
    return x * 4 + 6

# Your code here
# Figure out how many combinations each set could potentiall hold
# Assign a new a, b, c, d each time it has been checked
# Find all combinations where f(a) + f(b) = f(c) - f(d) and print them out
# Example output for each combination: f(1) + f(1) = f(12) - f(7) 

def main():
    q = (1, 3, 4, 7, 12)
    spaces = ' ' * 5
    sums = {}
    diffs = {}
    for x in q:
        for y in q:
            sums[(x, y)] = f(x) + f(y) 
            diffs[(x, y)] = f(x) - f(y)

    for x in sums.keys():
        for y in diffs.keys():
            if sums[x] == diffs[y]:
                print(f"f({x[0]}) + f({x[1]}) = f({y[0]}) + f({y[1]})" + spaces + f"{sums[x]} = {diffs[y]}")



if __name__ == '__main__':
    main()