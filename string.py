# ==========================================
# 1. Palindrome String Check
# ==========================================
print("--- 1. Palindrome String Check ---")
text = input("Enter a string: ")

# Convert to lowercase and remove spaces manually
clean_str = ""
for char in text:
    if char != " ":
        if "A" <= char <= "Z":
            # Convert uppercase to lowercase using ASCII
            clean_str = clean_str + chr(ord(char) + 32)
        else:
            clean_str = clean_str + char

# Reverse the string
rev_str = ""
for i in range(len(clean_str) - 1, -1, -1):
    rev_str = rev_str + clean_str[i]

if clean_str == rev_str:
    print('"', text, '" is a Palindrome String.')
else:
    print('"', text, '" is NOT a Palindrome String.')


# ==========================================
# 2. Find the Longest Word in a Sentence
# ==========================================
print("\n--- 2. Longest Word in a Sentence ---")
sentence = input("Enter a sentence: ")

words = sentence.split()
longest = ""

for w in words:
    if len(w) > len(longest):
        longest = w

print("The longest word is:", longest, "(Length:", len(longest), "characters)")


# ==========================================
# 3. Check Two Strings are Anagrams
# ==========================================
print("\n--- 3. Anagram Check ---")
str1 = input("Enter first string: ").lower()
str2 = input("Enter second string: ").lower()

# Sort characters and compare
if sorted(str1) == sorted(str2):
    print("The strings are Anagrams.")
else:
    print("The strings are NOT Anagrams.")


# ==========================================
# 4. Remove Duplicate Characters from a String
# ==========================================
print("\n--- 4. Remove Duplicate Characters ---")
s = input("Enter a string: ")
result = ""

for char in s:
    if char not in result:
        result = result + char

print("String after removing duplicates:", result)


# ==========================================
# 5. Compress String ("aaabbc" -> "a3b2c1")
# ==========================================
print("\n--- 5. Compress String ---")
s = input("Enter a string to compress (e.g., aaabbc): ")

if len(s) == 0:
    print("Empty string!")
else:
    compressed = ""
    count = 1
    
    for i in range(len(s)):
        # Check if next character is same
        if i + 1 < len(s) and s[i] == s[i + 1]:
            count = count + 1
        else:
            compressed = compressed + s[i] + str(count)
            count = 1
            
    print("Compressed String:", compressed)