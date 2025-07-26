from random import randint


def dice_roll(num: int) -> list[int]:
    """
    Rolls a specified number of 6-sided dice.

    :param num: The number of dice to roll. Must be a positive integer.
    :return: A list of integers representing the results of each roll.
    :raises ValueError: If 'num' is not a positive integer.
    """

    if num <= 0:
        raise ValueError

    rolls: list[int] = []
    for i in range(num):
        random_roll: int = randint(1, 6)
        rolls.append(random_roll)

    return rolls

def main() -> None:
    """
    This is the Main Function

    """
    while True:
        try:
            rolls = input("How many dice would you like to roll ? ")
        
            if rolls.lower() == 'exit':
                break

            print(*dice_roll(int(rolls)),sep = ",")
        except ValueError: 
            print("Enter a Valid Integer or type exit to leave")

if __name__ == "__main__":
    main()