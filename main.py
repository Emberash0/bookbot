#returns a book stored in location: filepath as a string and closes the called file
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

#Counts words in a given string
def word_count(book):
    book_words = book.split()
    count = len(book_words)
    return count

def main():
    book = "books/frankenstein.txt"
    num_words = word_count(get_book_text(book))
    print(f"Found {num_words} total words")

main()