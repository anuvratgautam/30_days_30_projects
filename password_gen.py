import string
import secrets

class pwd_generator():
    """ 
    Class To Generate Passwords
    """
    def __init__(self,length: int,uppercase: bool,symbols: bool):
        """
        Class Contructor to Initialize the Length Of the Password, 
        If it Should Contain UpperCase Letters, If it Should Contain Symbols

        """
        self.length: int = length
        self.uppercase: bool = uppercase
        self.symbols: bool= symbols

    def check_uppercase(self,password: str)->bool:
        """
        Function to check if the password contains UpperCase Letters
        """
        for char in password:
            if char in string.ascii_uppercase:
                return True
        return False

    def check_symbols(self,password: str)->bool:
        """
        Function to check if the password contains Symbols
        """
        for char in password:
            if char in string.punctuation:
                return True
        return False

    def generator(self)->str:
        """
        Function To Generate the Password using the Secrets Module 
        """
        combination: str = string.ascii_lowercase+string.digits

        if self.uppercase:
            combination += string.ascii_uppercase

        if self.symbols:
            combination += string.punctuation

        combination_len = len(combination)
        new_password: str = ""

        for _ in range(self.length):
            new_password += combination[secrets.randbelow(combination_len)]

        return new_password

    def generate(self):
        """
        Function to be used by user to Generate and access the password
        """
        password = self.generator()
        print(f"Your Password is :{password} U:{self.check_uppercase(password)} S:{self.check_symbols(password)}")

def bool_check(user: str):
    """
    Function to check the user input and convert it to boolean equivalent
    """
    if user.lower() == 'y':
        return True
    return False

def main()-> None:
    """
    Main Function
    """
    length = int(input("Enter The Length of The Password : "))
    upper = input("Upper Case ? y/n : ")
    symbol = input("Symbols ? y/n : ")

    pwd = pwd_generator(length=length,uppercase=bool_check(upper),symbols=bool_check(symbol))
    pwd.generate()


if __name__ == "__main__":
    main()
