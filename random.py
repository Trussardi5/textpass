import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def save_password_to_file(password, file_name):
    with open(file_name, 'w') as file:
        file.write(f'Randomly generated password: {password}')

if __name__ == "__main__":
    password_length = 16  # You can change the password length here
    generated_password = generate_random_password(password_length)
    file_name = "random_password.txt"

    save_password_to_file(generated_password, file_name)
    print(f"Random password generated and saved to '{file_name}'.")
