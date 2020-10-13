# Python Activtiy
# 
# Fill in the code for the functions below. 
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# Part A. starts_with
# Define a function starts_with(s, char) that takes a string and a character
# and returns true if the string starts with that character and false otherwise. 
def starts_with(s, char):
    if len(s) == 0 and char == "":
        return True
    elif len(char) == 0:
        return True
    elif len(s) > 0:
        first_letter = s[0]
        if ord(char) == ord(first_letter):
            return True
    return False


# Part B. starts_with_vowel
# Define a function starts_with_vowel(s) that takes a string and
# returns true if the string starts with a vowel and false otherwise. 
# For our purposes, a consonant is any letter other than A, E, I, O, U)
# Your solution should work for both upper and lower cases 
def starts_with_vowel(s):
    vowel = "aeiouAEIOU"
    if len(s) > 0:
        if s[0] in vowel:
            return True

    return False


# Part C. max_min_sum
# Define a function max_min_sum(arr) that takes an array and returns the sum
# of the largest element and the smallest element of the array.
# For an empty array it should return zero
# For an array with just one element, it should return that element
def max_min_sum(arr):
    arrayLength = len(arr)
    if arrayLength == 0:
        return 0
    elif arrayLength ==1:
        return arr[0]
    else:
        maxNumber = max(arr)
        minNumber = min(arr)
        sum = maxNumber + minNumber
        return sum
    return
