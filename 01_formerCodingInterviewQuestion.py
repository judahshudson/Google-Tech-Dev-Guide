'''
https://techdevguide.withgoogle.com/paths/foundational/find-longest-word-in-dictionary-that-subsequence-of-given-string#!

Former Coding Interview Question:
Find longest word in dictionary that is a subsequence of a given string


The Challenge
Given a string S and a set of words D, find the longest word in D that is a subsequence of S.

Word W is a subsequence of S if some number of characters, possibly zero, can be deleted from S to form W, without reordering the remaining characters.

Note: D can appear in any format (list, hash table, prefix tree, etc.

For example, given the input of S = "abppplee" and D = {"able", "ale", "apple", "bale", "kangaroo"} the correct output would be "apple"

The words "able" and "ale" are both subsequences of S, but they are shorter than "apple".
The word "bale" is not a subsequence of S because even though S has all the right letters, they are not in the right order.
The word "kangaroo" is the longest word in D, but it isn't a subsequence of S.
Learning objectives
This question gives you the chance to practice with algorithms and data structures. It’s also a good example of why careful analysis for Big-O performance is often worthwhile, as is careful exploration of common and worst-case input conditions.


1) ALGORITHM
Data Structures
D (set of words) = [list]
S (a string) = "string" 

Function Find Longest Word Inside
-iterate through set of words D
-for each word
*iterate through letters
*see if letter is in string S
*proper sequence
(next letter of word
must be found in strange after previous,
not before)
*if not -> word not in string
*if yes -> is it the longest?

***continue here***
implement this into code below:
How To Continue
if target letter of word not in string, stop & skip word
if all letters of word found in string (in sequence),
if len(current word) > Longest Word
then Longest Word = current word


2) PSEUDO CODE
D = []     #set of words
S = ""     # a string
indexOfLastFoundLetter = 0
longestWord = ""

for word in D:
    for letter in D:
        if letter in string S:
             if ***index of letter in S*** > indexOfLastFoundLetter:   #ensure proper sequence
                continue
             else:
                  word is not in S / go to next word in D
        else:
                  word is not in S / go to next word in D
    if word found in S:
         if len(word) > len(longestWord):
              longestWord = word

run program (using data, function)

'''


D = ["able", "ale", "apple", "bale", "kangaroo"]
S = "abppplee"
indxPrevLetter = 0
currentWord = ""
longestWord = ""
substringOfS = True 

# find longest word in D that is a subsequence of S.
for word in D:
    for letter in word:	#is word a substring of S?
        if letter in S: # all letters in S
            if S.find(letter) > indxPrevLetter: #ensure proper sequence (current found letter comes after previous found letter)
                indxPrevLetter = S.find(letter)	#update indxPrevLetter
                currentWord += letter	#add letter to currentWord
            else:	#word not a substring of S
                #substringOfS = False NOTE: this gave false kangaroo answer 
                break
        else:		#word not a substring of S
            substringOfS = False 
            break
    # word is substring of S
    if substringOfS and len(word) > len(longestWord):
	    longestWord = word
    substringOfS = True #reset to true

print(longestWord)	





