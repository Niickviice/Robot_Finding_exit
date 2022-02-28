
#  Best search 

#
########################

import copy
from ctypes.wintypes import HLOCAL
from distutils.util import run_2to3
from multiprocessing import active_children
from multiprocessing.sharedctypes import Value
import re
from turtle import position

x = "XXX"
s = "_"
robot = "robot"
a = [robot, s, s, s, s, s]
b = [s, s, s, s, s, s]
c = [s, s, s, s, s, s]
d = [x, x, s, s, x, x]
e = [s, s, x, x, s, s]
f = [s, s, x, x, s, s]
g = [s, s, s, x, s, s]
laberinto = [a, b, c, d, e, f, g]

copia_table = copy.deepcopy(laberinto)

for i in laberinto:
    print(i)
    print()
    
def movimiento_derecha():
    contador = 0
    llave = "key_d"
    for j, values in enumerate(laberinto):
        for i in values:
            if i == robot:
                r1 = values.index("robot")
                radiohead = j
                if r1 < 5:
                    condicional = laberinto[radiohead][r1+1]
                    if condicional == "_":
                        values.insert(r1 + 1, values.pop(r1))
                        print("El robot se ha movido a la derecha", values)
                        actual = values.index("robot")
                        contador = 1
                        print("contador:", contador)
                        imprimirlaberinto()
                    elif condicional == "XXX":
                        print("no se puede desplazar a la derecha hay un obstáculo")
                        print()
                        print(laberinto)
                        actual = r1
                    yield contador, llave, j, actual
                elif r1 == 5:
                    print("No se puede mover a la derecha")
                    actual = r1
                    yield contador, llave, j, actual
                    
                    
         
    return contador, llave, j, actual 


def movimiento_izquierda():
    contador = 0 
    llave = "key_i"
    for j, values in enumerate(laberinto):
        for i in values: 
            if i == robot:
                r1 = values.index("robot")
                condicional = laberinto[j][r1-1]
                if condicional == "_":
                    values.insert(r1 - 1, values.pop(r1))
                    print("El robot se ha movido a la izquierda", values)
                    actual = values.index("robot")
                    print("contador:", contador)
                elif condicional == "XXX":
                    print("no se puede desplazar a la izquierda hay un obstáculo")
                    print()
                    print(laberinto)
                    actual = r1
                yield contador, llave, j, actual                
    return contador, llave, j, actual

def movimiento_bajo():
    contador = 0
    llave = "key_a"
    for j, values in enumerate(laberinto):
        print(j, values)
        for i in values:
            if i == robot: 
                r1 = values.index(robot)
                hola = j 
                condicional = laberinto[hola+1][r1]
                if condicional == "_":
                    laberinto[hola+1].insert(r1, values.pop(r1))
                    laberinto[hola+1].pop(r1+1)
                    laberinto[hola].append("_")
                    koala = hola+1
                    actual = 2
                    print()
                    print("Se ha movido el robot un lugar abajo")
                    print()
                    for j in laberinto:
                        for h in j:
                            if h == robot:
                                actual = j.index(robot)
                                koala = laberinto.index(j)
                                print(h)
                                print(j)            
                    yield contador+2, llave, koala, actual
                elif condicional == "XXX":
                    for j in laberinto:
                        for h in j:
                            if h == robot:
                                actual = j.index(robot)
                                koala = laberinto.index(j)
                                print(h)
                                print(j)      
                    print("no se puede desplazar ahacia abajo hay un obstáculo")
                    print()
                    yield contador, llave, koala, actual
    return contador, llave, koala, actual



def movimiento_sureste():
    contador = 0
    llave = "key_se"
    for j, values in enumerate(laberinto):
        print(j, values)
        for i in values:
            if i == robot: 
                r1 = values.index(robot)
                hola = j
                if r1 < 5:
                    condicional = laberinto[hola+1][r1+1]
                    if condicional == "_":
                        laberinto[hola+1].insert(r1+1, values.pop(r1))
                        laberinto[hola+1].pop(r1+2)
                        laberinto[hola].append("_")
                        print("Se ha movido el robot un lugar al suroeste")
                        print()
                        contador + 1
                        for j in laberinto:
                            for h in j:
                                if h == robot:
                                    actual = j.index(robot)
                                    koala = laberinto.index(j)
                                    print(h)
                                    print(j)   
                        yield contador+3, llave, koala, actual
                    elif condicional == "XXX":
                        for j in laberinto:
                            for h in j:
                                if h == robot:
                                    actual = j.index(robot)
                                    koala = laberinto.index(j)
                                    print(h)
                                    print(j)   
                        print("no se puede desplazar al sureste hay un obstáculo")
                        print()
                        yield contador, llave, koala, actual
                elif r1 == 5:
                    print("No se puede mover ya que llegaste al límite")
                    actual = r1
                    koala = hola
                    yield contador, llave, koala, actual
                        
    return contador, llave,  koala, actual

