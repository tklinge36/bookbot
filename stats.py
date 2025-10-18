def number_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars

def sorted_chars(text):
    chars_dict = get_chars_dict(text)
    chars_list = []

    for chars in chars_dict:
        char_dict = {"char": chars, "num": chars_dict[chars]}  # Different variable name
        chars_list.append(char_dict)  # Append char_dict, not chars_dict
    
    chars_list.sort(reverse=True, key=sort_on)  # Sort once, after the loop
    return chars_list

def sort_on(text):
    return text["num"]