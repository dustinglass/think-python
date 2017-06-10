
def ReadText(path):
    line_list = []
    fin = open(path)
    for line in fin:
        word = line.strip()
        line_list.append(word)
    return line_list

words = ReadText('words.txt')

def find_letter_pair(word):
    pair_indexes = []
    index = 0
    while index < len(word) - 1:
        if word[index] == word[index + 1]:
            pair_indexes.append(index)
        index += 1
    return pair_indexes

def three_consecutive_pairs(word):
    pairs = find_letter_pair(word)
    index = 0
    while index < len(pairs) - 2:
        if pairs[index + 2] - pairs[index + 1] == 2 and pairs[index + 1] - pairs[index] == 2:
            print word
        index += 1
    return None


for word in words:
    three_consecutive_pairs(word)