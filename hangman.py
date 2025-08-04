import os
from google import genai
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
api_key =  os.getenv("API_KEY")

client = genai.Client(api_key=api_key)

def word_gen(category: str)-> str:
    '''
    This function is to generate the word for any given 'category' by the user

    '''
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(f"""You are a HANGMAN agent.
        Your task is to return a SINGLE valid word that fits the following category: "{category}".
            Avoid special characters like '*', '`', or quotes. Do not include spaces. 
            For multi-word categories, abbreviate if needed
            (e.g., 'United States of America' → 'USA')."""),
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
            ),
        )
        print("The Word contains " , len(response.text), "letters")
        return response.text.strip()
    except Exception as e:
        print(f"There was an error {e} while generating the word")
        return ""

def clue_gen(word: str,context: list,guess: str) -> str:
    '''
    This function is used to generate the clues when the user has guessed the wrong , 
    this sends the 'word' which is tho be guessed  

    '''
    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=(f"""You are a HANGMAN agent in a word-guessing game.
            Your task is to generate a helpful but not-too-obvious clue for the user.

            Here are the rules:
            - DO NOT reveal or mention the word directly.
            - DO NOT say things like "The word is..." or "This country is...".
            - Try to make the clue creative, subtle, and fun.
            - Use metaphors, indirect facts, or historical hints if possible.

            The target word (DO NOT MENTION THIS): {word}
            Previous clues: {context}
            The user's last incorrect guess was: {guess}
            Give your next clue below:
            """),
            config=types.GenerateContentConfig(
                thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
            ),
        )
        print("Here is your Clue: ",response.text)
        return response.text.strip()
    except Exception as e:
        print(f"There was an error {e} while generating the clue")
        return ""

def main()-> None:
    '''
    This is the main Function

    '''
    try:
        category = input("Enter the Category You Would like to play in :")
        word = word_gen(category).lower()
        guessed: set = set()
        tries = 5
        clues = 2
        context = []

        while tries > 0:
            blanks = 0

            print("Word : ", end = ' ')
            for char in word:
                if char in guessed:
                    print(char, end = ' ')
                else :
                    print('_', end = ' ')
                    blanks += 1

            print()

            #check for blanks
            if blanks == 0:
                print("You Have Guessed the Word !")
                break

            guess = input("Enter You Guess : ").lower()

            if guess in guessed:
                print('You have already guessed that')
                continue
            
            if guess == '\\clues':
                if clues > 0:
                    clue = clue_gen(word,context,guess)
                    context.append(clue)
                    print(clue)
                    clues -= 1
                    print(f"You have only {clues} remaining")
                    continue
                else:
                    print("You are out of clues")
            elif guess == word:
                print("You Have Guessed the Word !")
                break

            guessed.add(guess)


            if guess not in word:
                tries -= 1
                print(f"Wrong Guess! You have {tries} left. If you want clues type \\clues")
                if tries == 0:
                    print("Exhausted all tries. You Lost!")
                    break
    except Exception as e:
        print(f"You Faced This Error:  {e}")



if __name__ == "__main__":
    main()