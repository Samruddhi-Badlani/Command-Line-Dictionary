import json
from difflib import get_close_matches
dictionary = json.load(open("data.json"))
def find_meaning(word):
    word = word.lower()
    if word in dictionary:
        return dictionary[word]
    elif word.title() in dictionary:
        return dictionary[word.title()]
    elif word.upper() in dictionary:
        return dictionary[word.upper()]
    elif len(get_close_matches(word,dictionary.keys())) > 0:
        value = input("Did you mean %s Enter Y for Yes else N for no : " % get_close_matches(word,dictionary.keys())[0])
        if value == 'Y':
            return dictionary[get_close_matches(word,dictionary.keys())[0]]
        else:
            return "Sorry we could not understand the word"
    else:
        return "The word does not exist"

print("**************COMMAND LINE DICTIONARY*****************")
word = input("Enter a word : ")
output = find_meaning(word)

if type(output) == list:
    for x in output:
        print(x)
else:
    print(output)