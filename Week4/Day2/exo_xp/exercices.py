#Exercice 1

#Quetion 1
my_fav_numbers={3,21,18}

#Quetion 2 
my_fav_numbers.add(10)
my_fav_numbers.add(7)

#Question 3
my_fav_numbers.pop()

#Quetion 4
friend_fav_numbers={2,8,18,5}

#Questio 5
my_fav_numbersfriend_fav_numbersour_fav_numbers=my_fav_numbers.union(friend_fav_numbers)
print(my_fav_numbersfriend_fav_numbersour_fav_numbers)

#Exercice 2
#Question 1
#yes, it is possible .

#Exercice 3
basket = ["Banana", "Apples", "Oranges", "Blueberries"];

#Question 1
basket.remove("Banana")

#Question 2
#basket.remove("Myrtilles")

##Quetion 3
#remove return error when the item doesn't existe
basket.append("Kiwi")

##Quetion 4
basket.append("Apples")

##Quetion 5
c=basket.count("Apples")
print(f"Total Apples : {c}")

#Question 6
basket.clear()

#Question 7
for b in basket:
    print(b)

#Exercice 3
#Question 1

"""The float type in Python represents the floating point number.
 Float is used to represent real numbers and is written with a decimal point dividing the integer and fractional parts.
 For example, 6.08, 90.3+e14"""

#Question 2
for i in range(10):
    print(i+0.25)


#Question 3
liste=[1.5,2,2.5,3,3.5,4,4.5,5]

    
    

#Exercice 5
##Question 1
for i in range(1,21):
    print(i)

##Question 2
for i in range(1,21):
    if not (i-1)%2:
        print(i)

#Exercice 6
##Question 1
name = input("Enter your name :")
while name.capitalize()!="Clement":
    name = input("Enter your name :")

#Exercie 7
##Question 1
fruits=input("""Entrer vos fruit(s) prefere(s) en les separant par un seul espace  
 Exemple: apple mango cherry
 ==>""")
liste=fruits.split()
fruit=input("Entrer le nom d'un fruit:")
if  fruits.count(fruit):
    print("You chose one of your favorite fruits! Enjoy!")
else:
    print("You chose a new fruit. I hope you enjoy!")

 

#Exercice 9
##Question 1
garniture=input("Entrer une garniture pour  votre pizza :")
lgarniture=[garniture]
prix_garniture=2.5
while garniture!="quitter":
    print(f"Nous ajoutons {garniture} a votre pizza")
    lgarniture.append(garniture)
    garniture=input("Entrer une ganiture ou <<quitter>> pour quitter :\t")
print(f"Liste de vos garnitures :")
for g in lgarniture:
    print(f"{g} prix = 2.5 ")
print(f"\n Prix total :10 + {len(lgarniture)*2.5}")


#Exercice 10
##Question 1
nb=int(input("Donnez le nombre de personnes:\t "))
cout=0
for n in range(nb):
    name=input(f"Le nom de la personne numero {n+1}:\t")
    age=int(input(f"L'age de la personne numero {n+1}:\t"))
    if age <3:
        print(f"Entrer gratuit pour {name}")
    elif age>=3 and age<=12:
        print(f"Payez 10 $ pour {name}")
        cout+=10
    elif age>12:
        print(f"Payez 15 $ pour {name}")
        cout+=15
print(f"Votre facture est de : {cout} $")

##Question 2
