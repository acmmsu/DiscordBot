"""
By Anthony Eid
Date: 10/20/2022

File is responsible for encryption functions.
"""


from math import ceil, floor, sqrt
from typing import List

def encrypt_basic(string: str) -> str:
    """Encrypt a given string

    Args:
        string (str): The string to encrypt

    Returns:
        str: The encrypted version of the given string.
    """
    
    # Get variables for size of encryption matrix
    str_sqrt: float = sqrt(len(string))
    str_flr: int  = floor(str_sqrt)
    str_ceil: int = ceil(str_sqrt)
    
    # Increase encryption matrix size if it can't hold string
    while str_flr * str_ceil < len(string):
        if str_flr == min(str_flr, str_ceil):
            str_flr += 1
        else:
            str_ceil += 1
    
    matrix: List[List[str]]  = [[''] * str_flr for i in range(str_ceil)]
    
    # fill matrix 
    for i in range(str_flr):
        for j in range(str_ceil):
            str_ind = j + i * str_ceil
            if str_ind <= len(string) - 1:
                matrix[i][j] =  string[j + (i * str_ceil)]
    
    # fill encrypted array
    encrypted_chars = []
    for i in range(str_flr):
        for j in range(str_ceil):
            encrypted_chars.append(matrix[j][i])
          
    # return encrypted string  
    return "".join(encrypted_chars)
    
    
    
def decrypt_basic(string: str) -> str:
    """Decrypt a given decrypted string.

    Args:
        string (str): The string to decrypt

    Returns:
        str: The decrypted version of the given string
    """
    # Get variables for decryption matrix size
    str_len = len(string)
    sqrt_ceil = ceil(sqrt(str_len))
    sqrt_flr = floor(sqrt(str_len))
    
    # Increase decryption matrix size if it can't hold whole string
    while sqrt_flr * sqrt_ceil < str_len:
        if sqrt_flr == min(sqrt_flr, sqrt_ceil):
            sqrt_flr += 1
        else:
            sqrt_ceil += 1
 
    matrix: List[List[str]] = [[' '] * sqrt_flr for j in range(sqrt_ceil)]
    str_idx: int = 0
 
    # Fill the matrix column-wise
    for j in range(sqrt_ceil):
        for i in range(sqrt_flr):
            if (str_idx < str_len):
                matrix[j][i] = string[str_idx]
            str_idx += 1
            
    # Decrypt string 
    decrypt = []
    for i in range(sqrt_flr):
        for j in range(sqrt_ceil):
            if str_len > 0:
                decrypt.append(matrix[j][i])
                str_len -= 1
            else:
                break
       
    # Return decrypted string         
    return "".join(decrypt)
