lexicon = {
        "merry":"god", 
        "christmas":"jul", 
        "and":"och",
        "happy":"gott",
        "new":"nytt", 
        "year":"ar"
                }
def translate(words):
    return ' '.join(list(map(lambda word: lexicon.get(word,word),words)))

english_words = ["merry", "christmas", "and", "happy", "new", "year"]

print(translate(english_words))