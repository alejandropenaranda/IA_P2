class Nodo:
    def __init__(self,puntuacionB,puntuacionN,caballoB, caballoN, puntos,padre=None,operador=None):
        self.puntuacionB = puntuacionB
        self.puntuacionN = puntuacionN
        self.padre = padre
        self.puntos = puntos
        self.operador = operador # operador utilizado para que goku llegara a esta posicion
        self.caballoB = caballoB # posicion actual del goku
        self.caballoN = caballoN # posicion actual del goku
        self.primerobjetivo = 0
        self.val_heuristica = 0
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
    
    #Verificar si el nodo actual llego a la meta
    def esMeta(self):
        if len(self.bolas) == 0:
            return True
        else:
            return False    
    
    def showPuntuacionB(self):
        return self.puntuacionB

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
    
    #Funcion que verifica si goku puede devolverse, comparando el nodo "abuelo" con el nuevo nodo
    def nodo_puede_devolverse(self):
        if self.padre==None:
            return True
        elif self.padre.padre == None:
            return True
        elif self.bolas != self.padre.padre.bolas or self.freezers != self.padre.padre.freezers or self.cells != self.padre.padre.cells or self.semillas != self.padre.padre.semillas:
            return True
        else:
            return False
    
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

    def nodo_validoN(self, lista_nodos):
        count = 0
        if self.padre==None:
            return True
        for n in lista_nodos:
            if self.puntos == n.puntos and self.caballoN == n.caballoN:
                count = count+1
        if count>0:
            return False
        else:
            return True

    #Funcion que compara la posicion del nodo nuevo con la de su nodo "abuelo"
    def comparar_posicion(self):
        if self.padre==None:
            return True
        elif self.padre.padre == None:
            return True
        elif self.showKakaroto() == self.padre.padre.showKakaroto():
            return True
        else:
            return False

    def eliminarSemilla(self, semilla):
        self.semillas.remove(semilla)
        return self.semillas

    def eliminarBola(self, bola):
        self.bolas.remove(bola)
        return self.bolas
    
    def definir_primer_objetivo(self,objetivo):
        self.primerobjetivo = objetivo

    def showValHeuristica(self):
        return self.val_heuristica
    
    def heuristica(self):
        if len(self.bolas)==2:
            aux = abs(self.bolas[0][0]-self.kakaroto[0]) + abs(self.bolas[0][1]-self.kakaroto[1])
            aux2 = abs(self.bolas[1][0]-self.kakaroto[0]) + abs(self.bolas[1][1]-self.kakaroto[1])
            if aux>aux2:
                self.definir_primer_objetivo(1)
            else:
                self.definir_primer_objetivo(0)

            if self.primerobjetivo == 0:
                distancia1 = abs(self.bolas[0][0]-self.kakaroto[0]) + abs(self.bolas[0][1]-self.kakaroto[1])
                distancia2 = abs(self.bolas[0][0]-self.bolas[1][0]) + abs(self.bolas[0][1]-self.bolas[1][1])
                self.val_heuristica = distancia1 + distancia2
                return self.showValHeuristica()
            else:
                distancia1 = abs(self.bolas[1][0]-self.kakaroto[0]) + abs(self.bolas[1][1]-self.kakaroto[1])
                distancia2 = abs(self.bolas[0][0]-self.bolas[1][0]) + abs(self.bolas[0][1]-self.bolas[1][1])
                self.val_heuristica = distancia1 + distancia2
                return self.showValHeuristica()
        elif len(self.bolas) == 1:
            aux =  abs(self.bolas[0][0]-self.kakaroto[0]) + abs(self.bolas[0][1]-self.kakaroto[1])
            self.val_heuristica = aux
            return self.showValHeuristica()
        else:
            self.val_heuristica = 0
            return self.showValHeuristica()
    
    def heuristicaCosto(self):
        self.heuristica()
        return self.showCosto() + self.showValHeuristica()