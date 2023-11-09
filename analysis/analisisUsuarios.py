from data.ListaUsuarios import usuarios
from helpers.crearCSV import crearCSVUsuarios
from helpers.crearHTML import crearTabla

import pandas as pd

#Usamos la función crear CSVUsuarios
crearCSVUsuarios(usuarios,'BDUsuarios.csv')

# creando un dataframe desde una CSV
dataFrameUsuarios = pd.read_csv('data/BDUsuarios.csv')
print(dataFrameUsuarios)

# convertir el DF en Tabla html
crearTabla(dataFrameUsuarios,'usuarios')