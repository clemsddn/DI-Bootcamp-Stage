class Pets():
    def __init__(self, animals):
        self.animals = animals

    def walk(self):
        for animal in self.animals:
            print(animal.walk())

class Cat():
    is_lazy = True

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def walk(self):
        return f'{self.name} is just walking around'

class Bengal(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Chartreux(Cat):
    def sing(self, sounds):
        return f'{sounds}'

class Siamese(Cat):
    pass

all_cats=[Bengal('Milou',2),Chartreux('Boby',5),Siamese('Rex',1)]

sara_pets=Pets(all_cats)
sara_pets.walk()


#Exercice 2
class Dog :
    def __init__(self,name, age, weight):
        self.name=name
        self.age=age
        self.weight=weight

    def bark(self):
        return f'{self.name} is barking'

    def run_speed(self):
        return (self.weight/self.age*10)
    
    def fight (self,other_dog):
        if (self.run_speed()*self.weight)>(other_dog.run_speed()*other_dog.weight):
            return f'{self.name} win !'
        elif (self.run_speed()*self.weight)<(other_dog.run_speed()*other_dog.weight):
            return f'{other_dog.name} win'

dog1=Dog('Non',8,50)
dog2=Dog('Rex',3,45)
dog3=Dog('Bobly',4,53)

print(f'\n{dog1.fight(dog2)}')
print(f'\n{dog1.fight(dog3)}')



