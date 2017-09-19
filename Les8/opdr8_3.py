def code(text):
    new_text = ""
    for char in text:
        char_num = ord(char)
        new_text += chr(char_num + 3)
    return new_text

result = input("Voer tekst in: ")
print(code(result))
