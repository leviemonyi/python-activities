def is_palindrome(s):
    # Remove any spaces and convert to lowercase for comparison
    s = s.replace(" ", "").lower()
    # Check if the string is the same forwards and backwards
    return s == s[::-1]

# Input: Get a string from the user
user_input = input("Enter a string: ")

# Check if the string is a palindrome
if is_palindrome(user_input):
    print(f"'{user_input}' is a palindrome!")
else:
    print(f"'{user_input}' is not a palindrome.")
