# Rabin Karp Algorithm

'''
Karp-Rabin algorithm is a string-searching algorithm that utilises hashing to find matches 
between a given search pattern and a text.

Rabin-Karp improves upon this concept by utilising the fact that comparing the hashes 
of two strings can be done in linear time and is far more efficient than comparing 
the individual characters of those strings to find a match. 
Thus, providing a best case runtime complexity of O(n+m).


Algorithm:
1. Compute the hash of the string pattern.
2. Compute the substring hash of the string text starting from index 0 to m-1.
3. Compare the substring hash of text with the hash of pattern.
    - If they are a match, then compare the individual characters to ensure 
    the two strings are an exact match.
    - If they are not a match, then slide the substring window by incrementing 
    the index and repeat step 3 to compute the hash of the next m characters 
    until all n characters have been traversed

Modular Arithmetic
All math in the Rabin-Karp algorithm needs to be done in modulo Q to 
avoid manipulating large H values and integer overflows.
This is done at the expense of increased hash collisions, also known as spurious hits.
'''

# d is the number of characters in the input alphabet
d = 256

# pat  -> pattern
# txt  -> text
# q    -> A prime number

def search(pat, txt, q):
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0 # hash value for pattern
    t = 0 # hash value for txt
    h = 1

    # The value of h would be "pow(d, M-1)%q"
    for i in range(M-1):
        h = (h*d)%q

    # Calculate the hash value of pattern and first window
    # of text
    for i in range(M):
        p = ((d * p) + ord(pat[i])) % q
        t = ((d * t) + ord(txt[i])) % q

    # Slide the pattern over text one by one 
    for i in range(N-M+1):
        if p == t:
            for j in range(M):
                if txt[i+j] != pat[j]:
                    break
                else:
                    j += 1
            if j == M:
                print("Pattern found at index " + str(i))

    # Calculate hash value for next window of text: Remove
    # leading digit, add trailing digit
    if i < N-M:
        t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q

        # We might get negative values of t, converting it to
        # positive
        if t < 0:
            t = t + q

txt = "GEEKS FOR GEEKS"
pat = "GEEK"

# A prime number
q = 101

# Function Call
search(pat, txt, q)

'''
Time complexity:
    best: o(m+n)
    average: o(m+n)
    worst: o(mn)
    The worst case of the Rabin-Karp algorithm occurs when all characters of pattern 
    and text are the same as the hash values of all the substrings of T[] match with 
    the hash value of P[]. 

Space complexity:
    o(1)
'''