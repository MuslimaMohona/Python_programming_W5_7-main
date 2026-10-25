DELIMITER = ','

def collectWords():
    words = ""
    while True:
        word = input("Insert word (empty stops): ")
        if word == "":
            break
        if words == "":
            words = word
        else:
            words += DELIMITER + word
    return words

def analyseWords(words):
    if words == "":
        amount = 0
        characters = 0
    else:
        delimiters = words.count(DELIMITER)
        amount = delimiters + 1
        characters = len(words) - delimiters
    if amount > 0:
        average = characters / amount   
    else:
        average = 0 
   
    print(f" - {amount} Words")
    print(f" - {characters} Characters")
    print(" - {:.2f} Average word length".format(average))

def main():
    print("Program starting.")
    words = collectWords()
    analyseWords(words)
    print("Program ending.")
main()
