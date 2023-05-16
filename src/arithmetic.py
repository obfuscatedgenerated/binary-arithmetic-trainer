from util import take_valid_int_in
from twos_complement import int_to_2scomp_str

from random import randint

def add_game():
    print("Operands are given as positive integers with no sign bit.")
    print("Sum should be given as a positive integer with no sign bit.")
    print("Operands will never result in overflow.")
    print()

    bits = take_valid_int_in("How many bits? ", 1, None)
    print()

    while True:
        # get random ints in representable range
        # subtracting greater from the max value of the rng for smaller ensures no overflow
        greater = randint(0, (1 << bits) - 1)
        smaller = randint(0, ((1 << bits) - 1) - greater)
        sum = greater + smaller

        # convert to binary strings
        a_str = bin(greater)[2:].zfill(bits)
        b_str = bin(smaller)[2:].zfill(bits)
        sum_str = bin(sum)[2:].zfill(bits)

        # shuffle the order of the operands
        if randint(0, 1) == 0:
            a_str, b_str = b_str, a_str

        guess = input(f"What is {a_str} + {b_str} in binary? ")

        if guess == sum_str:
            print("Correct!")
        else:
            print(f"Incorrect. The answer was {sum_str}.")

def sub_game():
    print("Operands are given as positive integers with a sign bit for consistency with the difference.")
    print("Difference should be given as a 2's complement binary string, with a sign bit.")
    print("Operands will never result in underflow.")
    print()

    bits = take_valid_int_in("How many bits, including the sign bit? ", 1, None) - 1
    print()

    while True:
        # get random ints in representable range
        # subtracting a from the max value of the rng for b ensures no underflow
        a = randint(0, (1 << bits) - 1)
        b = randint(0, ((1 << bits) - 1) - a)
        diff = a - b

        # shuffle the order of the operands
        if randint(0, 1) == 0:
            a, b = b, a
            diff = -diff

        # convert to binary strings
        a_str = "0" + bin(a)[2:].zfill(bits)
        b_str = "0" + bin(b)[2:].zfill(bits)
        diff_str = int_to_2scomp_str(diff, bits + 1)

        guess = input(f"What is {a_str} - {b_str} in binary? ")

        if guess == diff_str:
            print("Correct!")
        else:
            print(f"Incorrect. The answer was {diff_str}.")
