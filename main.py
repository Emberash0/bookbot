from stats import word_count, char_count, num_sort
import sys

#returns a book stored in location: filepath as a string and closes the called file
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    num_words = word_count(text)
    num_chars = char_count(text)
    report = num_sort(num_chars)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for datum in report:
        if datum["char"].isalpha():
            print(f"{datum["char"]}: {datum["num"]}")
    print("============= END ===============")

main()