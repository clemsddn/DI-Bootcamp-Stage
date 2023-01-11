import re
def ordonnee():

    print("Trier par ordre alphabetique :")
    exp="[a-zA-Z_-]+\s[a-zA-Z_-]+"
    sequence=input("Entrez une sequence de mots en les séparant par des virgules\n==>> ")
    while re.findall(exp,sequence):
        sequence=input("Error: separer les mots  par des virgules\n==>> ")
    liste=sequence.split(",")
    print("Resultat :")
    liste.sort()
    for word in liste:
        print(word,", ",end='')


ordonnee()