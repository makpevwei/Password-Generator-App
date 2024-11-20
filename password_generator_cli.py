import random

# Define lists of characters to use in password generation
LETTERS = [
    "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s",
    "t", "u", "v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N",
    "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"
]  # List of uppercase and lowercase English letters

NUMBERS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]  # List of numerical digits

SYMBOLS = ["!", "#", "$", "%", "&", "@", "(", ")", "*", "+"]  # List of special characters

def generate_password(n_letters, n_numbers, n_symbols):
    """
    Generate a random password based on the specified number of letters, numbers, and symbols.

    This function takes the counts of letters, numbers, and symbols and creates a randomized password 
    by selecting characters from predefined lists. The resulting password is shuffled to ensure 
    randomness in character order.

    Args:
        n_letters (int): Number of letters in the password.
        n_numbers (int): Number of numbers in the password.
        n_symbols (int): Number of symbols in the password.

    Returns:
        str: Generated password as a single string.
    """
    # Select random letters based on user input
    letter_choices = [random.choice(LETTERS) for _ in range(n_letters)]
    
    # Select random numbers based on user input
    number_choices = [random.choice(NUMBERS) for _ in range(n_numbers)]
    
    # Select random symbols based on user input
    symbol_choices = [random.choice(SYMBOLS) for _ in range(n_symbols)]
    
    # Combine all selected characters into a single list
    password_list = letter_choices + number_choices + symbol_choices

    # Shuffle the list to randomize character order
    random.shuffle(password_list)

    # Convert the list of characters into a single string
    return ''.join(password_list)
