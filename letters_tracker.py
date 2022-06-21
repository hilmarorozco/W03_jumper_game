import random
from words_list import words_list


class Letters_tracker:

    def __init__(self):
        self.word_to_guess = (random.choice(words_list)).upper

    
    
    def word_tracker(self):
    
        self.letters_to_guess = set(self.word_to_guess)
        
        self.word_found = False
        self.player_attempt = 4    

        
        while (self.word_found == False) and (self.player_attempt >= 0):
            self.player_letter_guess = ("\nChoose a letter [a-z] for your guess: ")

            


            if self.player_letter_guess in self.letters_to_guess:
                print(f"The letter '{self.player_letter_guess.upper()}' is in the word!")
            else:
                
                print(f"The letter '{self.player_letter_guess.upper()}' is not in the word.")
                self.player_attempt = self.player_attempt - 1

    def word_display(self):
        


