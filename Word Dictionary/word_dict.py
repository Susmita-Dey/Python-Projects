# Steps to reproduce:
# have a python dictionary that has a key/value pair that represents a word and it's definition
# collect input from the user, input is a word
# check if the word is in the dictionary or not
# print the definition of the word if exists

from PyDictionary import PyDictionary

# dictionary = PyDictionary()

# while True:
#     word = input("Enter your word: ")
#     print(dictionary.meaning(word))
#     print()
#     again = input("Do you wanna search another new word?(Yes/No) ")
#     if again == "Yes" or again == "yes":
#         continue
#     else:
#         print("Happy Hacking!!!")
#         break


dictionary = PyDictionary("hello", "eyes", "indentation")
print(dictionary.printMeanings())
print("\n\n")
print(dictionary.getMeanings())


# def main():
#     word_dictionary = {
#         'hi': 'a way of greeting',
#         'eyes': 'an organ for seeing',
#         'earth': 'a planet in space'
#     }

#     while True:
#         word = input("Enter a word: ")
#         if word == "":
#             break
#         if word in word_dictionary:
#             print(word, ":", word_dictionary[word])


# main()
