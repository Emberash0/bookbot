from stats import word_count, char_count, num_sort, chars_dict_to_sorted_list, word_count_dict, words_dict_to_sorted_list
import sys

#returns a book stored in location: filepath as a string and closes the called file
def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def print_report(book_path, word_count, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    for item in sorted_chars:
        if item[0].isalpha():
            print(f"{item[0]}: {item[1]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 main.py <path_to_book> -w(words) OR -c(characters)")
        sys.exit(1)
    book = sys.argv[1]
    text = get_book_text(book)
    num_words = word_count(text)
    if(sys.argv[2]) == "-c":
        print("WordBot is counting characters...")
        num_chars = chars_dict_to_sorted_list(char_count(text))
        print_report(book, num_words, num_chars)
    if(sys.argv[2]) == "-w":
        print("WordBot is counting words...")
        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book}...")
        print("----------- Word Count ----------")
        print(f"Found {num_words} total words")
        word_chart = words_dict_to_sorted_list(word_count_dict(text))
        for word in word_chart:
            print(f"{word[0]}: {word[1]}")
        print("============= END ===============")

main()