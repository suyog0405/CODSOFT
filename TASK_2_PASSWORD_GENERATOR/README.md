# Task 2 – Password Tool 🔐

This is a dual-function password utility built in Python.  
It allows users to either:

1. **Set their own password**, or  
2. **Generate a strong random password** using custom rules.


## 🔧 Features

- Option to:
  - Set a user-defined password
  - Generate a secure password with user-chosen options
- Input validation:
  - Password length must be at least 6 characters
  - Prevents generation if no character types are selected
- Random password includes:
  - Letters (uppercase + lowercase)
  - Digits
  - Symbols (if selected)


## ▶️ How to Run

Make sure Python is installed on your system.

Open terminal / command prompt, go to the folder, and run:

```bash
python password_generator.py

```

##  Sample Outputs
Case 1: Set your own password

Password Tool 🔐
1. Set your own password
2. Generate strong password
Choose (1/2): 1
Enter your password: suyog@123
Your custom password is: suyog@123

Case 2: Generate password with choices

Password Tool 🔐
1. Set your own password
2. Generate strong password
Choose (1/2): 2
Enter desired length (minimum 6): 12
Include letters? (y/n): y
Include numbers? (y/n): y
Include symbols? (y/n): y
Generated Password: q#7GvB!9xZ$1

## 💻 Technologies Used
 - Python 3.x
 - Visual Studio Code (VS Code)
 - Terminal / Command-line

