import random
import sys





def main():
name=input("Please enter your name: ")
print("Welcome {name}, this is the Hangman game!")

        
keyword=input("Please enter a word: ")
print("_ "*(len(keyword)))


guessed_word=set(guessed_word) 
newset=set() 

a=[] 
guesses=["_ "for j in range(len(keyword))]

def guess(letters): 
    if not letters in keyword:
        a.append("x")
        hanging(len(a)) 

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
    
    class Hangman(object):

    Hangman_Versions = ["", "O", "O-", "O-|", "O-|-", "O-|-<"]

    def __init__(sguess):
        self.hangman = self.Hangman_Versions[0]

    def draw(self, incorrect_guesses):
       

    sguess.hangman = guess.Hangman_Version[incorrect_guesses]
    
    print sguess.hangman
    
        if 
        
        incorrect_guesses == 5 :
            print( "You have been killed :(" )
    
    while letter_guess.isalpha() = False: 
                word_guess = raw_input("No special characters allowed! Only enter a letter, please: ").lower()

            
            if 
                letter_guess not in sguess.guessed_letters:
                sguess.guessed_letters.append(letter_guess)
    
