def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
        return file_contents

def num_of_words(filepath):
    word_count = 0
    book_text = get_book_text(filepath)
    
    for words in book_text.split():
        word_count += 1
	
    return f"Found {word_count} total words"

def character_count(filepath):
    lower_case_text = get_book_text(filepath).lower()
    # character_dict = {
    #     "a": 0, "b": 0, "c": 0, "d": 0, "e": 0,
    #     "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
    #     "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
    #     "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
    #     "u": 0, "v": 0, "w": 0, "x": 0, "y": 0,
    #     "z": 0, " ": 0
    # }
    character_dict = {
        "a", "b", "c", "d", "e",
        "f", "g", "h", "i", "j",
        "k", "l", "m", "n", "o",
        "p", "q", "r", "s", "t",
        "u", "v", "w", "x", "y",
        "z"
    }

    character_list = [
        {"char": "a", "num": 0},
        {"char": "b", "num": 0},
        {"char": "c", "num": 0},
        {"char": "d", "num": 0},
        {"char": "e", "num": 0},
        {"char": "f", "num": 0},
        {"char": "g", "num": 0},
        {"char": "h", "num": 0},
        {"char": "i", "num": 0},
        {"char": "j", "num": 0},
        {"char": "k", "num": 0},
        {"char": "l", "num": 0},
        {"char": "m", "num": 0},
        {"char": "n", "num": 0},
        {"char": "o", "num": 0},
        {"char": "p", "num": 0},
        {"char": "q", "num": 0},
        {"char": "r", "num": 0},
        {"char": "s", "num": 0},
        {"char": "t", "num": 0},
        {"char": "u", "num": 0},
        {"char": "v", "num": 0},
        {"char": "w", "num": 0},
        {"char": "x", "num": 0},
        {"char": "y", "num": 0},
        {"char": "z", "num": 0}
    ]

    for dict in character_list:
        current_char = dict["char"]
        current_num = dict["num"]

        # if current_char in character_list:
        #     print(current_char) 

        # if dict in character_dict:
        #     print(dict)
        
        print(f"{current_char}: {current_num}")