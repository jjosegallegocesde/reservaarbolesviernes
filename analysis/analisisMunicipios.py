from helpers.funcionesMunicipios import randomMunicipios
from helpers.crearCSV import crearCSVMunicipiosArboles

siembras = randomMunicipios()
crearCSVMunicipiosArboles(siembras,'BDMunicipiosArboles.csv')



#buscar municipios>90 arboles cantidad
#municipios con ceibas
#municipios con siembras<10

#como transformar un dataframe en pdf y que se permita descargar