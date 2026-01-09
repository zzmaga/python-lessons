# Complete the solution so that the function will break up camel casing, using a space between words.
# 1 var
def solution(s):
    res = ""
    for char in s:
        if char.isupper():
            res += " "
        res += char
    return res.strip()


# 2 var
def solution(s):
    newStr = ""
    for letter in s:
        if letter.isupper():
            newStr += " "
        newStr += letter
    return newStr


# 3 var
def solution(s):
    final_string = ""
    for i in range(len(s)):
        char = s[i]
        if char.isupper():
            final_string += " " + char
        else:
            final_string += char
    return final_string
