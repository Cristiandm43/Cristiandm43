def is_anagram(first_word, second_word):
    if first_word.lower() == second_word.lower():
        return False 
    return sorted(first_word.lower()) == sorted(second_word.lower())

first_word = input("Inserta la primera palabra: ")
second_word = input("Inserta la segunda palabra: ")

print(is_anagram(first_word , second_word))