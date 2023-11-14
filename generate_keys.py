import hashlib
import os
import sys
import random

number_of_values_in_key = 32
number_of_hashes_for_public_key = 256

# generate n-th hash of secret key
def generate_hash(secret_key, n = 1):
    my_hash = secret_key
    for i in range(n):
        my_hash = hashlib.sha256(str(my_hash).encode('utf-8')).hexdigest()
    return my_hash

def check_and_create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def main():
    # create directory keys if not exist
    check_and_create_directory("keys")

    private_key_file = open("keys/winternitz", "w")
    public_key_file = open("keys/winternitz.pub", "w")

    for i in range(number_of_values_in_key):
        random_number = random.randint(0,sys.maxsize)
        private_number = generate_hash(random_number)
        public_number = generate_hash(private_number, number_of_hashes_for_public_key)

        private_key_file.write(private_number + "\n")
        public_key_file.write(public_number + "\n")


    private_key_file.close()
    public_key_file.close()

    print("Success! Keys were created\n\nPrivate - at ./keys/winternitz\nPublic - at ./keys/winternitz.pub")

if __name__ == "__main__":
    main()