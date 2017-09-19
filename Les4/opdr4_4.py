def set_password(old_password, new_password):
    if old_password != new_password and len(new_password) > 6 and has_minimal_numbers(new_password, 1):
        return True
    else:
        return False


def has_minimal_numbers(text, count):
    number_count = 0
    for char in text:
        if char.isdigit():
            number_count += 1
    return number_count >= count


invalid_same_password = set_password("123456", "123456")
invalid_short_password = set_password("passw0rd", "1234")
invalid_text_password = set_password("abc123", "qwerty")
valid_password = set_password("letmein", "password1")

print("Resultaat zelfde wachtwoord: {0}".format(invalid_same_password))
print("Resultaat te kort wachtwoord: {0}".format(invalid_short_password))
print("Resultaat wachtwoord zonder nummers: {0}".format(invalid_text_password))
print("Resultaat geldig wachtwoord: {0}".format(valid_password))