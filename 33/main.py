
def semordnilap(file_path):
    file_path = r'C:\Users\Sara\Desktop\50py exercises for beginners\33\33.txt'
    file =  open(file_path,'r')
    words = [line.strip() for line in file]

    for word in words:
        a = word
        reversed = a[::-1]
        if reversed in words and word != reversed:
            print(f'{reversed} and {a} are semornilap')

semordnilap(r'C:\Users\Sara\Desktop\50py exercises for beginners\33\33.txt')


