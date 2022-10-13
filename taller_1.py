
# ESTRUCTURAS DE DATOS

# LISTAS

#Las listas son una estructura de datos en la cual se pueden almacenar datos de cualquier tipo como por ejemplo
#enteros, Sting, float, etc. los cuales se almacenan de una manera más organizada para conseguir un uso más eficiente de estos datos.")

# METODOS DE LISTAS

# list.append(x): Este método lo que hace es agregar un dato en el final de la lista.

print("METODOS EN LAS LISTAS")

print("METODO APPEND")

list = [1,2,3,4,5]
print(list)

list.append(6)
print(list)

print("---------------------------------------------------------------------------------------------")

# list.extend(iterable): Este método lo que hace es agregara a la lista los elementos de otra lista al final de esta.

print("METODO EXTEND")

list_1 = [1,2,3,4,5]
print(list_1)

list_2 = [6,7,8,9,10]
print(list_2)

list_1.extend(list_2)
print(list_1)

print("---------------------------------------------------------------------------------------------")

# list.insert(i, x): Inserta un elemento en la lista en la posición dada.

print("METODO INSERT")

list = [1,2,3,4,5]
print(list)

list.insert(5,6)
print(list)

print("---------------------------------------------------------------------------------------------")

# list.remove(x): Este metodo sirve para para quitar el primer valor de la lista que sea el mismo que se desae remover.

print("METODO REMOVE")

list = [1,2,3,4,5]
print(list)

list.remove(3)
print(list)

print("---------------------------------------------------------------------------------------------")

# list.pop([i]): Este método lo que hace es quitar el elemento en la posición dada.

print("METODO POP")

list = [1,2,3,4,5]
print(list)

list.pop(0)
print(list)

print("---------------------------------------------------------------------------------------------")

# list.clear(): Este método lo que hace es que elimina todos los elementos de una lista.

print("METODO CLEAR")

list = [1,2,3,4,5]
print(list)

list.clear()
print(list)

print("---------------------------------------------------------------------------------------------")

# list.index(x[,start[, end]]): Este método lo que hace es una busqueda dentro de la lista
# a lo que retorna la posición en la que se encuentra el valor señalado y en caso de que
# no exista el valor señalado el programa retornara ValueError los argumentos start y end
# son opcionales los cuales son para pautar un tramo determinado en la lista para realizar la busqueda.

print("METODO INDEX")

list = [1,2,3,4,5]
print(list)

pos_3 = list.index(3)
print(pos_3)

print("---------------------------------------------------------------------------------------------")

# list.count(x): Este método retorna el número de veces que aparece el elemento dado en la lista.

print("METODO COUNT")

list = [1,2,3,4,5]
print(list)

vec_1 = list.count(1)
print(vec_1)

print("---------------------------------------------------------------------------------------------")

# list.sort(*,key=None, reverse=False): Este método hace que los elementos de esta lista
# se organicen en orden alfanumérico.

print("METODO SORT")

list = [4,2,5,3,1]
print(list)

list.sort()
print(list)

print("---------------------------------------------------------------------------------------------")

# list.reverse(): Lo que hace este método es retornar los elementos de la lista en orden inverso al que se encuentra.

print("METODO REVERSE")

list = [1,2,3,4,5]
print(list)

list.reverse()
print(list)

print("---------------------------------------------------------------------------------------------")

# list.copy(): Lo que hace este método es retornar una copia superficial de la lista.

print("METODO COPY")

list = [1,2,3,4,5]
print(list)

list.copy()
print(list)

print("---------------------------------------------------------------------------------------------")

# LISTAS COMO PILAS

# Al usar los métodos en estas listas se hace más fácil el uso de esta como una pila
# la cual permite almacenar y recuperar datos siendo de tipo LIFO << Del inglés
# Last In, First Out, lo que quiere decir en español, Ultimas en entrar, Primeras en salir>>
# y para esto se utilizan los métodos append para ingresar datos a la lista y el método pop para sacarlos.

print("EJEMPLO LISTAS COMO PILAS")

list = [1,2,3,4,5]
print(list)

list.append(6)
list.append(7)
print(list)

list.pop()
list.pop()
list.pop()
list.pop()
print(list)

print("---------------------------------------------------------------------------------------------")

# LISTAS COMO COLAS

