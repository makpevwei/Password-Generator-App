import streamlit as st
from password_generator_cli import generate_password  # Import the password generation function
from file_operations import write_password_to_file, read_passwords_from_file  # Import file operations

# Streamlit app configuration and setup
st.title("Password Generator App")  # App title displayed at the top of the page
st.write("Generate a secure password and save it to a file.")  # Description of the app

# User inputs for password preferences
# Allows the user to specify the number of letters, numbers, and symbols in the password
n_letters = st.number_input("Number of letters:", min_value=0, value=8)  # Default to 8 letters
n_numbers = st.number_input("Number of numbers:", min_value=0, value=4)  # Default to 4 numbers
n_symbols = st.number_input("Number of symbols:", min_value=0, value=4)  # Default to 4 symbols

# Button to generate the password
if st.button("Generate Password"):  
    # Generate a password based on user input
    password = generate_password(int(n_letters), int(n_numbers), int(n_symbols))
    
    # Display the generated password on the screen
    st.success(f"Generated Password: {password}")
    
    # Save the generated password to a file
    write_password_to_file(password)
    st.info("Password saved to file.")  # Notify the user that the password was saved

# Checkbox to display saved passwords
if st.checkbox("Show Saved Passwords"):  
    # Retrieve passwords stored in the file
    passwords = read_passwords_from_file()
    
    if passwords:
        st.write("Saved Passwords:")
        st.markdown("\n".join([f"- {password}" for password in passwords]))  # Bullet points for clarity
    else:
        st.warning("No passwords saved yet.")

