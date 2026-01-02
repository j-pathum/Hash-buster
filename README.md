# Hash-Buster 🔓

A Python-based Dictionary Attack tool designed to audit password strength by attempting to crack MD5 and SHA-256 hashes.



## 🛡️ Educational Purpose
This tool demonstrates **why weak passwords are dangerous**. A simple dictionary attack can resolve unsalted hashes in milliseconds. This project highlights the importance of:
1.  Using Salted Hashes.
2.  Using long, complex passwords that aren't in common dictionaries.

## ⚡ Features
- **Auto-Detection:** Automatically identifies if a hash is MD5 or SHA-256 based on hexadecimal length.
- **Fast Lookup:** Iterates through wordlists to find matching hash signatures.
- **Clean CLI:** Simple command-line interface.

## 🚀 How to Run
1. **Prepare your Hash:**
   (Example: The MD5 hash for "dragon" is `5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8`)
   
2. **Run the Script:**
   ```bash
   python cracker.py 5e884898da28047151d0e56f8dc6292773603d0d6aabbdd62a11ef721d1542d8 common_pass.txt
