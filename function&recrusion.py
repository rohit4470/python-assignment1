# ==========================================
# 1. Factorial Using Loop
# ==========================================
print("--- 1. Factorial Using Loop ---")
def calculate_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact

num = int(input("Enter a number to find factorial: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    result = calculate_factorial(num)
    print("Factorial of", num, "is:", result)


# ==========================================
# 2. Sum of First N Natural Numbers Recursively
# ==========================================
print("\n--- 2. Sum of Natural Numbers (Recursion) ---")
def sum_natural(n):
    # Base condition
    if n == 1:
        return 1
    else:
        return n + sum_natural(n - 1)

n_val = int(input("Enter value of n: "))
if n_val <= 0:
    print("Please enter a positive integer.")
else:
    ans = sum_natural(n_val)
    print("Sum of first", n_val, "natural numbers is:", ans)


# ==========================================
# 3. Print a String in Reverse Using Recursion
# ==========================================
print("\n--- 3. Reverse String Using Recursion ---")
def reverse_string(s):
    # Base condition: if string is empty or has 1 char
    if len(s) == 0:
        return s
    else:
        # Take last character + reverse of remaining string
        return s[-1] + reverse_string(s[:-1])

text = input("Enter a string: ")
rev_text = reverse_string(text)
print("Reversed string is:", rev_text)


# ==========================================
# 4. Find Power of a Number (x^n) Using Recursion
# ==========================================
print("\n--- 4. Power of a Number (x^n) Using Recursion ---")
def power(base, exp):
    # Base condition: anything raised to power 0 is 1
    if exp == 0:
        return 1
    else:
        return base * power(base, exp - 1)

x = int(input("Enter base (x): "))
n = int(input("Enter exponent (n): "))

if n < 0:
    print("This simple recursion supports positive exponents only.")
else:
    output = power(x, n)
    print(x, "raised to the power", n, "is:", output)