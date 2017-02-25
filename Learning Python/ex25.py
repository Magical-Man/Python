#Here I think that .split() will seperate each word with white space

def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(" ")
    return words

#Here I think that sorted() means to sort alphabet

def sort_words(words):
    """Sorts the words."""
    return sorted(words)

#I think this means pop the firs value, then print it

def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print(word)

#This means pop the last value then print it

def print_last_word(words):
    """Prints the last word after popping it off."""
    word  = words.pop(-1)
    print(word)

#Uses prior functions to create a new function
def sort_sentence(sentence):
    """Takes in a full scentance and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)

def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)

def print_first_and_last_sorted(scentence):
    """Sorts the words then prints the first and last one."""
    words =  sort_sentence(scentence)
    print_first_word(words)
    print_last_word(words)
