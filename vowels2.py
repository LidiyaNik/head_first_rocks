vowels = ['a', 'e', 'i', 'o', 'u']
word = input('Provide a word to search for vowels:')
found = []
for letter in word:
    if letter in vowels:
        #опреділення необхідності включення букви в список vowels
        if letter not in found:
            found.append(letter)
#цикл, який відображає знайдену в слові букву
for vowel in found:
    print(vowel)