from stats import num_of_words
from stats import character_count
from stats import sorted_char

def main():    
    word_count = num_of_words("./books/frankenstein.txt")
    num_of_characters = character_count("./books/frankenstein.txt")

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    print(sorted_char(character_count("./books/frankenstein.txt")))
    print("============= END ===============")

main()
