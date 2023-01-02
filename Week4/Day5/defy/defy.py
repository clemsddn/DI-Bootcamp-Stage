def ordonnee():
    print("Trier par ordre alphabetique :")
    sequence=input("Entrez une seauence de mots en les séparant par des virgules\n==>> ")
    liste=sequence.split(",")
    print("Resultat :")
    liste.sort()
    for word in liste:
        print(word,", ",end='')


ordonnee()