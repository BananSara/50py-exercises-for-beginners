def char_freq_table():
    # Get the file name from the user
    file_path = input("Please enter the file name: ")

    try:
        # Open the file and read its contents
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()

        # Initialize an empty dictionary for character frequencies
        char_freq = {}

        # Iterate over each character in the file and count its frequency
        for char in text:
            if char in char_freq:
                char_freq[char] += 1
            else:
                char_freq[char] = 1

        # Sort the characters by frequency, then by character (alphabetical)
        sorted_char_freq = sorted(char_freq.items(), key=lambda x: (-x[1], x[0]))

        # Print the character frequency table
        print("\nCharacter Frequency Table:")
        print(f"{'Character':^10} | {'Frequency':^10}")
        print("-" * 25)
        for char, freq in sorted_char_freq:
            # Display whitespace characters like spaces and newlines
            if char == " ":
                char_display = "' ' (Space)"
            elif char == "\n":
                char_display = "\\n (Newline)"
            elif char == "\t":
                char_display = "\\t (Tab)"
            else:
                char_display = f"'{char}'"
            print(f"{char_display:^10} | {freq:^10}")

    except FileNotFoundError:
        print("The file was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

# Run the function
char_freq_table()
