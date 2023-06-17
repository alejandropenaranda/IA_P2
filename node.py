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
        self.eleccion = None
        self.revisado = revisado
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
                    self.utilidad = max(utilidades_validas)
                else:  # Profundidad impar
                    self.utilidad = min(utilidades_validas)
            return self.utilidad

    def cosa(self):
        nodos=self.recorrer_arbol_arriba()
        a=nodos.pop(-1)
        a.calcular_utilidad()
        print("Utilidad Raiz:",a)

    def agregar_hijo(self, hijo):
        self.hijos.append(hijo)
        hijo.padre = self

    def agregar_hijos(self, hijos): 
        self.hijos.extend(hijos)
        caminoB=[]
        caminoN=[]
        for i in self.showHijos():
            caminoB.append(i.showCaballoB())
            caminoN.append(i.showCaballoN())
        print("Hijos con B",caminoB)
        print("Hijos con N",caminoN)

    def subirUtilidad(self):
        nodos=self.recorrer_arbol_arriba()
        #nodos.reverse()
        a=nodos[0].showUtilidad()
        #print("UTILIDAD NODO TERMINAL:",a)

        for i in nodos:
            if i.padre == None:
                pass
            elif i.padre.showRevisado()==False:
                i.padre.utilidad = i.showUtilidad()
                i.padre.eleccion = i
                # print("Utilidad Padre:",i.padre.utilidad)
                # print("Revisado:",i.padre.revisado)
                # print("---")
                i.padre.revisado = True
            elif i.padre.showRevisado()==True and i.padre.showTipo()=="MIN":
                #i.padre.utilidad = min(i.padre.utilidad,i.showUtilidad())
                if i.padre.utilidad>i.showUtilidad():
                    i.padre.utilidad = i.showUtilidad()
                    i.padre.eleccion = i
                #print("Utilidad Padre:",i.padre.utilidad)
            elif i.padre.showRevisado()==True and i.padre.showTipo()=="MAX":
                #i.padre.utilidad = max(i.padre.utilidad,i.showUtilidad())
                if i.padre.utilidad<i.showUtilidad():
                    i.padre.utilidad = i.showUtilidad()
                    i.padre.eleccion = i



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