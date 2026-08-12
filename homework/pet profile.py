class Pet:
    print("Pet class is created")
pet_object=Pet()
class PetProfile:
    category="pet"
    def __init__(self,name,animal_type,age,favourite_food):
        self.name=name
        self.animal_type=animal_type
        self.age=age
        self.favourite_food=favourite_food
pet1=PetProfile("Tom","Cat",2,"Fish")
pet2=PetProfile("Bruno","Dog",4,"Chicken")
print(pet1.category)
print(pet2.category)
print(pet1.name)
print(pet1.animal_type)
print(pet1.age)
print(pet1.favourite_food)
print(pet2.name)
print(pet2.animal_type)
print(pet2.age)
print(pet2.favourite_food)