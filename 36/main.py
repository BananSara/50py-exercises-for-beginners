def hapaxes():
    file_path = input('enter your file name: ')
    # file_path = r"C:\Users\Sara\Desktop\50py exercises for beginners\36\36.txt"
    with open(file_path, 'r') as file:
        words = file.read().lower().split()
    
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1  
        else:
            word_counts[word] = 1  

    hapaxes = []
    for word, count in word_counts.items():
        if count == 1:
            hapaxes.append(word)
            
    return hapaxes 
print(hapaxes())