def filter_long_words(word,int):
    longest = []
    for i in word:
        if len(i) > int:
            longest.append(i)
    return (longest)

print(filter_long_words(['apple','orange','cat'], 4))
