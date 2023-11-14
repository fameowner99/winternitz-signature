import hashlib
import os

max_number_of_hashes = 256

# generate n-th hash of secret key
def generate_hash(secret_key, n = 1):
    my_hash = secret_key
    for i in range(n):
        my_hash = hashlib.sha256(str(my_hash).encode('utf-8')).hexdigest()
    return my_hash

def get_hash_byte_array(hash):
	num_of_characters = 2
	splitted_array = [hash[i:i + num_of_characters] for i in range(0, len(hash), num_of_characters)]
	return [int(numeric_string, 16) for numeric_string in splitted_array]

def check_and_create_directory(directory):
	if not os.path.exists(directory):
	    os.makedirs(directory)

def read_private_key():
	with open("keys/winternitz") as f:
		return f.read().splitlines()

def main():
	check_and_create_directory("signature")

	message = input("Enter message to sign with ./keys/winternitz key: \n")

	message_hash = generate_hash(message)
	bytes_array = get_hash_byte_array(message_hash)

	private_key_values = read_private_key()

	with open("signature/winternitz.sign", "w") as f:
		for idx, num in enumerate(bytes_array):
			f.write(generate_hash(private_key_values[idx], max_number_of_hashes - num) + "\n")

	print("Success! Signature created at ./signatur/winternitz.sign for message:\n" + message)

if __name__ == "__main__":
    main()