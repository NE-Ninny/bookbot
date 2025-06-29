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
    character_dict = {
        "a": 0, "b": 0, "c": 0, "d": 0, "e": 0,
        "f": 0, "g": 0, "h": 0, "i": 0, "j": 0,
        "k": 0, "l": 0, "m": 0, "n": 0, "o": 0,
        "p": 0, "q": 0, "r": 0, "s": 0, "t": 0,
        "u": 0, "v": 0, "w": 0, "x": 0, "y": 0,
        "z": 0, " ": 0
    }
    
    for character in lower_case_text:
        if character in character_dict:
            character_dict[character] += 1
    
    return character_dict

def sorted_char(dict):
    sorted_list = []
    
    for char in dict:
        char_dict = {char}
        num_dict = {dict[char]}
        
        print(char_dict, num_dict)

