import pandas as pd

# los data frame son diccionarios que se parecen a una tabla de excel, a una base de datos. 
# tienen filas. cada fila representa un registro
# lleva llave {} adentro

df = pd.DataFrame({
    "nombre": ["ana", "juan", "Pedro"],
    "edad": [25, 30, 35],
    "salario": [3000, 4000, 5000]
})
print(df)
