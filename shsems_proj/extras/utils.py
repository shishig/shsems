import os
from random import randint

def generate_random_string(size = 6):
    alpha = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    str = ""
    for i in range(size):
        str += alpha[randint(0,51)]
    
    return str