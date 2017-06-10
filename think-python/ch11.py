from pprint import pprint

def ReadText(path):
    line_list = []
    fin = open(path)
    for line in fin:
        word = line.strip()
        line_list.append(word)
    return line_list

words = ReadText('words.txt')

def has_duplicates(input_list):
    look = {}
    for i in input_list:
        if i not in look.keys():
            look[i] = 1
        else:
            return True
    return False

def rotate_word(word, rotate=13):
    """
    Converts [word] to its ASCII character code and increments it by [rotate] within the range of lower case letters.
    Defaults to ROT13 encryption.

    INPUT:
        word: string
        rotate: integer
    OUTPUT:
        result: rotated
    """
    ord_list = []
    rotated = ''
    lo = ord('a')
    hi = ord('z')
    if rotate > hi - lo:
        raise ValueError, 'rotate is too great'
    for c in word.lower():
        rotation = ord(c) + rotate
        if hi > rotation > lo:
            ord_list.append(rotation)
        else:
            remainder = rotation % hi
            ord_list.append(lo + 1 + remainder)
    for i in ord_list:
        rotated += chr(i)
    return rotated

def rotate_pair(word1, word2, rotate=13):
    """
    Returns a dictionary if the
    """
    pair = {}
    if rotate_word(word1, rotate) == word2:
        pair[word1] = word2
        return pair
    else:
        return None

def rotate_pairs(words, rotate=13):
    rotated_dict ={}
    rotate_pairs = {}
    for word1 in words:
        rotated_dict[word1] = rotate_word(word1, rotate)
    for word2 in words:
        if rotated_dict.get(rotate_word(word2, -rotate)):
            rotate_pairs[word2] = rotate_word(word2, -rotate)
    # for word2 in words:
    #     rotate_pairs[word2] = rotated_dict.get(word2)
    return rotated_dict, rotate_pairs


pprint(rotate_pairs(words))












