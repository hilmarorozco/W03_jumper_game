


from display_parachute import Display_parachute
from letters_tracker import Letters_tracker



class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        
             
    """
    
    def __init__(self): 
        #, lives_num = 4):
        """Constructs a new instance of Director.

        Args:
            self (Director): An instance of Director.
        """
        self._is_alive = True
        #self._is_playing = True
        #self._lives = lives_num


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
        
        
        
        self.word_string = ["_", "_", "_", "_", "_"]
        word = Letters_tracker()

        


