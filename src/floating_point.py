from util import take_valid_int_in, take_valid_float_in, take_bool_in

from random import randint


def float_to_fixed_point_str(n: float, m_bits: int, f_bits: int) -> str:
    """Converts a float to a fixed point binary string.

    Args:
        n (float): The float to convert.
        m_bits (int): The number of bits to use for the mantissa.
        f_bits (int): The number of bits to use for the fractional.

    Returns:
        str: The fixed point binary string.
    """

    if m_bits < 1:
        raise ValueError("m_bits must be greater than 0")
    
    if f_bits < 1:
        raise ValueError("f_bits must be greater than 0")

    if n < 0:
        raise ValueError("n must be positive")

    # get the integer part
    i = int(n)

    # get the fractional part
    f = n - i

    # convert the integer part to binary
    i_str = bin(i)[2:].zfill(m_bits)

    # convert the fractional part to binary
    f_str = ""
    for j in range(f_bits):
        # multiply the fractional part by 2
        f *= 2

        # if the result is greater than or equal to 1, subtract 1 and add a 1 to the string
        if f >= 1:
            f -= 1
            f_str += "1"
        # otherwise, add a 0 to the string
        else:
            f_str += "0"

    return i_str + f_str



def fip_game():
    m_bits = take_valid_int_in("How many bits for the mantissa? ", 1, None)
    f_bits = take_valid_int_in("How many bits for the fractional? ", 1, None)
    guess_denary = take_bool_in("Guess denary? (y/n) ")

    while True:
        # generate a random denary mantissa within the representable range (fixed point)
        n = randint(0, (1 << m_bits) - 1)

        # generate a random denary fractional within the representable range (fixed point, i.e. 1111 = 0.5 + 0.25 + 0.125 + 0.0625 = 0.9375)
        for i in range(f_bits):
            # randomly choose to add 2^-(i+1) to the number
            # TODO: perhaps more efficient using binary and bitshifting
            if randint(0, 1):
                n += 2 ** -(i + 1)

        # get fixed point string
        s = float_to_fixed_point_str(n, m_bits, f_bits)

        if guess_denary:
            guess = take_valid_float_in(f"What is {s} in denary? ", None, None)
            if guess == n:
                print("Correct!")
            else:
                print(f"Incorrect. The answer was {n}.")
        else:
            guess = input(f"What is {n} in fixed point? ")
            if guess == s:
                print("Correct!")
            else:
                print(f"Incorrect. The answer was {s}.")



def flp_positive_only_game():
    pass

def flp_with_2s_comp_game():
    pass
