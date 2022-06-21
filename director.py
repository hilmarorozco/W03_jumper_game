import random

from words_list import words_list
from display_parachute import Display_parachute
from score import Score



class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        
             
    """
    
    def __init__(self, lives_num = 4):
        """Constructs a new instance of Director.

        Args:
            self (Director): An instance of Director.
        """
        self._is_alive = True
        self._lives = lives_num


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_alive == True:
            self._play_game()
            #self._do_updates()
            #self._do_outputs()

 


    def _play_game(self):
        """ text here
        
        Args:
            self (Director): An instance of Director.
        """
        word_to_guess = (random.choice(words_list)).upper
        word_found = False
        #letters_guessed = []
        #words_guessed = []

        player_attempt = 4    

        
        while (word_found == False) and (player_attempt >= 0):
            player_letter_guess = ("\nChoose a letter [a-z] for your guess: ")

            if player_letter_guess not in word_to_guess:
                print(f"The letter '{player_letter_guess.upper()}' is not in the word.")
                player_attempt = player_attempt - 1
            else:
                print(f"The letter '{player_letter_guess.upper()}' is in the word!")
        


    # def _do_updates(self):
    #     """Keeps watch on where the seeker is moving.

    #     Args:
    #         self (Director): An instance of Director.
    #     """
    #     # self._hider.watch_seeker(self._seeker)
    #     pass
        
    # def _do_outputs(self):
    #     """Provides a hint for the seeker to use.

    #     Args:
    #         self (Director): An instance of Director.
    #     """

    #     # hint = self._hider.get_hint()
    #     # self._terminal_service.write_text(hint)
    #     # if self._hider.is_found():
    #     #     self._is_playing = False
    #     pass
            
