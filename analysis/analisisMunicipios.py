from helpers.funcionesMunicipios import randomMunicipios
from helpers.crearCSV import crearCSVMunicipiosArboles

siembras = randomMunicipios()
crearCSVMunicipiosArboles(siembras,'BDMunicipiosArboles.csv')