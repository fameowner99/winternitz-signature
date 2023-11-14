import hashlib

def read_signature():
	 with open("signature/winternitz.sign") as f:
	 	return f.read().splitlines()

# generate n-th hash of secret key
def generate_hash(secret_key, n = 1):
    my_hash = secret_key
    for i in range(n):
        my_hash = hashlib.sha256(str(my_hash).encode('utf-8')).hexdigest()
    return my_hash

def read_public_key():
	with open("keys/winternitz.pub") as f:
		return f.read().splitlines()

def get_hash_byte_array(hash):
	num_of_characters = 2
	splitted_array = [hash[i:i + num_of_characters] for i in range(0, len(hash), num_of_characters)]
	return [int(numeric_string, 16) for numeric_string in splitted_array]

def main():
	message = input("Enter message to validate with ./signature/winternitz.sign signature: \n")

	private_key_signature = read_signature()

	message_hash = generate_hash(message)
	bytes_array = get_hash_byte_array(message_hash)

	public_key_values = read_public_key()


	hashed_private_key_signature = []
	for idx, num in enumerate(bytes_array):
		hashed_private_key_signature.append(generate_hash(private_key_signature[idx], num))

	if (hashed_private_key_signature == public_key_values):
		print("Signature signature/winternitz.sign VALID for message " + message)
	else:
		print("Signature signature/winternitz.sign NOT VALID for message " + message)

if __name__ == "__main__":
    main()