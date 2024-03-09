# Import the 'hashlib' module for hashing functions
import hashlib

def calculate_file_hash(file_path, algorithm='md5'):
    """
    Calculate the hash value of a file using the specified algorithm.

    Args:
    - file_path (str): The path to the file.
    - algorithm (str): The hash algorithm to use (default is 'md5').

    Returns:
    - str: The calculated hash value.
    """
    try:
        # Validate the chosen algorithm
        if algorithm not in ('md5', 'sha256'):
            raise ValueError("Invalid algorithm. Supported algorithms: md5, sha256")

        # Create a hash object for the chosen algorithm
        hash_object = hashlib.new(algorithm)

        # Open the file and read it in chunks for efficiency
        with open(file_path, 'rb') as file:
            for chunk in iter(lambda: file.read(4096), b''):
                hash_object.update(chunk)

        # Get the hexadecimal representation of the hash
        return hash_object.hexdigest()

    except Exception as e:
        print(f"Error: {e}")
        return None

# Usage
file_path = input("Enter the path to the file: ")
chosen_algorithm = input("Choose hash algorithm (md5/sha256): ")

hash_value = calculate_file_hash(file_path, chosen_algorithm)

if hash_value:
    print(f"\n{chosen_algorithm.upper()} Hash Value:")
    print(hash_value)
else:
    print("File hashing failed.")
