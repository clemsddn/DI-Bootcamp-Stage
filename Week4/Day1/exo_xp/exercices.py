# Exercice 1
print(4*"Hello world \n")

#Exercice 2

print((99**3)*8)

#Exercice 3

>>> 5 < 3
False

>>> 3 == 3
 True

>>> 3 == "3"
False

>>> "3" > 3
False

>>> "Hello" == "hello"
False

#Exercice 4

computer_brand="DELL"
print(f"I have a {computer_brand} computer")

#Exercice 5
nom="DINDANE"
prenom="Clement"
age=25
shoe_size=41
info=f"Je suis {nom} {prenom} j'ai {age} ans.\n Je chausse le {shoe_size} et j'adore codé." 
print(info)

#Exercice 6

a=5
b=3
if a>b :
    print("Hello word")

#Exercice 7

nb=float(input("Entrer un nombre :"))
if not nb:
    print(f"Le nombre {nb} n'est ni pair ni impair \n")
elif (nb-int(nb)):
    print(f"Le nombre {nb} est  impair")
elif (nb%2):
    print(f"Le nombre {nb} est  impair")
elif not(nb%2) and nb:
    print(f"Le nombre {nb} est  pair")


#Exercice 8
nom =input("Entrer votre nom :")
if nom.lower()=="clement":
    print(f"Salut {nom}  Tu est mon homonyme.\n Je suis ravie de faire ta connaissance .\n")
else:
    print(f"Salut {nom} je suis Clenent .\n Je suis ravie de faire ta connaissance.\n")

#Exercice 9
taille = float(input("Entrer votre taille en pouces :"))
if (2.54*taille)>145 :
     print("Vous etes assez grand pour rouler.\n")
else:
    print("Vous n'etes pas assez grand pour rouler.\n")
   