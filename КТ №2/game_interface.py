import hangman_module as hm
import os


def clear_screen():

    os.system('cls' if os.name == 'nt' else 'clear')


def display_game():

    state = hm.get_game_state()
    
    clear_screen()
    print("=" * 50)
    print("         ВИСЕЛИЦА НА ПОЛЕ ЧУДЕС")
    print("=" * 50)
    
    print("\n" + state["gallows"])
    print("\nПодсказка:", state["hint"])
    print("\nСлово:", state["display_word"])
    print("\nОшибок:", state["mistakes"])
    
    if state["game_over"]:
        print("\n" + "=" * 50)
        if state["win"]:
            print(" ПОБЕДА! Вы угадали слово! ")
        else:
            print(f" ИГРА ОКОНЧЕНА! Загаданное слово: {state['secret_word']}")
        print("=" * 50)
        return False
    
    return True


def play_game():

    hm.init_game()
    
    while display_game():
        guess = input("\nВведите букву: ").strip()
        
        if not guess:
            continue
        
        result = hm.process_guess(guess[0])
        print("\n" + result["message"])
        
        if result["positions"]:
            print(f"Буква найдена на позициях: {result['positions']}")
        
        input("\nНажмите Enter для продолжения...")


def main():

    while True:
        play_game()
        
        again = input("\nХотите сыграть еще? (да/нет): ").lower()
        if again not in ['да', 'yes', 'y', 'д']:
            break
    
    print("\nСпасибо за игру!")


if __name__ == "__main__":
    main()