def get_num_words(text):
    words = len(text.split())
    return words

def get_letter_occurrences(text):
    letters_dict = {}
    for letter in text:
        new_letter = letter.lower()
        if new_letter in letters_dict:
            letters_dict[new_letter] += 1
        else:
            letters_dict[new_letter] = 1
    return letters_dict

def get_sorted_list(dictionary):
    sorted_list = []
    for key, value in dictionary.items():
        pair = {"char": key, "num": value}
        sorted_list.append(pair)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list

def sort_on(list_to_sort):
    return list_to_sort["num"]