#from wordsets import english_words, english_words_small
from wordsets import english_words_small


def find_anagrams(letters, words):
    """Find a collection of anagrams of given letters from a given word bank.

    :param letters: The letters from which to form anagrams.
    :param words: A set of lowercase, alphabetic English words in a word bank.
    :return: A set of anagrams of the given letters found in the word bank.
    """
    canonicalize_letters = canonicalize(letters)

    lookup_dict = build_lookup(words)

    if lookup_dict.get(canonicalize_letters, 0):
       return lookup_dict[canonicalize_letters]
    return set()


"""
Create a canonicalized string from a given word.
Canonical meaning letters sorted alphabetically
:param word: a string to form the canonical string
:return: A string that has been sorted alphabetically
"""
def canonicalize(word):
    canonical_list = sorted(word)
    canonical_str = ""
    for l in canonical_list:
        canonical_str += l
    return canonical_str

"""
Create a lookup dictionary where each key is the canonical word and each value
is all the words in the parameter "words" that matches.

:param words: a given word bank.
:return : a dictionary of canonical words (keys)
          and a set of matching words in the words bank (value).
"""
def build_lookup(words):
    lookup = {}
    key_set = {canonicalize(word) for word in words}
    #print(key_set)
    for key in key_set:
        #print("key " + key)
        for word in words:
            #print("word " + word)
            if key == canonicalize(word):
                #print("key == word")
                if lookup.get(key, 0):
                    #print(lookup[key])
                    lookup[key] = lookup[key] |{word,}
                else:
                    lookup[key] = {word,}

    return lookup


# Test code. Switch out "english_words_small" param to change word bank
if __name__ == '__main__':
    while True:
        letters = input("What letters would you like to find the anagram of? ").lower().strip()
        for anagram in find_anagrams(letters, english_words_small):
            print(anagram)
