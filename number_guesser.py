from random import randint


num_low: int = 1
num_high: int = 10

print("Number Guessing Game!")
print(f"Guess a number between {num_low} to {num_high}")

a: int = randint(num_low,num_high)


while True: 
    try:
        guess: int = int(input("Take a Guess :"))
        if guess < a:
            print("Wrong Guess! Try Guessing Higher")
        elif guess > a:
            print("Wrong Guess! Try Guessing Lower")
        else: 
            print("You Guessed It correctly")
            break
    except ValueError: 
        print("Enter a Valid Integer")


