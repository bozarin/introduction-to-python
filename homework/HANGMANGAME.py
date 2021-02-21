import random
import sys


def main():
name=input("Please enter your name: ")
print("Welcome {name}, this is the Hangman game!")

keyword=input("Please enter a word: ")
print("_ "*(len(keyword)))
