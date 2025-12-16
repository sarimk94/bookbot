def get_num_words(book):
    return len(book.split())

def get_chars(s):
    my_dict = {}
    for char in s:
        lower_char = char.lower()
        if lower_char not in my_dict:
            my_dict[lower_char] = 1
        else:
            my_dict[lower_char] += 1
    return my_dict


def sorted_dict(my_dict):
    sorted_list = []
    for k, v in my_dict.items():
        sorted_list.append({'char': k, 'num': v})
    sorted_list.sort(reverse=True, key=lambda item: item['num'])
    return sorted_list