def movimiento_suroeste():
    contador = 0
    llave = "key_so"
    for j, values in enumerate(laberinto):
        print(j, values)
        for i in values:
            if i == robot: 
                r1 = values.index(robot)
                hola = j
                condicional = laberinto[hola+1][r1-1]
                if condicional == "_":   
                    laberinto[hola+1].insert(r1-1, values.pop(r1))
                    laberinto[hola+1].pop(r1+1)
                    laberinto[hola].append("_")
                    print("Se ha movido el robot un lugar al sureste")
                    print()
                    print("Se ha  movido al suroeste el robot")
                    for j in laberinto:
                        for h in j:
                            if h == robot:
                                actual = j.index(robot)
                                koala = laberinto.index(j)
                                print(h)
                                print("Koala*****____", koala)   
                    yield contador+3, llave, koala, actual
                elif condicional == "XXX":
                    for j in laberinto:
                        for h in j:
                            if h == robot:
                                actual = j.index(robot)
                                print("XXX ACTUAL*****", actual)
                                koala = laberinto.index(j)
                                print(koala)
                                print(h)
                                print(j)   
                    print("no se puede desplazar al suroeste hay un obstáculo")
                    print()
                    yield contador, llave,  koala, actual
    return contador, llave, actual, koala


def desahacer_movimiento(contador, identificador):
    counter = 0
    for i, values in enumerate(laberinto):
        for h in values:
            if h == robot: 
                r2 = values.index(robot)
                nivel = i
                if r2 < 5:
                    derecha = laberinto[nivel][r2+1]
                    izquierda = laberinto[nivel][r2-1]
                    arriba = laberinto[nivel-1][r2]
                    norteoeste = laberinto[nivel-1][r2-1]
                    norponiente = laberinto[nivel-1][r2+1]
                elif r2 == 5:
                    izquierda = laberinto[nivel][r2-1]
                    arriba = laberinto[nivel-1][r2]
                    norteoeste = laberinto[nivel-1][r2-1]
                    derecha = "XXX"
                    norponiente = "XXX"    
                if contador == 1:
                    if derecha == "_" and identificador == "key_i":
                        values.insert(r2 + 1, values.pop(r2))
                        print("El movimiento izquierdo ha sido anhulado")
                        return counter - 1
                    elif izquierda == "_" and identificador == "key_d":
                        values.insert(r2 - 1, values.pop(r2))
                        print("El movimiento derecho ha sido anhulado")
                        return counter - 1
                elif contador == 2: 
                    if arriba == "_" and identificador == "key_a":
                        laberinto[nivel-1].pop(r2)
                        laberinto[nivel-1].insert(r2, values.pop(r2))
                        laberinto[nivel].insert(r2, "_")
                        print("El movimiento de abajo ha sido anhulado")
                        print()
                        for j in laberinto:
                            print(j)
                        return counter -2
                elif contador == 3:
                    if norponiente == "_" and identificador == "key_so":
                        laberinto[nivel-1].pop(r2)
                        laberinto[nivel-1].insert(r2+1, values.pop(r2))
                        laberinto[nivel].insert(r2, "_")
                        print("El movimiento suroeste ha sido anhulado")
                        imprimirlaberinto()
                        return counter -3
                    elif norteoeste == "_" and identificador == "key_se":
                        laberinto[nivel-1].pop(r2)
                        laberinto[nivel-1].insert(r2-1, values.pop(r2))
                        laberinto[nivel].insert(r2, "_")
                        print("El movimiento sureste ha sido anhulado")
                        return counter -3
                elif contador == 0:
                    print("No has realizado ningun moviemito")
    return counter
                            
                        
                                
def imprimirlaberinto():
    for i in laberinto: 
        print("Estado final", i)    


#nodo = movimiento_derecha()
#nodo3 = movimiento_izquierda()
#nodo2 = movimiento_bajo()
#nodo5 = movimiento_suroeste()
#nodo4 = movimiento_suoeste()
#print(next(nodo5))

