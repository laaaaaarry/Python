# Import the 'random' module for generating random values
import random
# Import the 'string' module for working with string-related operations (e.g., ascii_letters, digits, punctuation)
import string

def generate_random_password(length=12):
    """
    Generate a random password of the specified length.

    Args:
    - length (int): The length of the password (default is 12).

    Returns:
    - str: The generated random password.
    """
    # Define the character set for the password (uppercase letters, lowercase letters, digits, and symbols)
    characters = string.ascii_letters + string.digits

    try:
        # Validate the password length
        if length <= 0:
            raise ValueError("Password length must be greater than 0")

        # Generate a random password using the defined character set
        password = ''.join(random.choice(characters) for _ in range(length))

        return password

    except Exception as e:
        print(f"Error: {e}")
        return None

# Usage
# Set the desired length of the random password
password_length = int(input("Enter the desired length of the password: "))

# Call the function to generate a random password
generated_password = generate_random_password(password_length)

# Display the result
if generated_password:
    print("\nGenerated Random Password:")
    print(generated_password)
else:
    print("Password generation failed.")
