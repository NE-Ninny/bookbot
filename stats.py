def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        
        return file_contents

def num_of_words(filepath):
    word_count = 0
    book_text = get_book_text(filepath)
    
    for words in book_text.split():
        word_count += 1
	
    return f"{word_count} words found in the document"
