vowels = list("aeiou")
word = input("Please input the word you want to check:")
found = {}
for letter in word:
    if letter in vowels:
        found.setdefault(letter,0)
        found[letter] += 1
for k,v in sorted(found.items()):
    print(k,"was found",v,"time(s)")