from colorama import Fore

from data.word import Word
from words_logic import WordLogic


class Termo:
    MAX_ATTEMPTS = 6
    
    def __init__(self):

        w = Word()
        self.correct_word = w.word
        
        self.attempts = list()


    def can_attempt(self):
        if len(self.attempts) > 0 and (self.attempts[-1] != self.correct_word and len(self.attempts) < self.MAX_ATTEMPTS):
            return True
        elif len(self.attempts) == 0:
            return True
        return False


    def attempt(self, word):
       
        wl = WordLogic(self.attempts)

        if word and len(word) != 5:
            wl.show_attempts(self.correct_word) 
            print(Fore.RED + "\nPalavra inválida.\n" + Fore.RESET)
            return False

        self.attempts.append(word)
        
        wl.show_attempts(self.correct_word)

        if word == self.correct_word:
            print(Fore.GREEN + "\nParabéns, você acertou!\n" + Fore.RESET)
            return True
        
        elif len(self.attempts) <= self.MAX_ATTEMPTS - 1:
            print(Fore.YELLOW + "\nQuase...\n" + Fore.RESET)
        
        else:
            print(Fore.RED + "\nTentativas esgotadas!\nPalavra correta: " + self.correct_word + Fore.RESET)

    @property
    def show_grid(self):
        print("┏" + "━" * 11 + "┓")
        
        for _ in range(6):
            print ("┃ " + "_ " * 5 + "┃")
        
        print("┗" + "━" * 11 + "┛")

    @property
    def got_it(self):
        return (True if (len(self.attempts) > 0 and self.correct_word == self.attempts[-1]) else False)


