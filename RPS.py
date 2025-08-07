import random
import sys

class RPS:
    """
    This class is a higly robust and modular rock paper scissors implementation

    """
    def __init__(self) -> None:
        """
        This is class constructor
        """
        print("Welcome to RPS !!")
        print("_____________________________")

        self.choices: dict = {'rock':'🪨',"paper": '📃', 'scissors': '✂️'}
        self.moves: list[str] = list(self.choices.keys())

    def play_game(self)->None:
        """
        This is the main function to play the game

        """
        while True:
            try:
                #show options
                self.options()

                user: str  =  input("Enter a Choice :").lower()
                if user == 'exit':
                    print("Thanks For Playing!")
                    sys.exit()

                if user not in self.moves:
                    raise ValueError

                robo = random.choice(self.moves)

                self.selection(user, robo)
                self.check(user, robo)
            except ValueError:
                print("You Can Only Choose from the options or exit the game ")
                continue


    def options(self)->None:
        """
        This is to display the options of the game 
        """
        print("_____________________________")
        print("Choose From the Following: ")
        for i, (key, value) in enumerate(self.choices.items(), 1):
            print(f"{i}.{key} {value}")
        print("_____________________________")

    def selection(self,user,robo)->None:
        """
        This to show the choices
        """
        print("_____________________________")
        print(f"You Played : {self.choices[user]}")
        print(f"Robo Played : {self.choices[robo]}")
        print("_____________________________")

    def check(self, user, robo)->None:
        """
        This is to check the options of the user against the robot
        """
        if user == robo:
            print("Draw!")
        elif user == 'rock' and robo == 'scissors':
            print("You win!")
        elif user == 'scissors' and robo == 'paper':
            print("You win!")
        elif user == 'paper' and robo == 'rock':
            print("You win!")
        else:
            print("You lost!")

if __name__ == "__main__":
    a = RPS()
    a.play_game()