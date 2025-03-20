def valid_word(word):
    for l in word:
        if ord(l) < 97 or ord(l) > 122:
            return False
    return True


with open("data\\words_dataset.txt", "r") as words:
    
    word_list = list()

    for w in words.readlines():
        if len(w) == 6 and not(w in word_list):
            word_list.append(w[:5])

if word_list:
    with open("data\\words_dataset-filtered.txt", "w") as words:
        for w in word_list:
            
            if valid_word(w):
                words.write(w + "\n")
            