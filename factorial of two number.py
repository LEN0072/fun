def factorial_iterative(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result


num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

fact1 = factorial_iterative(num1)
fact2 = factorial_iterative(num2)

print(f"The factorial of {num1} is: {fact1}")
print(f"The factorial of {num2} is: {fact2}")
