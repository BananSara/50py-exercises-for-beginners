dictionary = {
    "merry":"god",
    "christmas":"jul",
    "and":"och", 
    "happy":"gott",
    "new":"nytt",
    "year":"ar"
    }
def translate(words):
    swedish = []
    for word in words:
        if word in dictionary:
            swedish.append(dictionary[word])
        else:
            print('invalid!')
    return swedish

english_sentence = ["merry", "christmas", "and", "happy", "new", "year"]
print(translate(english_sentence))
