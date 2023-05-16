from util import take_valid_int_in

from twos_complement import tc_game
from arithmetic import add_game, sub_game
from floating_point import fip_game, flp_game

def main():
    games = {
        "2's complement (to/from denary)": tc_game,
        "Addition of integers": add_game,
        "Subtraction of integers": sub_game,
        "Fixed point (to/from denary)": fip_game,
        "Floating point (to/from denary)": flp_game,
    }

    # TODO: normalisation game
    # TODO: floating point addition and subtraction games (normalise both then add/subtract)

    game_names = list(games.keys())
    game_funcs = list(games.values())

    print("=====================================")
    print("Available games:\n")

    for i, name in enumerate(game_names):
        print(f"{i + 1}. {name}")
    
    print("=====================================\n")

    index = take_valid_int_in("Select a number and press return: ", 1, len(game_funcs)) - 1
    print()
    game_funcs[index]()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        # stop vomiting every time the user exits
        print("\n\nExiting...")
        exit(0)
