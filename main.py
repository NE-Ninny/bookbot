from stats import num_of_words
from stats import character_count

def main():    
    word_count = num_of_words("./books/frankenstein.txt")
    num_of_characters = character_count("./books/frankenstein.txt")

    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(word_count)
    print("--------- Character Count -------")
    print(num_of_characters)
    print("============= END ===============")

main()
