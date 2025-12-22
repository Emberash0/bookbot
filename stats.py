#Counts words in a given string
def word_count(book):
    book_words = book.split()
    count = len(book_words)
    return count