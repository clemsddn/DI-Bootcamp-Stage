"""#Exercice 1
class Cat:
    def __init__(self, cat_name, cat_age):
        self.name = cat_name
        self.age = cat_age
dictionnaire={}
cat1=Cat("Minou",2)
dictionnaire[cat1.name]=cat1.age
cat2=Cat("Bob",4)
dictionnaire[cat2.name]=cat2.age
cat3=Cat("Lacy",1)
dictionnaire[cat3.name]=cat3.age

def afficher(dictionnaire):
    return max(dictionnaire,key=dictionnaire.get),max(dictionnaire.values())
    
a,b=afficher(dictionnaire) 
print(f"Le chat le plus âgé est {a} et a {b} des années. ")

#Exercice 2
class Dog:
    def __init__(self,name,height):
        self.name=name
        self.height=height
    def bark(self):
        print(f"\n{self.name}  goes woof! ")
    def jump(self):
        print(f"\n{self.name} jumps {self.height*2} cm high!")

davids_dog=Dog("Rex",50) 
print(f"\nname : {davids_dog.name}\nheight : {davids_dog.height}") 
davids_dog.bark() 
davids_dog.jump()     
    
sarahs_dog=Dog("Teacup",20)
print(f"\nname : {sarahs_dog.name}\nheight : {sarahs_dog.height}") 
sarahs_dog.bark() 
sarahs_dog.jump()

dico={davids_dog.name:davids_dog.height,sarahs_dog.name:sarahs_dog.height}
def bigDog():
    return max(dico,key=dico.get)
    

print(f"{bigDog()} is the big dog")

#Exercice 3
class Song:
    def __init__(self,lyrics):
        self.lyrics=lyrics 
    def sing_me_a_song(self):
        for ly in self.lyrics:
            print(f"\n{ly}")

stairway= Song(["There’s a lady who's sure","all that glitters is gold", "and she’s buying a stairway to heaven"])
stairway.sing_me_a_song()
"""
#Exercice 4
class Zoo():
    def __init__(self,zoo_name):
        self.zoo_name=zoo_name
        self.animals=[]
    def add_animal(self,new_animal):
        if not new_animal in self.animals:
           self.animals.append(new_animal)
    def get_animals(self):
        print(f"{self.zoo_name} animals:")
        for animal in self.animals:
            print(animal)
    def sell_animal(self, animal_sold):
        if animal_sold in self.animals:
            self.animals.remove(animal_sold)
        else:
            print(f"{animal_sold} doesn't existe in the animals list ")
    def sort_animals(self):
        self.animals.sort()
        self.animalDict={}
        for an in self.animals:
            if an[0] in self.animalDict.keys():
                self.animalDict[an[0]].append(an)
            else:
                self.animalDict[an[0]]=[an]
    def get_groups(self):
        print("\nSafari zoo animals groups :\n")
        for let ,an in self.animalDict.items():
            print(f"Group {let} : {an}")
ramat_gan_safari=Zoo("Ramat gan safari")
ramat_gan_safari.add_animal("biche")
ramat_gan_safari.add_animal("pedri")
ramat_gan_safari.add_animal("singe")
ramat_gan_safari.add_animal("pan")
ramat_gan_safari.add_animal("peroquet")
ramat_gan_safari.get_animals()

ramat_gan_safari.sort_animals()
ramat_gan_safari.get_groups()

