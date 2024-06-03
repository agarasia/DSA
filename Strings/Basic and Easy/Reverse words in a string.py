# Approach: Use the in-built split()
#           function to seperate words
#           and concatenate the reversed list
def reverseWords(s):
    listWord = s.split()
    listWord.reverse()
    return " ".join(listWord)
# T(n) = O(n)
# S(n) = O(m)   where m is the number of words in the string

s = "a  good example"

print(reverseWords(s))