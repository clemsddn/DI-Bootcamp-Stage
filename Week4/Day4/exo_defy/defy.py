import os
import re
matrix =[
    [7,'i',3],
    ['T','s','i'],
    ['h','%','x'],
    ['i',' ','#'],
    ['s','M',' '],
    ['&','a',' '],
    ['#','t','%'],
    ['^','r','!']
        ]

for m in matrix:
    print("\n\t_____________________________________________")
    for n in m:
        print("\t  ",n,"  |  ",end="")
print("\n\t_____________________________________________")

chaine=''
phrase=list(zip(*matrix))

for seg in phrase:
    for x in seg:
        chaine+=str(x)
def decriptage(chai):
    
    sc_list = '[@_!#$%^&*()<>?}{~:]+'
    res=re.findall(sc_list,chai)
    rese=re.sub(sc_list,' ',chai)
    chaine_liste=list(rese)


    dig=[]
    for sy in chaine_liste:
        if sy.isdigit():
            dig.append(sy)
    for d in dig:
        chaine_liste.remove(d)
    return "".join(chaine_liste)

print(f"\nDecripter vos messages comme par exemple le  text du tableau ci dessus :\n \t Resultat ======>>> {decriptage(chaine)}\n")

print("""\t \t#######################################################################################################
    \t \t#######################################################################################################""")
def main():
    chain=input("\nEntrer une chaine :")
    print(f"\nLe message est :\n=======>>> {decriptage(chain)}")

main()
os.system("pause")