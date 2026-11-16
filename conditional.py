# ==========================================
# 1. Electricity Bill Calculator
# ==========================================
print("--- 1. Electricity Bill Calculator ---")
units = float(input("Enter units consumed: "))

if units <= 100:
    bill = units * 5
elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)
else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

if bill > 2000:
    bill = bill + (bill * 5 / 100)  # 5% surcharge add kiya

print("Total Bill amount: ₹", bill)


# ==========================================
# 2. Loan Approval System
# ==========================================
print("\n--- 2. Loan Approval System ---")
salary = float(input("Enter monthly salary: "))
credit = int(input("Enter credit score: "))
age = int(input("Enter age: "))

if age >= 21 and age <= 60:
    if salary >= 30000 and credit >= 700:
        print("Loan Status: Approved")
    elif salary >= 30000 or credit >= 700:
        print("Loan Status: Conditionally Approved")
    else:
        print("Loan Status: Rejected")
else:
    print("Loan Status: Rejected (Age not in range 21-60)")


# ==========================================
# 3. Number Classification
# ==========================================
print("\n--- 3. Number Classification ---")
num = int(input("Enter an integer: "))

# Positive, Negative or Zero
if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")

# Even or Odd
if num % 2 == 0:
    print("Number is Even")
else:
    print("Number is Odd")

# Divisible by 3 and 5
if num % 3 == 0 and num % 5 == 0:
    print("Number is divisible by both 3 and 5")
else:
    print("Number is NOT divisible by both 3 and 5")


# ==========================================
# 4. Exam Result Analyzer
# ==========================================
print("\n--- 4. Exam Result Analyzer ---")
m1 = float(input("Enter marks of subject 1: "))
m2 = float(input("Enter marks of subject 2: "))
m3 = float(input("Enter marks of subject 3: "))
m4 = float(input("Enter marks of subject 4: "))
m5 = float(input("Enter marks of subject 5: "))

# Check if failed in any subject (< 33)
if m1 < 33 or m2 < 33 or m3 < 33 or m4 < 33 or m5 < 33:
    print("Result: Fail (Scored less than 33 in one or more subjects)")
else:
    total = m1 + m2 + m3 + m4 + m5
    percentage = (total / 500) * 100
    print("Total Marks:", total, "/ 500")
    print("Percentage:", percentage, "%")
    
    if percentage >= 60:
        print("Division: First Division")
    elif percentage >= 50:
        print("Division: Second Division")
    elif percentage >= 40:
        print("Division: Third Division")
    else:
        print("Result: Fail (Percentage below 40%)")