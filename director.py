from terminal_service import TerminalService
from hider import Hider
from seeker import Seeker


class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        
             
    """
    
    def __init__(self):
        """Constructs a new instance of Director.

        Args:
            self (Director): An instance of Director.
        """
        self._is_alive = True


    def start_game(self):
        """Starts the game by running the main game loop.
        
        Args:
            self (Director): an instance of Director.
        """
        while self._is_alive != False:
            self._get_inputs()
            self._do_updates()
            self._do_outputs()

    def _get_inputs(self):
        """ text here
        
        Args:
            self (Director): An instance of Director.
        """    
        #letter_guess = self._terminal_service.read_number("\nEnter a location [1-1000]: "))
        # self._seeker.move_location(new_location)
        pass
        #letter_guess = self._terminal_service.prompt_text("\nChoose a letter [a-z] for your guess: ")
        
        
        
        
        

    def _do_updates(self):
        """Keeps watch on where the seeker is moving.

        Args:
            self (Director): An instance of Director.
        """
        # self._hider.watch_seeker(self._seeker)
        pass
        
    def _do_outputs(self):
        """Provides a hint for the seeker to use.

        Args:
            self (Director): An instance of Director.
        """

        # hint = self._hider.get_hint()
        # self._terminal_service.write_text(hint)
        # if self._hider.is_found():
        #     self._is_playing = False
        pass
            
