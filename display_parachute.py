class Display_parachute:
    def __init__(self):

        self.parachute4 = "  ___\n /___\ \n \   /\n  \ /\n   0\n  /|\ \n  / \ \n\n^^^^^^^"
        self.parachute3 = " /___\ \n \   /\n  \ /\n   0\n  /|\ \n  / \ \n\n^^^^^^^"
        self.parachute2 = " \   /\n  \ /\n   0\n  /|\ \n  / \ \n\n^^^^^^^"
        self.parachute1 = "  \ /\n   0\n  /|\ \n  / \ \n\n^^^^^^^"
        self.parachute0 = "   X\n  /|\ \n  / \ \n\n^^^^^^^"

    def display_jumper(self, player_attempt):
        if player_attempt == 4:
            print(self.parachute4)
        if player_attempt == 3:
            print(self.parachute3)
        if player_attempt == 2:
            print(self.parachute2)
        if player_attempt == 1:
            print(self.parachute1)
        if player_attempt == 0:
            print(self.parachute0)

# How to test a single file
if __name__ == "__main__":
    display = Display_parachute()
    display.display_jumper(4)
