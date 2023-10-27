import pandas as pd
import random

usuarios=[]

for i in range(10):
    nombre = random.choice(['juan','andrea','sara','jorge'])
    contrasena = random.choice(['admin123','arboles000'])
    edad = random.randint(18,62)
    usuario=[nombre,contrasena,edad]
    usuarios.append(usuario)
    
# print(usuarios)

tabla = pd.DataFrame(usuarios),

print (tabla)