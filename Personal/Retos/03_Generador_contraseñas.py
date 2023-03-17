import random
import string


def password_generator(length , includes_capitals = True , includes_numbers = True, includes_symbols = True):

    characters = string.ascii_lowercase
    if includes_capitals:
        characters += string.ascii_uppercase
    if includes_numbers:
        characters += string.digits
    if includes_symbols:
        characters += string.punctuation
    
    password = "".join(random.choice(characters) for i in range(length))
    
    return password

password = password_generator(length = 16 , includes_capitals = True, includes_numbers = True, includes_symbols = True)
print(password)


