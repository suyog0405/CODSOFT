import random
import string

def create_password(length, use_letters, use_numbers, use_symbols):
    chars = ''
    if use_letters:
        chars += string.ascii_letters
    if use_numbers:
        chars += string.digits
    if use_symbols:
        chars += string.punctuation

    if not chars:
        return "Error: No character types selected."

    return ''.join(random.choice(chars) for _ in range(length))


# Start
print("Password Tool ")
print("1. Set your own password")
print("2. Generate strong password")

choice = input("Choose (1/2): ")

if choice == '1':
    user_password = input("Enter your password: ")
    if len(user_password) < 6:
        print("Warning: Password too short. Use at least 6 characters.")
    else:
        print("Your custom password is:", user_password)

elif choice == '2':
    # Get length
    while True:
        length = input("Enter desired length (minimum 6): ")
        if length.isdigit() and int(length) >= 6:
            length = int(length)
            break
        else:
            print("Please enter a valid number (6 or more).")

    # Character options
    use_letters = input("Include letters? (y/n): ").lower() == 'y'
    use_numbers = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

    # Generate password
    result = create_password(length, use_letters, use_numbers, use_symbols)
    print("Generated Password:", result)

else:
    print("Invalid choice. Please select 1 or 2.")
