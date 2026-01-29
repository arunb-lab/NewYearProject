#Recursion is a programming technique where a function calls itself 
# either directly or indirectly to solve a problem by breaking it into smaller, simpler subproblems.
def factorial(n):
    # Base case: if n is 0 or 1, return 1
    if n == 0 or n == 1:
        return 1
    else:
        # Recursive case: n * factorial of (n-1)
        return n * factorial(n - 1)
# Example usage
num = 5
result = factorial(num)
print(f"The factorial of {num} is {result}")    