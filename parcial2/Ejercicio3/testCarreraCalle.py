from Carrera import Carrera
from Calle import Calle

carrera_p = Carrera(43, 1, "10-10-2022")
calle0 = Calle(1)
calle0.setAtleta("Grant")
calle0.setTiempo(31.78)
print(carrera_p.getDistancia(), carrera_p.getRonda(), carrera_p.getFecha())
print(calle0.getNumero(), calle0.getAtleta(), calle0.getTiempo())
carrera_p.insertar_calle(calle0)
carrera_p.imprimir_calles()