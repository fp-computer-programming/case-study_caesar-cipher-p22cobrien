# Author: CMOB 4/25/2022

# Imports
from string import ascii_uppercase


# Functions
def cipher_key(shift):
    original_letters = ascii_uppercase
    shifted_letters = ascii_uppercase[int(shift):] + ascii_uppercase[:int(shift)]

    return dict(zip(original_letters, shifted_letters))


def shift_line(line, dict_key):
    new_line = ""
    # Add code here
    for character in line:
        
    return new_line


def encrypt_message(filename, dict_key):
    # Add code here
    with open(filename)
    content = open.filename
    for line in content:
        outfile.write(shift_line(line,dict_key))


# Main
user_file = input("Please enter a file to be encrypted: ")
shift_value = input("Please enter a shift value: ")

key = cipher_key(shift_value)

encrypt_message(user_file, key)
