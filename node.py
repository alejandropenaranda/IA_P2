class Nodo:
    def __init__(self,puntuacionB,puntuacionN,caballoB, caballoN, puntos,padre=None,operador=None,tipo=None,revisado=False):
        self.puntuacionB = puntuacionB
        self.puntuacionN = puntuacionN
        self.tipo = tipo
        self.padre = padre
        self.puntos = puntos
        self.operador = operador # operador utilizado para que goku llegara a esta posicion
        self.caballoB = caballoB # posicion actual del goku
        self.caballoN = caballoN # posicion actual del goku
        self.utilidad = None
        self.hijos = []
        if padre is None:
            self.profundidad = 0
        else:
            self.profundidad = padre.profundidad + 1

    def calcular_utilidad(self):
        if not self.hijos:  # Nodo de última profundidad
            return self.utilidad
        else:
            utilidades_hijos = [hijo.calcular_utilidad() for hijo in self.hijos]
            utilidades_validas = [utilidad for utilidad in utilidades_hijos if utilidad is not None]
            if utilidades_validas:
                if self.profundidad % 2 == 0:  # Profundidad par
                    self.utilidad = max(utilidades_validas)/(self.profundidad+7)
                else:  # Profundidad impar
                    self.utilidad = min(utilidades_validas)/(self.profundidad+7)
            return self.utilidad

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        hijo.padre = self

    # Recorre el arbol desde el nodo actual hasta su padre y luego hacia la raíz.
    def recorrer_arbol_arriba(self, nodos_recorridos=None):
        if nodos_recorridos is None:
            nodos_recorridos = []
        nodos_recorridos.append(self)#Agrega el nodo actual a la lista de nodos recorridos
        if self.padre is not None:
            self.padre.recorrer_arbol_arriba(nodos_recorridos)
        return nodos_recorridos
    
    #Verificar si el nodo actual llego a la meta
    def esMeta(self):
        if len(self.puntos) == 0:
            return True
        else:
            return False

    def showHijos(self):
        return self.hijos   
    
    def showPuntuacionB(self):
        return self.puntuacionB

    def showPuntuacionN(self):
        return self.puntuacionN

    def showTipo(self):
        return self.tipo

    def showRevisado(self):
        return self.revisado

    def showEleccion(self):
        return self.eleccion

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