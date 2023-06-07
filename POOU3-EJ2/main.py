from manejadorhelados import ManejaHelados as MH
from manejadorsabores import ManejaSabores as MS
from clasemenu import menu

if __name__=='__main__':
    mh=MH()
    ms=MS()
    m=menu()
    ms.cargarsabores()
    m.menuopciones(mh,ms)
