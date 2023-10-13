import pandas as pd
from funcionsumar import sumararboles
#analisar una lista de datos 
ciudades=["medellin","bogota","bucaramanga","cartagena","cali","barranquilla"]


#analisar una lista de dicionarios 
estudiantes=[
    {"id":1,"nombre":"felipe","promedio":2.9},
    {"id":2,"nombre":"carlos","promedio":2.5},
    {"id":3,"nombre":"juan","promedio":3.0},
    {"id":4,"nombre":"pedro","promedio":2.4}
   ]

arbolespormunicipio=[
    {"id":1,"municipio":"Carolina","tipo":"guayacanes","cantidad":1500}
]
#convirtiendo listas y listas de dataframe
dataframe1=pd.DataFrame(ciudades)
dataframe2=pd.DataFrame(estudiantes)

print (dataframe1)
print(dataframe2)

numerodearbolesori=120000
numeroarbolessuroeste=300000
numeroarbolesnorte=500000

sorientenorte=sumararboles(numerodearbolesori,numeroarbolesnorte)
ssuroesteoriente=sumararboles(numeroarbolessuroeste,numerodearbolesori)
#Analisar un csv