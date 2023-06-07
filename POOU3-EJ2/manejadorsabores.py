import csv
from clasesabor import Sabor
class ManejaSabores:
    listasabores=[]

    def __init__(self):
        listasabores=[]

    def cargarsabores(self):
        archivo = open("sabores.csv")
        reader = csv.reader (archivo,delimiter=";")
        for fila in reader:
            idsabor=int(fila[0])
            ingredientes=str(fila[1])
            nombre=str(fila[2])
            unsabor=Sabor(idsabor,ingredientes,nombre)
            self.listasabores.append(unsabor)

    def mostrarsabores(self):
        print('LISTA SABORES ')
        for i in range(len(self.listasabores)):
            print ('{}'.format(self.listasabores[i]))      

    def getSabor(self,cod):
        return self.listasabores[cod-1].getNombre()   
      