class Helado:
    __gramos=float
    __precio=float
    __sabores=list
    
    def __init__(self,gramos,precio):
        self.__gramos=gramos
        self.__precio=precio
        self.__sabores=[]

    def addsabor(self,sabor):
        self.__sabores.append(sabor)

    def getGramos(self):
        return int(self.__gramos)
    def getPrecio(self):
        return self.__precio
    def getSabores(self):
        return self.__sabores
    
    def getTotal(self,nombre):
        total=0
        if nombre in self.__sabores:
            total+=int(self.__gramos)/int(len(self.__sabores))
            return total    
            
    def mostrarSabores(self,l):
        for i in range(len(self.__sabores)):
            if self.__sabores[i] not in list(l):
                list(l).append(self.__sabores[i])
                print('{}'.format(l[i]))        
        return list(l)        

    def __str__(self):
        i=0
        s=''
        for i in range(len(self.__sabores)):
            s+=self.__sabores[i]
            s+=', '
        return 'Peso:{} Precio:{} sabores: {}'.format(self.__gramos,self.__precio,s)    