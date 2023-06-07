from clasehelado import Helado
from collections import Counter
class ManejaHelados:
    listahelados=[]

    def __init__(self):
        self.listahelados=[]

    def registrarventa(self,ms):
        i=0
        gramos=input('Ingrese peso del helado en gramos ')
        precio=int(int(gramos)*2)
        unaventa=Helado(gramos,precio)
        print('SABORES DISPONIBLES: ')
        ms.mostrarsabores()
        cantsabores=int(input('Ingrese cantidad de sabores '))
        for i in range(cantsabores):
            cod=int(input('Ingrese codigo del sabor numero:{} '.format(i+1)))
            sabor=ms.getSabor(cod)
            unaventa.addsabor(sabor)
        self.listahelados.append(unaventa)    
        print('Helado registrado con exito ')

    def mostrarmas(self):
        print('Sabores de helado mas pedidos: ')
        saborescontador=Counter()
        for helado in self.listahelados:
            for sabor in helado.getSabores():
                saborescontador[sabor]+=1
        saboresordenados=saborescontador.most_common(5)
        for sabor, contador in saboresordenados:
            print('{}: {} veces'.format(sabor,contador))        

    def totalgramos(self,ms):
        grtotales=0
        codigo=int(input('Ingrese codigo de helado a buscar '))
        nombre=ms.getSabor(codigo)
        for i in range(len(self.listahelados)):
            grtotales+=self.listahelados[i].getTotal(nombre)
        print ('Se vendio un total de: {} gramos, para el helado: {}'.format(grtotales,nombre))    

    def mostrarsabores(self):
        s=''
        tamaño=int(input('Ingrese peso del helado en gramos a buscar '))
        print ('Listado de sabores con el tamaño ingresado')
        for helado in self.listahelados:
            if helado.getGramos() == tamaño:
                for sabor in helado.getSabores():
                    if sabor not in s:
                        print('\t{}'.format(sabor))
                        s+=sabor + ', '
           
    def importetotal(self,ms):
        tot1=0
        tot2=0
        tot3=0
        tot4=0
        tot5=0
        for i in range(len(self.listahelados)):
            gr=int(self.listahelados[i].getGramos())
            if gr==100:
                tot1+=int(self.listahelados[i].getPrecio())
            elif gr==150:
                tot2+=int(self.listahelados[i].getPrecio())
            elif gr==250:
                tot3+=int(self.listahelados[i].getPrecio())
            elif gr==500:
                tot4+=int(self.listahelados[i].getPrecio())
            elif gr==1000:
                tot5+=int(self.listahelados[i].getPrecio())  
        print ('Importes totales para gramos:')
        print('100gr:{} 150gr:{} 250:{} 500gr:{} 1000gr:{}'.format(tot1,tot2,tot3,tot4,tot5))                     



    def mostrarhelados(self):
        for i in range(len(self.listahelados)):
            print('Venta numero {}: {}'.format(i+1,self.listahelados[i]))

            

