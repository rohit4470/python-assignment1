# ==========================================
# 1. Age Validation System
# ==========================================
print("--- 1. Age Validation System ---")
try:
    age = int(input("Enter your age: "))
    if age < 18:
        # Raising custom exception using ValueError
        raise ValueError("Age must be 18 or above to register.")
    else:
        print("Age verified successfully! Access granted.")
except ValueError as e:
    print("Error:", e)


# ==========================================
# 2. Bank Withdrawal System
# ==========================================
print("\n--- 2. Bank Withdrawal System ---")
balance = 5000  # Initial account balance
print("Current Account Balance: ₹", balance)

try:
    withdrawal = float(input("Enter amount to withdraw: ₹"))
    if withdrawal > balance:
        raise ValueError("Insufficient balance! Withdrawal amount exceeds current balance.")
    else:
        balance = balance - withdrawal
        print("Withdrawal successful! Remaining balance: ₹", balance)
except ValueError as e:
    print("Transaction Failed: Error:", e)


# ==========================================
# 3. Password Validator
# ==========================================
print("\n--- 3. Password Validator ---")
password = input("Enter a password to validate: ")

try:
    # Check length < 8
    if len(password) < 8:
        raise Exception("Password must be at least 8 characters long.")
    
    # Check uppercase
    has_upper = False
    for char in password:
        if "A" <= char <= "Z":
            has_upper = True
            break
    if not has_upper:
        raise Exception("Password must contain at least one uppercase letter.")
        
    # Check number
    has_number = False
    for char in password:
        if "0" <= char <= "9":
            has_number = True
            break
    if not has_number:
        raise Exception("Password must contain at least one number.")
        
    print("Password is strong and valid!")
    
except Exception as e:
    print("Validation Error:", e)