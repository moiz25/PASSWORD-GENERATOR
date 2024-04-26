import random
import string

def generate_password(length=12):
    # Define the characters to be used in the password
    characters = string.ascii_letters + string.digits + string.punctuation
    
    # Generate a random password using the defined characters
    password = ''.join(random.choice(characters) for _ in range(length))
    
    return password

def main():
    # Specify the length of the password (default is 12)
    password_length = 12
    
    # Generate a password
    password = generate_password(password_length)
    
    # Print the generated password
    print("Generated Password:", password)

if __name__ == "__main__":
    main()
