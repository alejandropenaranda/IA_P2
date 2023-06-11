class Nodo:
    def __init__(self,puntuacionB,puntuacionN,caballoB, caballoN, puntos,padre=None,operador=None,tipo=None):
        self.puntuacionB = puntuacionB
        self.puntuacionN = puntuacionN
        self.tipo = tipo
        self.padre = padre
        self.puntos = puntos
        self.operador = operador # operador utilizado para que goku llegara a esta posicion
        self.caballoB = caballoB # posicion actual del goku
        self.caballoN = caballoN # posicion actual del goku
        self.utilidad = 0
        if padre is None:
            self.profundidad = 0
        else:
            self.profundidad = padre.profundidad + 1

    # Recorre el arbol desde el nodo actual hasta su padre y luego hacia la raíz.
    def recorrer_arbol_arriba(self, nodos_recorridos=None):
        if nodos_recorridos is None:
            nodos_recorridos = []
        nodos_recorridos.append(self)#Agrega el nodo actual a la lista de nodos recorridos
        if self.padre is not None:
            self.padre.recorrer_arbol_arriba(nodos_recorridos)
        return nodos_recorridos

    def verCamino(self):
        nodos = self.recorrer_arbol_arriba()
        caminoB=[]
        caminoN=[]
        for i in nodos:
            if i.showTipo()=="MAX":
                posicion1=i.showCaballoB()
                posicion2=i.showCaballoN()
                caminoB.append(posicion1)
                caminoN.append(posicion2)
            elif i.showTipo()=="MIN":
                posicion1=i.showCaballoB()
                posicion2=i.showCaballoN()
                caminoB.append(posicion1)
                caminoN.append(posicion2)
        caminoB.reverse()
        caminoN.reverse()
        return caminoB, caminoN
    
    #Verificar si el nodo actual llego a la meta
    def esMeta(self):
        if len(self.puntos) == 0:
            return True
        else:
            return False    
    
    def showPuntuacionB(self):
        return self.puntuacionB

    def showPuntuacionN(self):
        return self.puntuacionN

    def showTipo(self):
        return self.tipo

    def showPuntos(self):
        return self.puntos
    
    def showCaballoB(self):
        return self.caballoB

    def showCaballoN(self):
        return self.caballoN

    def showOperador(self):
        return self.operador
    
    def showProfundidad(self):
        return self.profundidad
    
    def showUtilidad(self):
        return self.utilidad
    
    def funcionUtilidad(self):
        self.utilidad = self.puntuacionB - self.puntuacionN
        return self.showUtilidad()
    
    #Funcion que revisa si hay nodos iguales en una lista de nodos
    def nodo_validoB(self, lista_nodos):
        count = 0
        if self.padre==None:
            return True
        for n in lista_nodos:
            if self.puntos == n.puntos and self.caballoB == n.caballoB:
                count = count+1
        if count>0:
            return False
        else:
            return True