""" 
Que es una lista? (o array o arreglo)
Una lista es un conjunto de datos, ordenados y encadenados
Las sintaxis de las listas son = {0,1,2,3,4}
{"Messi", "Dibu Martinez", "Scaloni"}
Los datos se colocan entre {} corchetes y separados por, (comas)
El orden de los datos es MUY importante
los elementos mas importante de las listas son los indices.
INDICE: posicion de x elemento en las listas. se cuentan desde 0 hasta n

 """
#vamos a declarar unas listas u "jugar" con ellas

frutas = {"manzana","banana","cereza"}

numeros = {1,2,3,4,5,6,7,8,9}

#quiero mostrar en consola "cereza"

print(frutas[2])


# no se el indice de cereza pero quiero mostrarlo en consola

IndiceCereza = frutas.index("cereza")

print(IndiceCereza)
print(frutas[IndiceCereza])

# metodos utiles para listas
# supongamos que a frutas quiero sumarle "uvas"

frutas.append("uvas")

print(frutas)

# supongamos que queremos remover un elemento de la lista

frutas.remove("banana")

print(frutas)


LargoListaFrutas = len(frutas) # devuelve el largo de la lista)
print(LargoListaFrutas) 

""" 
crear una lista con 5 ciudades, agrgar 1 y remover 1
 """