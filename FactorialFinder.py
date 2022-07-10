# Factorial Finder
#  The Factorial of a positive integer, n, is defined as the product of the sequence
#  n, n-1, n-2, ...1 and the factorial of zero, 0, is defined as being 1. 
# Solve this using both loops and recursion.

def factorial(n):
    if n == 0:
        return 1
    
    elif n > 0:
        result *= n
        n -= -1
        return result

def factorialRecursion(n):
    if n == 0:
        return 1
    
    elif n > 0:
        return n * factorialRecursion(n-1)

def main():
    result = factorial(5)
    print(f"{result} is the result when passed through loops")
   
    result2 = factorialRecursion(5)
    print(f"{result2} is the result when passed through recursion")

if __name__ == "__main__":
    main()