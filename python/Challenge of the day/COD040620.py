#Challenge of the Day 04/06/20 


def count_vowels(string):
    num_vow=(0)
    for vowel in string:
        if vowel in "aeiouAEIOU":
           num_vow = num_vow+1
    return num_vow



string=str(input("Please enter a word: "))

print(count_vowels(string))
