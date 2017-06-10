import string
import random

def StripPunctuation(word):
    result = ''
    for char in word:
        if char not in string.punctuation:
            result += char
    return result

def ReadText(path):
    file = open(path, 'r')
    line_list = []
    for line in file:
        line_list.append(line)
    return line_list

def StripLine(line):
    result = []
    for word in line:
        word = StripPunctuation(word.strip())
        if len(word) > 0:
            result.append(word)
    return result

def LinesToWords(line_list):
    word_list = []
    for line in line_list:
        line = StripLine(line.split(' '))
        if line:
            word_list.extend(line)
    return word_list

def WordFrequency(word_list):
    word_dict = {}
    for word in word_list:
        if word not in word_dict.keys():
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    freq_dict = zip(word_dict.values(), word_dict.keys())
    freq_dict.sort()
    for frequency, word in freq_dict:
        print frequency, word

# filename = 'The Shunned House.txt'

# line_list = ReadText(filename)

# word_list = LinesToWords(line_list)

# print """There are %s words total in %s.""" % (str(len(word_list)), filename)

# WordFrequency(word_list)

def histogram(s):
    d = {}
    for c in s:
        if c not in d:
            d[c] = 1
        else:
            d[c] += 1
    return d

hist = histogram('glassmoyer')

def choose_from_hist(histogram):
    seq = []
    for k, v in histogram.items():
        while v > 0:
            seq += k
            v -= 1
    return random.choice(seq)

print choose_from_hist({'a': 2, 'b': 1})














