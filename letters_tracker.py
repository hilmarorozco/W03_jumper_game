import random
from display_parachute import Display_parachute
from words_list import words_list


class Letters_tracker:

    def __init__(self):
        self.word_to_guess = (random.choice(words_list))
        self._word_string = ["_", "_", "_", "_", "_"]
        self.player_attempt = 4
        self.parachute = Display_parachute()
        self._found = False   
    
    
    def word_tracker(self):
       
        

        while self.player_attempt > 0:
            self.player_letter_guess = input("\nChoose a letter [a-z] for your guess: ")
            if self.player_letter_guess in self.word_to_guess:
                
                print(f"The letter '{self.player_letter_guess.upper()}' is in the word!")
            
            
            else:
                
                print(f"The letter '{self.player_letter_guess.upper()}' is not in the word.")
                self.player_attempt = self.player_attempt - 1
            
            self.word_display()
            print(f"{self._word_string}\n")
            self.parachute.display_jumper(self.player_attempt)
            
            if self.check_word_found() == True:
                print("You won!")
                return

            if self.player_attempt == 0:
                print("You lost!")
                return




    def word_display(self):
        print(f"\n{self.word_to_guess}\n")
        self.word_to_guess = (self.word_to_guess) #.upper
        
   
        word_len = len(self.word_to_guess)

        for index in range(0, word_len):
            if self.player_letter_guess == self.word_to_guess[index]:
                
                self._word_string[index] = self.player_letter_guess


    def check_word_found(self):
        for index in range(0, len(self._word_string)):
            if "_" == self._word_string[index]:
                return False
        
        return True







# How to test a single file
if __name__ == "__main__":
    test = Letters_tracker()
    test.word_tracker()
    #test.word_display()
    
    #print(test.word_to_guess)
    