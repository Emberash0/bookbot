from stats import word_count

#returns a book stored in location: filepath as a string and closes the called file
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    book = "books/frankenstein.txt"
    num_words = word_count(get_book_text(book))
    print(f"Found {num_words} total words")

main()