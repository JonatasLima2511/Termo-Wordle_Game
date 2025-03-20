from random import choice

class Word:

    word = ""

    def __init__(self):
        self.word = self.get_random_word().upper()

    def get_random_word(self):
        
        with open("data\\words_dataset-filtered.txt", "r", encoding = "utf-8") as words:
            word_list = list()
            
            for w in words.readlines():
                word_list.append(w[:5])

        return choice(word_list)
            
