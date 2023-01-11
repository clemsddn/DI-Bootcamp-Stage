class Cercle():    
    def __init__(self,libelle,rayon,diametre):
        self.rayon=rayon
        self.diametre=diametre
        self.libelle=libelle

    def printRayon(self):
        print(f"Rayon : {self.rayon}")

    def printDiametre(self):
        print(f"Diametre : {self.diametre} ")

    def aireCircle(self):
        from math import pi
        return pi*self.rayon**2

    def imprimerCercle(self):
        print(f"Caracteristiques cercle:\nlibelle :{self.libelle}\nRayon = {self.rayon}\nDiametre = {self.diametre}\nAire = {self.aireCircle()}")
      
    def additionCercle(self,other):
        self.rayon+=other.rayon
        self.diametre+=other.diametre

    @staticmethod
    def comparer(other1,other2):
        if other1.rayon > other2.rayon:
            print(f"{other1.libelle} is great")
        elif other1.rayon < other2.rayon:
            print(f"{other2.libelle} is great")
        else:
            pass
        
           
cercle=Cercle('A',10,30)
cercle.imprimerCercle()
cercle1=Cercle('B',20,30)
cercle.comparer(cercle1,cercle)

cercle.imprimerCercle()
cercle.additionCercle(cercle1)
cercle.comparer(cercle1,cercle)
