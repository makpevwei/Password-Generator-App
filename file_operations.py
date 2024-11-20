def write_password_to_file(password, file_path="passwords.txt"):
    """
    Append the generated password to a text file.

    Args:
        password (str): The generated password to be saved.
        file_path (str): Path to the file where the password will be stored. 
                         Defaults to "passwords.txt".
    """
    # Open the file in append mode ('a') to add the password without overwriting existing data
    with open(file_path, "a") as file:
        file.write(password + "\n")  # Add a newline after each password


def read_passwords_from_file(file_path="passwords.txt"):
    """
    Read all passwords from the specified text file.

    Args:
        file_path (str): Path to the file where passwords are stored. 
                         Defaults to "passwords.txt".

    Returns:
        list: A list of passwords read from the file. Each password is returned as a separate string.
    """
    try:
        # Attempt to open the file in read mode ('r') to retrieve passwords
        with open(file_path, "r") as file:
            return file.readlines()  # Read all lines and return as a list
    except FileNotFoundError:
        # Return an empty list if the file does not exist
        return []
