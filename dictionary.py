import json
from difflib import get_close_matches

data =json.load(open("data.json"))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif len(get_close_matches(word, data.keys()))>0:
        print("did you mean %s instead?" %get_close_matches(word,data.keys())[0])
        decide = input("press y for yes or n for no")
        if decide == "y" or "Y":
            return data[get_close_matches(word,data.keys())[0]]
        elif decide == "n" or "N":
            return("Word doesnt't exist in the dictionary.")
        else:
            print("Please enter y or n.")

    else:
        print("Word doesnt't exist in the dictionary.")

word = input("Enter the word you want to search:")
output = translate(word)

if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)