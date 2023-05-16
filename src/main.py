from util import take_valid_int_in
from twos_complement import game as twos_complement_game

def main():
    games = {
        "2's complement": twos_complement_game
    }

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
