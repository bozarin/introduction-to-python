import random
import sys





def main():
name=input("Please enter your name: ")
print("Welcome {name}, this is the Hangman game!")

keyword=input("Please enter a word: ")
print("_ "*(len(keyword)))


def display(key, guessed_words):

        word_displayed = "  "

     for letter in keyword:
            if letter in guessed_words:
                word_displayed += " " + letter + " "

     else:
      word_displayed += " _____ "

        print "This is your word so far:", word_displayed, 
        print("\n")

        return word_displayed
