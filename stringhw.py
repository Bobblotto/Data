# Input: a = "listen", b = "silent"
# Output: True

def anagramChecker(string1, string2):

    anagram = True

    if len(string1) != len(string2):
        anagram = False

    for i in string1:
        if i not in string2:
            anagram = False

    
    return anagram


print(anagramChecker("listen", "silent"))