from Circunferencia import Circunferencia_Centrada

def imprimirCircunferencia(circun):
    print("Centro=({0},{1})  Radio={2}  Diametro={3}  Longitud={4}  Area={5}".format(circun.getXCentro(), 
    circun.getYCentro(), circun.getRadio(), circun.getDiametro(), circun.getLongitud(), circun.getArea()))

circunf1 = Circunferencia_Centrada()
imprimirCircunferencia(circunf1)
circunf2 = Circunferencia_Centrada(2,3,4)
imprimirCircunferencia(circunf2)
circunf1.setRadio(5)
imprimirCircunferencia(circunf1)
circunf2.setDiametro(2)
imprimirCircunferencia(circunf2)
circunf3 = Circunferencia_Centrada(1.5,1.5)
circunf3.setLongitud(3.1416)
imprimirCircunferencia(circunf3)
circunf3.setArea(25.1328)
imprimirCircunferencia(circunf3)