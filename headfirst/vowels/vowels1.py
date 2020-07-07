words = input("Please input the word you want to check: ")
vowels = ['a','e','i','o','u']
found = []
for letter in words:
    if letter in vowels:
        if letter not in found:
            found.append(letter)
for vowel in found:
    print(vowel)
