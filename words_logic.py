from colorama import Fore

class WordLogic:

    in_position = False
    
    def __init__ (self, attempts: list):
        self.attempts_list = attempts


    def show_attempts(self, correct_word):

        print("┏" + "━" * 11 + "┓")

        for w in self.attempts_list:
            
            print("┃ ", end = "")

            for index, letter in enumerate(w):
                
                in_position = letter == correct_word[index]

                if letter in correct_word:
                    if in_position:
                        print(Fore.GREEN + letter + Fore.RESET, end = " ")
                    else:
                        print(Fore.YELLOW + letter + Fore.RESET, end = " ")
                else:
                    print(Fore.WHITE + letter + Fore.RESET, end = " ")
            
            print("┃")
        
        for _ in range(6 - len(self.attempts_list)):
            print ("┃ " + "_ " * 5 + "┃")

        print("┗" + "━" * 11 + "┛")