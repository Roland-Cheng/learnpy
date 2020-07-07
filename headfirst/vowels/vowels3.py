vowels = set("aeiou")
word = input("Please input the word you want to check:")
u = sorted(list(vowels.intersection(set(word))))
for letter in u:
    print(letter)