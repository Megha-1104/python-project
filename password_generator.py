import random
import string

def generate_password(length):
    if length < 4:
        raise ValueError("Password length should be at least 4 to include all character types.")
    
    # Define possible characters
    all_chars = string.ascii_letters + string.digits + string.punctuation
    
    # Ensure the password has at least one of each character type
    password = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
    
    # Fill the rest of the password length with random choices from all characters
    password += random.choices(all_chars, k=length - 4)
    
    # Shuffle the password list to ensure randomness
    random.shuffle(password)
    
    # Convert list to string and return
    return ''.join(password)

def main():
    # Get user input
    length = int(input("Enter the length of the password: "))
    count = int(input("Enter the number of passwords to generate: "))
    
    # Generate and display the passwords
    passwords = [generate_password(length) for _ in range(count)]
    for i, pwd in enumerate(passwords, 1):
        print(f"Password {i}: {pwd}")

if __name__ == "__main__":
    main()
