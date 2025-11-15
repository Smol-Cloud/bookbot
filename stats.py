def get_num_words(text):
    words = text.split()
    return len(words)

def char_count(text):
    text = text.lower()
    chars = {}
    for char in text:
        if char in chars:
            chars[char] += 1
        else:
            chars[char] = 1
    return chars

def sorted_char_count(chars_dict):
    char_list = []

    for key, value in chars_dict.items():
        if key.isalpha():
            char_list.append({"char": key, "num": value})
    
    def sort_on(items):
        return items["num"]

    char_list.sort(reverse=True, key=sort_on)

    return char_list