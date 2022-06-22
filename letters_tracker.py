import random
from display_parachute import Display_parachute
from words_list import words_list


class Letters_tracker:

    def __init__(self):
        self.word_to_guess = random.choice(words_list)
        self.word_string = ["_", "_", "_", "_", "_"]
        self.player_attempt = 4
        self.parachute = Display_parachute()    
    
    
    def word_tracker(self):
       
        

        while self.player_attempt >= 0:
            self.player_letter_guess = input("\nChoose a letter [a-z] for your guess: ")
            if self.player_letter_guess in self.word_to_guess:
                
                print(f"The letter '{self.player_letter_guess.upper()}' is in the word!")
            
            
            else:
                
                print(f"The letter '{self.player_letter_guess.upper()}' is not in the word.")
                self.player_attempt = self.player_attempt - 1
            
            print(f"{self.word_string}\n")
            self.parachute.display_jumper(self.player_attempt)



    def word_display(self):
        
        self.word_to_guess = (self.word_to_guess).upper
        self.display_word = ["_" for letter in self.word_to_guess]
        print(self.display_word)



# How to test a single file
if __name__ == "__main__":
    test = Letters_tracker()
    test.word_tracker()
    
    #print(test.word_to_guess)
    