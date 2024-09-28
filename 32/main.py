file_path = r'C:\Users\Sara\Desktop\50py exercises for beginners\32\32.txt'
file =  open(file_path, 'r')

for line in file:
    line = line.strip() #remove tailing and leading whitespace
    if line == line[::-1]: 
        print('Palindrome:', line)