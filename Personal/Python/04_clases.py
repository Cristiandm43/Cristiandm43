class Person:
    def __init__(self, name, surname, age):
        self.fullname = f"{name} {surname}"
        self.name = name
        self.surname = surname 
        self.age = age
    def walk(self):
        print(f"{self.fullname} esta caminando")

my_person = Person("Cristian", "Machado", 19)        
print(my_person.name)
print(my_person.surname)
print(my_person.fullname)
print(f"{my_person.fullname} tiene {my_person.age}")
my_person.walk()



