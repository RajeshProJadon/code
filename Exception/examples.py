def factorial(n):
    # n! can also be defined as n * (n-1)!
    """calculate n! recursivley"""
    if n < 1:
        return 1
    else:
        print(n/0)
        return n*factorial(n-1)
try:
    print(factorial(100))
except RecursionError:
    print("This program calculate factorilas that large")
except ZeroDivisionError:
    print("Division by Zero")

print("Program Terminating")