#nodo1, key = next(movimiento_sureste())
#nodo2, key = next(movimiento_suroeste())
#nodo3, key = next(movimiento_bajo())



def ejecución_movimientos():
    lista_almacen = []
    lista_Nodos = [lista_almacen]
    i = 0
    for i in range(5):
        if i == 0:
            nodo, key, indice, indice_robot = next(movimiento_derecha())
            print("-----", nodo, key, indice, indice_robot)
            lista_almacen.extend([nodo, key, indice, indice_robot])
            lista_Nodos.append(lista_almacen)
            print()
            if nodo == 1:
                desahacer_movimiento(nodo, key)
        elif i == 1:
            nodo, key, indice, indice_robot = next(movimiento_izquierda())
            print("-----", nodo, key, indice, indice_robot)
            lista_almacen.extend([nodo, key, indice, indice_robot])
            lista_Nodos.append(lista_almacen)
            print()
            if nodo == 1:
                desahacer_movimiento(nodo, key)
        elif i == 2:
            nodo, key, indice, indice_robot = next(movimiento_bajo())
            print("-----", nodo, key, indice, indice_robot)
            lista_almacen.extend([nodo, key, indice, indice_robot])
            lista_Nodos.append(lista_almacen)
            print()
            if nodo == 2:
                desahacer_movimiento(nodo, key)
        elif i == 3:
            nodo, key, indice, indice_robot = next(movimiento_suroeste())
            print("-----", nodo, key, indice, indice_robot)
            lista_almacen.extend([nodo, key, indice, indice_robot])
            lista_Nodos.append(lista_almacen)
            print()
            if nodo == 3:
                desahacer_movimiento(nodo, key)
            elif nodo == 0:
                print("No se puede deshacer, no hubo movimiento al suroeste")
        elif i == 4:
            nodo, key, indice, indice_robot = next(movimiento_sureste())
            print("-----", nodo, key, indice, indice_robot)
            lista_almacen.extend([nodo, key, indice, indice_robot])
            lista_Nodos.append(lista_almacen)
            print()
            if nodo == 3:
                desahacer_movimiento(nodo, key)
            
    return lista_almacen



def evaluacion(lola):
    lista = []
    for i, valor in enumerate(lola, 1):
        for h in list(range(1, 20, 4)):
            if i == h:
                thom = valor
                lista.extend([thom])
                hulu = max(lista)
                if valor == hulu:
                    nodo_vatter = lola[i-1:i+4]
    return nodo_vatter

def movimientos(lista, indice_robot):
    print(lista, indice_robot)
    for i, value in enumerate(laberinto):
        for h in value:
            if h == "robot":
                r2 = value.index("robot")
                robot = laberinto[i].pop(r2)
                laberinto[i].insert(r2, "_")
    laberinto[lista].pop(indice_robot)
    laberinto[lista].insert(indice_robot, robot)
    return laberinto
                
                
    

def Best_search():
    #Nodos_padre = []
    for i, values in enumerate(laberinto):
        for h in values:
            if h == "robot":
                print("Roboot", i)
                lola = ejecución_movimientos()
                print(lola)
                Nodos = evaluacion(lola)
                #Nodos_padre.append(Nodos)
                for h, valor in enumerate(Nodos):
                    if h == 2:
                        lista = Nodos[h]
                        indice_robot = Nodos[h+1]
                        print("Posicion", lista, indice_robot)
                                
    return Nodos, lista, indice_robot  



print("hola que hace")
#imprimirlaberinto()

def ejecucion():
    Nodos_padre = []
    cnn = 0
    for i in range(1, 6):
        print("cnnnnn----", cnn)
        if cnn <= 6: 
            nodo_Mayor, lista, robot = Best_search()
            Nodos_padre.append(nodo_Mayor)
            movimientos(lista, robot)
            print("Nodos Padre ---------------------------------------------------------------------------------")
            print(Nodos_padre)
            print("---------------------------------------------------------------------------------------------")
            imprimirlaberinto()
            for h, value in enumerate(laberinto):
                for k in value:
                    if k == "robot":
                        sublist = h
                        cnn = sublist
        elif cnn == 6:
            print("Ya no se pueden realizar movimientos, el robot ha llegado a la meta")
                    
    
    return Nodos_padre

portishead = ejecucion()

print()
print("-------------------RESULTADO FINAL-----------------")
print()
print("Estos son los Nodos Padre:", portishead)
print()
imprimirlaberinto()
