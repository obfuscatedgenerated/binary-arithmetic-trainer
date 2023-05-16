from util import take_valid_int_in, take_bool_in

from random import randint

def int_to_2scomp_str(n: int, bits: int) -> str:
    """Converts an integer to a 2's complement binary string.

    Args:
        n (int): The integer to convert.
        bits (int): The number of bits to use.

    Returns:
        str: The 2's complement binary string.
    """

    if bits < 1:
        raise ValueError("bits must be greater than 0")
    
    if n < 0:
        n = (1 << bits) + n

    return bin(n)[2:].zfill(bits)


def tc_game():
    bits = take_valid_int_in("How many bits? ", 1, None)
    guess_denary = take_bool_in("Guess denary? (y/n) ")
    print()

    while True:
        # get random int in representable range
        n = randint(-(1 << (bits - 1)), (1 << (bits - 1)) - 1)

        # get 2's complement string
        s = int_to_2scomp_str(n, bits)

        if guess_denary:
            guess = take_valid_int_in(f"What is {s} in denary? ", None, None)
            if guess == n:
                print("Correct!")
            else:
                print(f"Incorrect. The answer was {n}.")
        else:
            guess = input(f"What is {n} in 2's complement? ")
            if guess == s:
                print("Correct!")
            else:
                print(f"Incorrect. The answer was {s}.")
