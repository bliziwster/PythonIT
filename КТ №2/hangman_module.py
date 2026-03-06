import random
import os
from typing import List, Tuple, Dict

WORDS_FILE = "words.txt"
GALLOWS_FOLDER = "gallows"
MAX_MISTAKES = 6

game_state = {
    "secret_word": "",
    "hint": "",
    "guessed_letters": [],
    "mistakes": 0,
    "display_word": [],
    "game_over": False,
    "win": False
}


def load_words_from_file() -> List[Tuple[str, str]]:

    words_with_hints = []

    with open(WORDS_FILE, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line and '|' in line:
                word, hint = line.split('|', 1)
                words_with_hints.append((word.strip().upper(), hint.strip()))

    return words_with_hints


def load_gallows_stage(stage_number: int) -> str:

    file_path = os.path.join(GALLOWS_FOLDER, f"stage_{stage_number}.txt")
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()



def init_game() -> None:

    words_with_hints = load_words_from_file()
    word_info = random.choice(words_with_hints)
    
    game_state["secret_word"] = word_info[0]
    game_state["hint"] = word_info[1]
    game_state["guessed_letters"] = []
    game_state["mistakes"] = 0
    game_state["display_word"] = ["_"] * len(game_state["secret_word"])
    game_state["game_over"] = False
    game_state["win"] = False


def get_display_word() -> str:

    return " ".join(game_state["display_word"])


def get_hint() -> str:

    return game_state["hint"]


def get_mistakes_count() -> int:

    return game_state["mistakes"]


def is_game_over() -> bool:

    return game_state["game_over"]


def is_win() -> bool:

    return game_state["win"]


def get_gallows_display() -> str:

    return load_gallows_stage(game_state["mistakes"])


def process_guess(letter: str) -> Dict[str, any]:

    letter = letter.upper()
    result = {
        "correct": False,
        "message": "",
        "letter": letter,
        "positions": []
    }

    if letter in game_state["guessed_letters"]:
        result["message"] = f"Буква '{letter}' уже была названа"
        return result

    game_state["guessed_letters"].append(letter)

    if letter in game_state["secret_word"]:
        result["correct"] = True
        result["message"] = f"Есть буква '{letter}'!"

        for i, char in enumerate(game_state["secret_word"]):
            if char == letter:
                game_state["display_word"][i] = letter
                result["positions"].append(i + 1) 

        if "_" not in game_state["display_word"]:
            game_state["win"] = True
            game_state["game_over"] = True
            result["message"] = "Поздравляем! Вы угадали слово!"
    else:
        game_state["mistakes"] += 1
        result["message"] = f"Буквы '{letter}' нет в слове"

        if game_state["mistakes"] >= MAX_MISTAKES:
            game_state["game_over"] = True
            result["message"] = f"Игра окончена! Загаданное слово: {game_state['secret_word']}"
    
    return result


def get_game_state() -> Dict:

    return {
        "display_word": get_display_word(),
        "hint": get_hint(),
        "mistakes": game_state["mistakes"],
        "gallows": get_gallows_display(),
        "game_over": game_state["game_over"],
        "win": game_state["win"],
        "secret_word": game_state["secret_word"] if game_state["game_over"] else None
    }