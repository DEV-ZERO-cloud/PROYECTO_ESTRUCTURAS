"""GRUPO 6 - 
    Nombres: 1. Andres Felipe Rubiano Marrugo -T00077084 
             2. Cristian Benitez - T00078658
             3. Jesús Andrés Pérez -T00078491
             4. Israel Hoyos  -T00069427
             5. Santiago payares - T00068704"""
#--------------------------------------------------------------
import apoyo as ap
import interfaz as int

def main():
    # Crear un tablero de 9x9    o que sean impares
    tamx=9
    tamy=9
    Tablero = ap.Tablero(tamx,tamy)
    fuente_luz = ap.Luz(round(tamx/2),round(tamy/2),-1,-1)
    # Crear una fuente de luz y colocarla en el tablero
    ob1= ap.Obstaculo(8,0)
    esp1 = ap.Espejo(1,1,3)
    esp2 = ap.Espejo(0,4,3)
    esp3 = ap.Espejo(4,0,2)
    esp4 = ap.Espejo(4,6,4)
    Tablero.colocar_objeto(ob1.x,ob1.y,ob1)
    Tablero.colocar_objeto(esp1.x,esp1.y,esp1)
    Tablero.colocar_objeto(esp2.x,esp2.y,esp2)
    Tablero.colocar_objeto(esp3.x,esp3.y,esp3)
    Tablero.colocar_objeto(esp4.x,esp4.y,esp4)
    Tablero.colocar_objeto(fuente_luz.x,fuente_luz.y,fuente_luz)
    # Mostrar el tablero y ejecutar la lógica del juego
    Tablero.mostrar_tablero()
    fuente_luz.viajar_luz(Tablero)
main()
