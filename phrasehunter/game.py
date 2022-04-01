from phrasehunter.phrase import Phrase 
import random

class Game:
    
    def __init__(self):
        self.win = None
        self.lives = 7
        self.missed = 0
        self.phrases = ["the kid next to me smells like cheese", "i forgot what im doing", "peanut                          butter jelly time?", "wow thats a big hand", "you got nice toes"]
        self.active_phrase = None
        self.guesses = []
        
    def start(self):
        self.active_phrase = self.get_random_phrase()   
        self.welcome()
        
    def get_random_phrase(self):
        chosen_phrase = random.choice(self.phrases)
        return chosen_phrase
    
    def welcome(self): 
        ready = 0
        while ready == 0:
            ready = input("""
            Welcome to PhraseHunters 
            ------------------------ 
            Ready to play? (y/n)
            > """)
            if ready == "y":
                self.get_guess() 
            elif ready == "n":
                print("fine you dont have to, dont come back!")
                exit() 
            else:
                print("Please choose a valid option")
                
    def get_guess(self):
        guessing = True
        while guessing == True:
            phrase = Phrase(self.active_phrase)
            self.display_phrase = phrase.display(self.guesses)
            check = phrase.check_complete(self.lives, self.display_phrase, self.active_phrase) 
            if check == "win":
                self.game_over(check)   
            if check == "lose":
                self.game_over(check)
            if check == "incomplete":
                print("")
            current_guess = input("Guess a letter: ").lower()
            
            if current_guess not in self.active_phrase: 
                self.lives -= 1
                self.missed += 1
                
            print("You have {} out of 7 lives remaining!".format(self.lives)) 
            if len(current_guess) > 1:
                print("Guess one letter at a time") 
            else:
                self.guesses.append(current_guess)
                
    def game_over(self, status): 
        if status == "win":
            print("Heyyyy your smarter than i thought!")
            exit()
        if status == "lose":
            print("Thats a real shame, maybe youll get it next time.") 
            exit()
