from util import take_valid_int_in, take_valid_float_in, take_bool_in
from twos_complement import int_to_2scomp_str, twoscomp_str_to_int

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

    # get the integer part
    i = int(n)

    # get the fractional part
    f = n - i

    # convert the integer part to binary
    i_str = int_to_2scomp_str(i, m_bits)

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


def normalised_floating_point_to_float(s: str, e_bits: int) -> float:
    """Converts a normalised floating point binary string to a float.

    Args:
        s (str): The binary string.
        e_bits (int): The number of bits at the end used for the exponent.

    Returns:
        float: The float.
    """

    if e_bits < 1:
        raise ValueError("e_bits must be greater than or equal to 0")
    
    if e_bits >= len(s) - 1:
        raise ValueError("e_bits too large")

    # split the string into the mantissa and exponent
    m = s[:-e_bits]
    e = s[-e_bits:]

    if m == "":
        raise ValueError("s is not a normalised floating point binary string")

    if e == "":
        e = "0"

    # normalised if first 2 bits are 10 or 01
    positive_head_idx = m.find("01")
    negative_head_idx = m.find("10")

    if positive_head_idx == 0 and negative_head_idx == 0:
        raise ValueError("s is not a normalised floating point binary string")

    is_negative = negative_head_idx == 0

    # get the exponent (from sign bit to the end, since it is normalised)
    # it is normalised, so each value past the sign bit is a fractional bit
    if is_negative:
        m_int = -1
    else:
        m_int = 0
    
    for i in range(1, len(m)):
        # if the bit is 1, add 2^-i to the result
        if m[i] == "1":
            m_int += 2 ** -i
    
    # convert the exponent to an integer
    e_int = twoscomp_str_to_int(e)

    # result is m_int * 2^e_int
    return m_int * 2 ** e_int


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


def flp_game():
    m_bits = take_valid_int_in("How many bits for the mantissa including sign bit? ", 2, None)
    e_bits = take_valid_int_in("How many bits for the exponent? ", 1, None)
    allow_negative_mantissa = take_bool_in("Allow negative mantissa? (y/n) ")
    allow_negative_exponent = take_bool_in("Allow negative exponent? (y/n) ")
    print("Right now, you can only guess denary.")
    print()
    # sometimes you get some super cruel numbers! the bits selection only covers the question, not the converted fixed point number
    # TODO: perhaps add an option to limit the range of the exponent separately to prevent this?

    while True:
        # generate random sequence of 1s and 0s, where the first 2 bits are always 01 (positive) or 10 (if negative allowed)
        
        # build the sign bit
        s = ""
        if allow_negative_mantissa and randint(0, 1) == 1:
            s += "1"
        else:
            s += "0"
        
        # complete the first 2 bits to a normalised pair (01/10)
        s += str(1 - int(s[0]))

        # finish the mantissa
        for i in range(m_bits - 2):
            s += str(randint(0, 1))
        
        # build the exponent's sign bit
        if allow_negative_exponent and randint(0, 1) == 1:
            s += "1"
        else:
            s += "0"
        
        # finish the exponent
        for i in range(e_bits - 1):
            s += str(randint(0, 1))
        
        # get the denary value
        n = normalised_floating_point_to_float(s, e_bits)

        guess = take_valid_float_in(f"What is {s} in denary? ", None, None)
        if guess == n:
            print("Correct!")
        else:
            print(f"Incorrect. The answer was {n}.")
