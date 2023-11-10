from data.refrigerios import refrijerios
from helpers.crearCSV import crearCSVRefrigerios
from helpers.crearHTML import crearTabla

import pandas as pd

#Usamos la función crear CSVRefrigerios
crearCSVRefrigerios(refrijerios,'BDRefrigerios.csv')

# creando un dataframe desde una CSV
dataFrameRefrigerios = pd.read_csv('data/BDRefrigerios.csv')
print(dataFrameRefrigerios)

# convertir el DF en Tabla html
crearTabla(dataFrameRefrigerios,'refrigerios')