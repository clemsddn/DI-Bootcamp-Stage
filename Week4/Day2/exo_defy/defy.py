#Defy 1
"""print("Liste de multiples ")
nombre=int(input("Enter un nombre :"))
taille =int(input("Entrer le nombre de multiples :"))
listeMultiple=[]
i=1
while len(listeMultiple)<taille:
    listeMultiple.append(i*nombre)
    i+=1
print(f"Nombre:{nombre} - taille {taille} -> {listeMultiple}")
"""
#Defy 2
chaine = input("Entrer une chaine :")
ch=chaine[0]
for c in chaine:
      if ch[-1]!=c:
        ch+=c
            
       
print(ch)