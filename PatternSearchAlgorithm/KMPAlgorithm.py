# KMP Algorithm

'''
The basic idea behind KMP’s algorithm is: 
whenever we detect a mismatch (after some matches),
we already know some of the characters in the text of the next window. 
We take advantage of this information to avoid matching the characters 
that we know will anyway match. 

'''

from typing import List

def getNext(next: List[int], s:str) -> None:
    j = 0
    next[0] = 0
    for i in range(1, len(s)):
        while j > 0 and s[i] != s[j]:
            j = next[j-1]
        if s[i] == s[j]:
            j += 1
        next[i] = j

def KMP(haystack: str, needle: str) -> int:
    if len(needle) == 0:
        return 0
    next = [0] * len(needle)
    getNext(next, needle)
    j = 0
    for i in range(len(haystack)):
        while j > 0 and haystack[i] != haystack[j]:
            j = next[j-1]
        if haystack[i] == haystack[j]:
            j += 1
        if j == len(needle):
            idx = i - len(needle) + 1
            j = 0
            print("Pattern found at index " + str(idx))
    return -1

txt = "GEEKS FOR GEEKS"
pat = "GEEK"
KMP(txt, pat)

'''
Time complexity:
    o(m+n)

Space complexity:
    o(m)

'''