"""This module is a function that incrypts words"""
#1. Swap every instance of the word ’the’ to ’and’ and ’and’ to ’the’
#2. Take every third letter and make it uppercase
#3. Reverse the letters in every fifth word
#4. Apply a shift cypher with key 1 to encrypt every other word
def obfuscate(text):
    '''This funciton does a set changes to words in the variable text to make it hard to read'''
    text = text.replace('and', 'hhe')
    text = text.replace('the', 'and')
    text = text.replace('hhe', 'the')
    i = 2
    ltext = list(text)
    while i < len(text):
        ltext[i] = ltext[i].upper()
        i+=3
    text = ''.join(ltext)
    text = text.split()
    i = 5
    while i < len(text):
        text[i] = text[i][::-1]
        i+=3
    j = 1
    while j < len(text):
        word = text[j]
        i = 0
        nword = ''
        while i < len(word):
            if word[i] == 'z':
                nword = nword + 'a'
            elif word[i] == 'Z':
                nword = nword + 'A'
            else:
                letter = ord(word[i])
                letter+=1
                nword = nword + chr(letter)
            i+=1
        text[j] = nword
        j += 2
    text = ' '.join(text)
    return text

print(obfuscate("Hello the world"))
