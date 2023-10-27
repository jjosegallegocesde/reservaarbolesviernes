from data.ListaUsuarios import usuarios
from helpers.crearCSV import crearCSVUsuarios

#Usamos la función crear CSVUsuarios
crearCSVUsuarios(usuarios,'BDUsuarios.csv')