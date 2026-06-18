#Counts words in a given string
def word_count(book):
    book_words = book.split()
    count = len(book_words)
    return count

def word_count_dict(book):
    words = {}
    word = ""
    for char in book:
        if char.isalpha() or char == "'":
            if word == "":
                word = char.lower()
            else:
                word += char.lower()
        else:
            if word != "":
                if word in words:
                    words[word] += 1
                else:
                    words[word] = 1
            word = ""
    return words


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
    return items[1]

def chars_dict_to_sorted_list(dict):
    result = []
    for char in dict:
        result.append((char, dict[char]))
    result = sorted(result, key=sort_on, reverse=True)
    return result

def words_dict_to_sorted_list(dict):
    result = []
    for word in dict:
        result.append((word, dict[word]))
    result = sorted(result, key=sort_on, reverse=True)
    return result

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