# Las listas tambien pueden ser utilizadas como colas donde el primer elemento añadido
# es el primero en ser eliminado, para esto se utiliza el collections.deque el cual fue 
# creado parea eliminar de ambas puntas.

print("EJEMPLO LISTAS COMO COLAS")

from collections import deque
import queue
from typing import Set
list = deque([1,2,3,4,5])
print(list)

list.append(6)
list.append(7)
print(list)

list.popleft()
list.popleft()
print(list)

print("---------------------------------------------------------------------------------------------")

# COMPRENSION DE LISTAS

# Es una manera de crear una lista mas concisa estas se utilizan mas que todo al crear listas
# con resultados de operaciones matematicas. estas consisten en un ciclo for en el cual
# se hace el proceso deseado para que se muestre en la lista

print("EJEMPLO COMPRENSION DE LISTAS")

list = []
for x in range(5):
    list.append(x*2)

print(list)

print("---------------------------------------------------------------------------------------------")

# INSTRUCCION del

# La instruccion del es muy similar al metodo pop() la diferencia es que la instruccion del es que esta
# se puede utilizar para eliminar secciones de una lista o eliminar todos los elementos de la lista
# para elomonar toda la lista se utilizan los [:] dos puntos entre corchetes y para una seccion
# tambien se utilizan los dos punto poniendolos en medio de los dos rangos el inicial y el final
# en donde se desea eliminar sabiendo que el primer rango es excluyente y el primero es incluyente  

print("EJEMPLO DE LA INSTRUCCION del")

list = [1,2,3,4,5,6,7,8,9,10]
print(list)

del list[0]
print(list)

del list[2:6]
print(list)

del list[:]
print(list)

print("---------------------------------------------------------------------------------------------")

# TUPLAS Y SECUENCIAS

# Las tuplas son una serie de elementos con u valor asignado separados por comas en las cuales
# se pueden combinar tipos de datos como enteros, strings, float, entre otros.

print("EJEMPLO TUPLA")

tupla = 1,'dos', 3.14, 'cuatro'
print(tupla)

print("---------------------------------------------------------------------------------------------")

# len, en las tuplas el len se utiliza para saber cuales la longitud
# en numero de elementos de una tupla.

print("EJEMPLO DEL USO DEL len EN UNA TUPLA")

tupla = 1,'dos', 3.14, 'cuatro'
print(tupla)

len_tup = len(tupla)
print(len_tup)

print("---------------------------------------------------------------------------------------------")

# CONJUNTOS

# Es una agrupacion de elementos no ordenada en la cual no se pueden repetir datos
# para crear un conjunto se utiliza la funcion set() o utilizando llaves{}. Utilizando
# la funcion set() se tiene que meter todos los elementos del conjuntos dentro de un par 
# de comillas y al usal las llaves{} no se tiene que hacer esto.

print("EJEMPLO CREAR UN CONMJUNTO")

conjunto_1 = {1,2,3,4,5,6,7,8,9,0}
print(conjunto_1)

conjunto_2 = set('1,2,3,4,5,6,7,8,9,0')
print(conjunto_2)

print("---------------------------------------------------------------------------------------------")

# Para agregar los elementos de un conjunto en otro se hace una suma en la cual se crea
# un conjunto en el cual estan los elementos de ambos conjuntos en donde no se repite
# ningun elemento, eliminando los repitentes.

print("EJEMPLO SUMA DE CONJUNTOS")

conjunto_one = {1,2,3,4,5,6,7,8,9,0}
print(conjunto_one)

conjunto_two = {10,11,12,13,4,5,6,7}
print(conjunto_two)

conjunto_tree = conjunto_one | conjunto_two
print(conjunto_tree)

print("---------------------------------------------------------------------------------------------")

# Para seleccionar los elementos que estan unicamente en un conjunto se hace un resta de conjuntos.

print("EJEMPLO RESTA DE CONJUNTOS")

set_1 = {1,2,3,4,5,10,11,12,13,14,15}
print(set_1)

set_2 = {1,2,3,4,5,6,7,8,9}
print(set_2)

set_3 = set_1 - set_2
print(set_3)

print("---------------------------------------------------------------------------------------------")

# Para hallar los elementos que tienen en comun dos conjuntos se utiliza & en una operacion"

print("EJEMPLO ELEMENTOS EN COMUN DE DOS CONJUNTOS")

