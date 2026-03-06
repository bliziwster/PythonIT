import hangman_module as hm


def run_game():

    hm.init_game()

    state = hm.get_game_state()

if __name__ == "__main__":
    run_game()