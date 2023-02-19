# Problem:
    # A string s, consisting of words and spaces, is given, and I need to write a program that returns
    # the length of the last word in the string. A word is a maximal Substring consisting for non-space characters only.

#Solution: |
 # I used ".split()" method of python, that splits all the individual, containing no spaces between characters, and makes a list.
 # I assigned that list words into the variable called "words", and returned the lenght of the last word.

def lengthOfLastWord(s: str) -> int:
        words = s.split()
        return len(words[-1])