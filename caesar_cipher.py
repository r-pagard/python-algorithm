""" 
A kind of cipher algorithm.
    
    Functions:
        find_index: find the index of a given `char` in the given `string`.
        encrypt: Encrypting the given data with a key provided by the function.
        decrypt: Decrypting the given data with reversing the key provied by the function.
        brute_force: A function for the Brute Force attack by testing 52 steps from 1-52.
"""

from string import ascii_letters


ALPHA = ascii_letters

def find_index(string: str, char: str) -> int:
    """
    I don't want to use `.index` method in Python strings, 
    then I wrote this to underestand how `.index.` works.
    """

    for ch in range(0, len(string)):
        if string[ch] == char:
            return ch
    return "Your index not found in this string."

def encrypt(data: str, key: int) -> int:
    """
    The encrypting function.

    Attributes:
        data(str): The string will be encrypted.
        key(int): The step(shift).
    """
    result = ''

    for char in data:
        if char not in ALPHA:
            result += char
        else:
            alpha_key = (find_index(ALPHA, char) + key) % len(ALPHA)
            # you can use `alpha.index(char)` instead of `find_index(ALPHA, char)` to use Python abilities.
            result += ALPHA[alpha_key]
    return result


def decrypt(data: str, key: int) -> str:
    """
    The decrypting function.

    Attributes:
        data(str): The encrypted string that will be decrypted.
        key(str): The step(shift).
    """

    # Reverse the key to decrypt the data
    key *= -1
    # Return decrypted function with a new key(reversed key)
    return encrypt(data=data, key=key)

def brute_force(data):
    """
    The brute force function for find the decrypted string from 1-52 steps.
    """
    brute_force_data = {}

    for step in range(1, len(ALPHA)+1):
        # Call decrypt function for test 52 steps on it
        brute_force_data[step] = decrypt(data, step)

    return brute_force_data
