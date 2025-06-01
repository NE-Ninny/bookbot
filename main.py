from stats import num_of_words
from stats import character_count

# def get_book_text(filepath):
#     with open(filepath) as f:
#         file_contents = f.read()
        
#         return file_contents

# def num_of_words(filepath):
#     word_count = 0
#     book_text = get_book_text(filepath)
    
#     for words in book_text.split():
#         word_count += 1

#     # print(f"Word count: {word_count}")
#     return f"{word_count} words found in the document"

def main():    
    word_count = num_of_words("./books/frankenstein.txt")
    num_of_characters = character_count("./books/frankenstein.txt")

    print(word_count)
    print(num_of_characters)

main()
