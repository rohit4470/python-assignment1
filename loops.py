# ==========================================
# 1. Automorphic Number
# ==========================================
print("--- 1. Automorphic Number ---")
num = int(input("Enter a number: "))
temp = num
square = num * num
count = 0

# Count digits in number
while temp > 0:
    count = count + 1
    temp = temp // 10

# Extract last digits equal to count
divisor = 10 ** count
last_digits = square % divisor

if last_digits == num:
    print(num, "is an Automorphic Number (Square:", square, ")")
else:
    print(num, "is NOT an Automorphic Number (Square:", square, ")")


# ==========================================
# 2. Palindrome Number Series
# ==========================================
print("\n--- 2. Palindrome Number Series ---")
start = int(input("Enter start range: "))
end = int(input("Enter end range: "))

print("Palindrome numbers between", start, "and", end, "are:")
for n in range(start, end + 1):
    temp = n
    rev = 0
    while temp > 0:
        digit = temp % 10
        rev = rev * 10 + digit
        temp = temp // 10
    if n == rev:
        print(n, end=" ")
print()


# ==========================================
# 3. LCM & HCF Using Loops
# ==========================================
print("\n--- 3. LCM & HCF ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

# Find HCF using Euclidean algorithm with loop
x = a
y = b
while y != 0:
    temp = y
    y = x % y
    x = temp
hcf = x

# Find LCM using formula: (a * b) / HCF
lcm = (a * b) // hcf

print("HCF is:", hcf)
print("LCM is:", lcm)


# ==========================================
# 4. Password Retry System
# ==========================================
print("\n--- 4. Password Retry System ---")
correct_password = "python123"
attempts = 3

while attempts > 0:
    pwd = input("Enter password: ")
    if pwd == correct_password:
        print("Login Successful!")
        break
    else:
        attempts = attempts - 1
        print("Incorrect password. Attempts left:", attempts)

if attempts == 0:
    print("Account Blocked due to 3 failed attempts!")


# ==========================================
# 5. Star Patterns
# ==========================================
print("\n--- 5. Star Patterns ---")
rows = int(input("Enter number of rows for triangle: "))

print("\nTriangle Pattern:")
for i in range(1, rows + 1):
    for j in range(1, i + 1):
        print("*", end="")
    print()

print("\nPyramid Pattern:")
for i in range(1, rows + 1):
    # Print spaces
    for j in range(rows - i):
        print(" ", end="")
    # Print stars
    for k in range(2 * i - 1):
        print("*", end="")
    print()