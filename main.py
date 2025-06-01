from stats import num_of_words
from stats import character_count

def main():    
    word_count = num_of_words("./books/frankenstein.txt")
    num_of_characters = character_count("./books/frankenstein.txt")

    print(word_count)
    print(num_of_characters)

main()
