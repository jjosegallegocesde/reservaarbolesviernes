import pandas as pd
import random

refrijerios =[]

for i in range(3000):
    nombre = random.choice(['chicharron','papas','longaniza','huevos revueltos'])
    precio = random.randint(15000,40000)
    refrijerio=[nombre,precio]
    refrijerios.append(refrijerio)
    
# print(refrijerios)

tabla = pd.DataFrame(refrijerios),

print (tabla)