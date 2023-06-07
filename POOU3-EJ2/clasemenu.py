class menu:
    __opcion=int
    
    def __init__(self):
        self.__opcion=0

    def menuopciones(self,mh,ms):
        while self.__opcion!=7:
            print ('1-- Registrar helado vendido\n2--Mostrar nombres de los mas pedidos\n3--Estimar total de gramos vendidos\n4--Mostrar los sabores vendidos del tamaño ingresado\n5--Importe total recaudado por la heladeria\n6--Mostrar helados vendidos\n7--SALIR')
            self.__opcion=int(input('Ingrese una opcion '))
            if self.__opcion==1:
                mh.registrarventa(ms)
            if self.__opcion==2:
                mh.mostrarmas()
            if self.__opcion==3:
                mh.totalgramos(ms)
            if self.__opcion==4:
                mh.mostrarsabores()
            if self.__opcion==5:
                mh.importetotal(ms)
            if self.__opcion==6:
                mh.mostrarhelados()
            if self.__opcion==7:    
                print ('SALIENDO DEL PROGRAMA ')