#Ask the user to input a password

import string

def check_password(password):
    score = 0
    
    # Length check
    if len(password) >= 8:
        score += 1
    
    # Special character check
    if any(char in string.punctuation for char in password):
        score += 1
    
    # Digit check
    if any(char in string.digits for char in password):
        score += 1
    
    # Uppercase check
    if any(char in string.ascii_uppercase for char in password):
        score += 1
    
    # Lowercase check
    if any(char in string.ascii_lowercase for char in password):
        score += 1
    
    # Final result
    if score == 5:
        print(f"Score: {score}/5 - Very strong password")
    elif score in (3, 4):
        print(f"Score: {score}/5 - Moderate password")
    elif score in (1, 2):
        print(f"Score: {score}/5 - Weak password")
    else:
        print(f"Score: {score}/5 - Very weak password")

while True:
  password = input("Enter a password to check (or type 'exit' to quit): ")
  if password.lower() == "exit":
    print("Goodbye!")
    break
  check_password(password)