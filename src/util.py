from typing import Union

def take_valid_float_in(prompt: str, min: Union[int, float, None], max: Union[int, float, None]) -> float:
    """Takes a valid float number in the range [min, max].

    Args:
        prompt (str): The prompt to display.
        min (int | float | None): The minimum value. None for no minimum.
        max (int | float | None): The maximum value. None for no maximum.

    Returns:
        float: The valid number.
    """

    if min is not None and max is not None and min > max:
        raise ValueError("min must be less than or equal to max")

    while True:
        try:
            n = float(input(prompt))
        except ValueError:
            print("Invalid number.")
            continue

        if min is not None and n < min:
            print(f"Must be at least {min}.")
            continue
            
        if max is not None and n > max:
            print(f"Must be at most {max}.")
            continue

        return n
    

def take_valid_int_in(prompt: str, min: Union[int, None], max: Union[int, None]) -> int:
    """Takes a valid integer number in the range [min, max].

    Args:
        prompt (str): The prompt to display.
        min (int | None): The minimum value. None for no minimum.
        max (int | None): The maximum value. None for no maximum.

    Returns:
        int: The valid number.
    """

    while True:
        num = take_valid_float_in(prompt, min, max)

        if num.is_integer():
            return int(num)
        else:
            print("Must be an integer.")
            continue


def take_bool_in(prompt: str):
    """Takes a yes or no input.

    Args:
        prompt (str): The prompt to display.

    Returns:
        bool: The boolean value.
    """

    while True:
        try:
            s = input(prompt)
        except ValueError:
            print("Invalid input.")
            continue

        if s.lower() == "y":
            return True
        elif s.lower() == "n":
            return False
        else:
            print("Invalid input.")
            continue
