from pprint import pprint
import random

def sumall(*args):
    result = 0
    for a in args:
        if type(a) != int and type(a) != float:
            raise ValueError, 'all arguments must be numbers'
        else:
            result += a
    return result

def most_frequent(word):
    """
    Prints the letters in a word in order of descending frequency.
    """
    d = {}
    for letter in word:
        if letter not in d.keys():
            d[letter] = 1
        else:
            d[letter] += 1
    t = zip(d.values(), d.keys())
    t.sort(reverse=True)
    for frequency, letter in t:
        print frequency, letter

def ReadText(path):
    line_list = []
    fin = open(path)
    for line in fin:
        word = line.strip()
        line_list.append(word)
    return line_list

def BucketLength(wordlist):
    buckets = {}
    for word in wordlist:
        length = len(word)
        if length in buckets.keys():
            buckets[length].append(word)
        else:
            buckets[length] = [word]
    return buckets

def SortedLetters(word):
    if type(word) != str:
        raise ValueError, 'word must be of type str'
    listed = list(word.lower())
    listed.sort()
    tupled = tuple(listed)
    return tupled

def FindAnagrams(worddict):
    result = {}
    for wordlist in worddict.values():
        for word in wordlist:
            letters = SortedLetters(word)
            if letters in result.keys():
                result[letters].append(word)
            else:
                result[letters] = [word]
    return result

def ReturnAnagrams(anagramdict):
    result = []
    for v in anagramdict.values():
        if len(v) > 1:
            result.append(v)
    return result

def FindMetathesisPairs(anagramlist):
    result = []
    for wordlist in anagramlist:
        lowindex = 0
        highindex = 1
        wordlen = len(wordlist[0])
        while lowindex < len(wordlist) - 1 and highindex < len(wordlist):
            w1 = wordlist[lowindex]
            w2 = wordlist[highindex]
            mismatch = 0
            letterindex = 0
            while letterindex < wordlen:
                l1 = w1[letterindex]
                l2 = w2[letterindex]
                letterindex += 1
                if l1 == l2:
                    continue
                else:
                    mismatch += 1
                if mismatch > 2:
                    break #move onto next word pairing if there are more than two mismatches found
            if mismatch == 2:
                print (w1, w2)
            if highindex < len(wordlist):
                highindex += 1
            else:
                lowindex += 1                  
    return None

def IsWord(word, buckets):
    if word in buckets[len(word)]:
        return True
    else:
        return False

def ReduceWord(word, buckets):
    length = len(word)
    reduce_list = []
    index = 0
    while index < length:
        reduce_string = word[:index] + word[index + 1:]
        if IsWord(reduce_string, buckets) == True and reduce_string not in reduce_list:
            reduce_list.append(reduce_string)
        index += 1
    return reduce_list

def ReducibleWord(word, buckets):
    reduce_list = [word]
    while reduce_list != []:
        if reduce_list[0] == '':
            return True
        children = []
        for i in reduce_list:
            try:
                child = ReduceWord(i, buckets)  
            except:
                continue
            children.extend(child)
        reduce_list = children
    return False

def IncrementWord(word, buckets):
    length = len(word) + 1
    increment_list = []
    for v in buckets[length]:
        if word == v[:length - 1] and v not in increment_list:
            increment_list.append(v)
        if word == v[1:] and v not in increment_list:
            increment_list.append(v)
    if len(increment_list) > 0:
        return increment_list
    else:
        return None

def ExtendWord(word, buckets):
    extend_list = [word]
    while extend_list:
        print extend_list
        loop_list = None
        for i in extend_list:
            try:
                if not loop_list:
                    loop_list = IncrementWord(i, buckets)
                else:
                    loop_list.extend(IncrementWord(i, buckets))
            except:
                continue
        if loop_list:
            extend_list = loop_list
        else:
            return extend_list


wordlist = ReadText('words.txt')

buckets = BucketLength(wordlist)

index = int(buckets.keys()[-1:][0])
while index > 0:
    print "Searching words with %s letters..." % index
    for v in buckets[index]:
        if ReducibleWord(v, buckets) == True:
            print v
        else: 
            continue
    index -= 1


















