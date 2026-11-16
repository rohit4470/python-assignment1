# ==========================================
# 1. Use math module
# ==========================================
print("--- 1. Math Module Operations ---")
import math

num = float(input("Enter a number: "))
print("Square Root:", math.sqrt(num))
print("Power (num^2):", math.pow(num, 2))
print("Factorial (integer part):", math.factorial(int(num)))
print("Sine value:", math.sin(num))
print("Cosine value:", math.cos(num))


# ==========================================
# 2. Use random module
# ==========================================
print("\n--- 2. Random Module Operations ---")
import random

# Generate 4-digit OTP
otp = random.randint(1000, 9999)
print("Generated OTP:", otp)

# Generate random password (simple characters)
chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
password = "".join(random.choice(chars) for i in range(8))
print("Random Password:", password)

# Random list numbers
random_list = [random.randint(1, 100) for i in range(5)]
print("Random List Numbers:", random_list)


# ==========================================
# 3. Use datetime module
# ==========================================
print("\n--- 3. Datetime Module Operations ---")
import datetime

current_time = datetime.datetime.now()
print("Current Date and Time:", current_time)

# Calculate age
birth_year = int(input("Enter your birth year: "))
current_year = current_time.year
age = current_year - birth_year
print("Your calculated age is:", age, "years")


# ==========================================
# 4. Using Custom Package (geometry)
# ==========================================
print("\n--- 4. Custom Geometry Package ---")
# Package ko import karne ke liye niche wala code chalega 
# (jab aapne folder structure banaya ho)
from geometry import circle, rectangle

r = float(input("Enter radius of circle: "))
print("Circle Area:", circle.area(r))
print("Circle Perimeter/Circumference:", circle.perimeter(r))

l = float(input("Enter length of rectangle: "))
w = float(input("Enter width of rectangle: "))
print("Rectangle Area:", rectangle.area(l, w))
print("Rectangle Perimeter:", rectangle.perimeter(l, w))