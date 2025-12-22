#Counts words in a given string
def word_count(book):
    book_words = book.split()
    count = len(book_words)
    return count

def char_count(book):
    chars = {}
    for char in book:
        char_set = char.lower()
        if char_set in chars:
            chars[char_set] += 1
        else:
            chars[char_set] = 1
    return chars

def sort_on(items):
    return items["num"]

def num_sort(char_dict):
    sorted_dicts = []
    for entry in char_dict:
        sorted_dicts.append(
            {"char": entry,
            "num": char_dict[entry]
            }
        )
        sorted_dicts.sort(reverse=True, key=sort_on)
    return sorted_dicts



    
