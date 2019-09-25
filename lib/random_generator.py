import random
import characters as chars

def letter():
    rand_index = random.randrange(0, len(chars.alphabet))
    letter = chars.alphabet[rand_index]
    return letter


def no_space():
    rand_index = random.randrange(0, len(chars.alphabet_no_space))
    letter = chars.alphabet[rand_index]
    return letter
