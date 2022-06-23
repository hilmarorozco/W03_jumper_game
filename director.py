


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
        #self._is_alive = True

        self.tracker = Letters_tracker()

        #self._lives = lives_num

# 
    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        print("start game")

        self._play_game()


    def _play_game(self):
        """ text here
        
        Args:
            self (Director): An instance of Director.
        """
        self.tracker.word_tracker()

        #print("It kind of works")
        
        



    # def _word_found(self):
    #     """ text here
        
    #     Args:
    #         self (Director): An instance of Director.
    #     """
        #tracker = Letters_tracker()