set_one = {1,2,3,4,5}
print(set_one)

set_two = {1,2,3,4,5,6,7,8,9,0}
print(set_two)

set_tree = set_one & set_two
print(set_tree)

print("---------------------------------------------------------------------------------------------")

# DICCIONARIOS

# Son arreglos asociativos indexados por claves que pueden ser de cualquier tipo, 
# para crear un diccionario se utilizan las llaves{}, en los diccionarios 
# se maneja la siguiente secuencia clave:valor separados por comas con los demas asociandolos.

print("EJEMPLO CREACION DE DICCIONARIOS")

diccionario = {'Alzate':1,'Bernal':2,'Cruz':3,'Duarte':4}
print(diccionario)

print("---------------------------------------------------------------------------------------------")

# Para agregar un elemento al diccionario se utiliza la siguiente linea de codigo 
# nombre_diccionario['clave'] = valor

print("EJEMPLO AGRGACION DE ELEMENTOS EN UN DICCIONARIO")

dic = {'Alzate':1,'Bernal':2,'Cruz':3,'Duarte':4}
print(diccionario)

dic['Estupiñan'] = 5
print(dic)

print("---------------------------------------------------------------------------------------------")

# Para eliminar un elemento de un diccionario se utiliza la instruccion del.

print("EJEMPLO ELIMINAR UN ELEMENTO DE UN DICCIONARIO")

dic = {'Alzate':1,'Bernal':2,'Cruz':3,'Duarte':4}
print(dic)

del dic['Bernal']
print(dic)

print("---------------------------------------------------------------------------------------------")

# Para consultar si un elemento esta en un diccionario se utiliza la siguiente linea de codigo
# 'clave' in nombre_diccionario o en su defecto para saber si no esta se utiliza la siguiente 
# linea de codigo 'clave' not in nombre_diccionario estas lineas de codigo se les asigna una 
# variable y la salida de esta linea de codigo retorna un valor booleano

print("EJEMPLO CONSULTAR UN ELEMENTO EN UN DICCIONARIO ")

dic = {'Alzate':1,'Bernal':2,'Cruz':3,'Duarte':4}
print(dic)

con = 'Alzate' in dic
print(con)

print("---------------------------------------------------------------------------------------------")

# TECNICAS DE ITERACION

# Para iterar un diccionario se puede obtener la clave y el valor usando el metodo items().

print("EJEMPLO ITERACION DE DICCIONARIOS")

dic = {'Alzate':1,'Bernal':2,'Cruz':3,'Duarte':4}
for c, v in dic.items():
    print(c, v)

print("---------------------------------------------------------------------------------------------")

# Para obtener el indice con la posicion correspondiente se usa la funcion enumerate().

dic = {'Alzate':1,'Bernal':2,'Cruz':3,'Duarte':4}
for c, v in enumerate(dic):
    print(c, v)

print("---------------------------------------------------------------------------------------------")

# Para iterar una o mas sewcuencias al mismo tiempo se utiliza la fincion zip().

propiedades = ['edad', 'dia_mes', 'dia_nacimiento']
valores = ['17', '11', '15/03']
for p, v in zip(propiedades, valores):
    print('cual es tu {0}? Es {1}.'.format(p,v))

print("---------------------------------------------------------------------------------------------")

# CONDICIONES

# Las condiciones se utilizan para crear caminos los cuales se tienen que correr mientras 
# se cumpla la condicion los condicionales mas comunes son el if y el while.

print("EJEMPLO CONDICIONES CON IF")

n1 = int(input("Ingrese un valor: "))
n2 = int(input("Ingrese otro valor: "))
suma = n1 - n2
if suma >= 0:
    resultado = suma + 10
    print(resultado)
else:
    print("La suma de los valores ingresados es negativa y no se le puede añadir el valor acordado")

print("---------------------------------------------------------------------------------------------")

print("EJEMPLO CONDICIONES CON WHILE")

num_1 = 0
num_2 = 0
total = 0
pregunta = input("Desea continuar: ")

while (pregunta != 'no' ):
    num_1 = float(input("Ingresa el valor del producto: "))
    num_2 = float(input("Ingresa la cantidad de unidades que te llevas: "))
    total = num_1 * num_2
    print(total)
    pregunta = input("Desea continuar: ")