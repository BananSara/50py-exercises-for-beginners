text_input = "Was it a rat I saw?"
def clean_text(text):
    cleaned = []
    for char in text:
        if char.isalpha():
            cleaned.append(char)
        else:
            pass
    return (''.join(cleaned)).lower()

#  clean_text is a function. cleaned_text is variable which holds output of clean_text function. reveresed... holds reveresed of cleaned_text variable.
cleaned_text = clean_text(text_input)
reversed_cleaned_text =cleaned_text[::-1]

if cleaned_text == reversed_cleaned_text:
    print("IS PALINDROME!")
else:
    print("IS NOT PALINDROME")










