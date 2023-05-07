#1. Dead Code Elimination:

def compute_sum1(n): 
    unused_var = 42 # This variable is never used
    if n < 1:
        return 0
    total_sum = 0
    for i in range(n):
        total_sum += i
    unused_var = 99
    return total_sum

def compute_sum2(n):
    if n < 1:
        return 0
    total_sum = 0
    for i in range(n):
        total_sum += i
    return total_sum

# Example usage
print(compute_sum1(5))
print("after dead code elimination: ")
print(compute_sum2(5))


#2. Constant Propagation:

def multiply_by_two(x):
    # Constant value is propagated through the expression
    return 2 * x

# Example usage
print(multiply_by_two(3))
