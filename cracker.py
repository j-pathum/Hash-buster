import hashlib
import sys
import time

def crack_hash(target_hash, wordlist_file):
    print(f"--- Starting Hash-Buster ---")
    print(f"Target: {target_hash}")
    
    # 1. Detect Hash Type (Basic Heuristic based on length)
    if len(target_hash) == 32:
        hash_type = "md5"
    elif len(target_hash) == 64:
        hash_type = "sha256"
    else:
        print("Error: Unknown hash type. Only MD5 (32 chars) and SHA256 (64 chars) supported.")
        return

    print(f"Detected Type: {hash_type.upper()}")
    print(f"Loading wordlist: {wordlist_file}...")

    try:
        # 2. Open the wordlist file
        with open(wordlist_file, 'r', encoding='utf-8') as file:
            start_time = time.time()
            count = 0
            
            # 3. Loop through every word in the dictionary
            for line in file:
                word = line.strip()
                count += 1
                
                # 4. Hash the current word
                if hash_type == "md5":
                    # Encode word to bytes, then hash
                    hashed_word = hashlib.md5(word.encode('utf-8')).hexdigest()
                elif hash_type == "sha256":
                    hashed_word = hashlib.sha256(word.encode('utf-8')).hexdigest()

                # 5. Compare our hashed word to the target
                if hashed_word == target_hash:
                    end_time = time.time()
                    print(f"\n[+] PASSWORD CRACKED!")
                    print(f"Password: {word}")
                    print(f"Attempts: {count}")
                    print(f"Time: {end_time - start_time:.4f} seconds")
                    return

            print(f"\n[-] Password not found in wordlist.")

    except FileNotFoundError:
        print("Error: Wordlist file not found.")

if __name__ == "__main__":
    # Allow running from CLI with arguments
    if len(sys.argv) == 3:
        crack_hash(sys.argv[1], sys.argv[2])
    else:
        # Or prompt user if no arguments given
        target = input("Enter the hash to crack: ").strip()
        wordlist = "common_pass.txt" 
        crack_hash(target, wordlist)
