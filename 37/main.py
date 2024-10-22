def text_file():
    count = 0
    output_lines = []
    
    input_file = input('please enter your file: ')
    
    file_path = open(input_file, 'r')
    for line in file_path:
        count += 1 
        output_lines.append(f"{count}: {line}")
    
    new_file = 'numbered_file.txt'
    with open(new_file, 'w') as file:
        file.writelines(output_lines)
    return new_file


new_file = text_file()
print(f"New file created: {new_file}")