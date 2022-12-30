#Exercice 1

def display_message():
    print("\nSalut tout le monde coder avec python c'est trop geniale !\n")

display_message()

#Exercice 2
def favorite_book(title):
    print(f"One of my favorite books is <{title}>")
favorite_book("La chasse au hacker")
#Exercice 3
def describe_city(country,city):
    print(f"\n{city} is in {country}")

describe_city("Burkina","Tenkodogo")
#Exercice 4
def aleatoire():
    import random as r
    x=0
    a=r.randint(1,100)
    nb=int(input("Enter a integer number between 1 and 100 :"))
    c=2
    while x<2 :
        nb=int(input(f"il vous reste {c} chance(s) essayer encore :"))
        x +=1
        c -=1
        if nb == a:
            print("\nYou win!")
            break
       
    else:
        print("\nYou lost ")
        print(f"The numbers are {nb} and {a}")
aleatoire()

#Exercice 5
def make_shirt(text,size):
    print(f"\nLa taille de la chemise est {size} .\n Le texte est {text}")

make_shirt("Python","M")
def make_shirt_size(text,size="XXL"):
    
    print(f"\nLa taille de la chemise est {size} .\n \nLe texte est {text}")

make_shirt_size("J'aime Python")


def make_shirt_text(size,text="J'aime Python"):
    print(f"\nLa taille de la chemise est {size} .\n Le texte est {text}")

make_shirt_text("xxl")
make_shirt_text("M")
make_shirt("Burkina","L")
make_shirt(text="Burkina",size="L")

#Exercie 6
magician_names = ['Harry Houdini', 'David Blaine', 'Criss Angel']

def show_magicians(liste):
    for mg in liste:
        print("\n",mg)
show_magicians(magician_names)

def make_great(liste):
    for i in range(len(liste)):
        liste[i]="the Great "+liste[i]
make_great(magician_names)
show_magicians(magician_names)

#Exercice 7
def get_random_temp():
    import random as r
    return r.randint(-10,40)

print(get_random_temp())

def main():
    print(f"La température actuelle est de {get_random_temp()} degrés Celsius")

def mainc():
    a=get_random_temp()
    if not a:
        print("\nBrrr, c’est glacial! Portez des couches supplémentaires aujourd’hui ")
    elif a>0 and a<=16:
        print("\nAssez froid! N’oublie pas ton manteau ")
    elif a>16 and a<=23 :
        print("\nIl fait froid ")
    elif a>23 and a<24 :
        print("\nAh1! le beau temps")
    elif a>=24 and a<32 :
        print("\n Il fait quand bien me;e un peu chaud ")
    elif a>=32 and a<=40 :
        print("\nQuel chaleur ?")

def get_random_tempc(saison):
    import random as r
    if saison.lower()=="hiver":
        return r.randint(-10,16)
    elif saison.lower()=="printemps":
        return r.randint(16,23)
    elif saison.lower()=="automne":
        return r.randint(24,32)
    elif saison.lower()=="ete":
        return r.randint(32,40)
    else:
        print("Cette saison n'existe pas !")




def maincf():
    saison=input("Entrer une saison :")
    a=get_random_tempc(saison)
    if not a:
        print("\nBrrr, c’est glacial! Portez des couches supplémentaires aujourd’hui ")
    elif a>0 and a<=16:
        print("\nAssez froid! N’oublie pas ton manteau ")
    elif a>16 and a<=23 :
        print("\nIl fait froid ")
    elif a>23 and a<24 :
        print("\nAh1! le beau temps")
    elif a>=24 and a<32 :
        print("\n Il fait quand bien me;e un peu chaud ")
    elif a>=32 and a<=40 :
        print("\nQuel chaleur ?")

maincf()

def get_random_tempcm(saison):
    import random as r
    if saison >0 and saison<=3:
        return r.randint(-10,16)
    elif saison >3 and saison<=6:
        return r.randint(16,23)
    elif saison >6 and saison<=9:
        return r.randint(24,32)
    elif saison >9 and saison<=12:
        return r.randint(32,40)
    else:
        print("Ce mois n'existe pas !")
        return 100


def maincmois():
    saison=int(input("Entrer le numero d'un mois :"))
    a=get_random_tempcm(saison)
    if not a:
        print("\nBrrr, c’est glacial! Portez des couches supplémentaires aujourd’hui ")
    elif a>0 and a<=16:
        print("\nAssez froid! N’oublie pas ton manteau ")
    elif a>16 and a<=23 :
        print("\nIl fait froid ")
    elif a>23 and a<24 :
        print("\nAh1! le beau temps")
    elif a>=24 and a<32 :
        print("\n Il fait quand bien me;e un peu chaud ")
    elif a>=32 and a<=40 :
        print("\nQuel chaleur ?")

maincmois()
