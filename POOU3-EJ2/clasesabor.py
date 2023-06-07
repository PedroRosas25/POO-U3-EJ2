class Sabor:
    __idsabor=int
    __ingredientes=str
    __nombre=str

    def __init__(self,idsabor,ingredientes,nombre):
        self.__idsabor=idsabor
        self.__ingredientes=ingredientes
        self.__nombre=nombre

    def getIdsabor(self):
        return self.__idsabor
    def getIngredientes(self):
        return self.__ingredientes
    def getNombre(self):
        return self.__nombre    
    
    def __str__(self):
        return '{} {} {}'.format(self.__idsabor,self.__ingredientes,self.__nombre)