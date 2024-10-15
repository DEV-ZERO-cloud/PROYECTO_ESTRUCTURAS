/*GRUPO 6 - 
    Nombres: 1. Andres Felipe Rubiano Marrugo -T00077084 
             2. Cristian Benitez - T00078658
             3. Jesús Andrés Pérez -T00078491
             4. Israel Hoyos  -T00069427
             5. Santiago payares - T00068704*/
#include <iostream>
#include "apoyo.cpp"
#include "interfaz.cpp"
using namespace std;
//------------------------------------
int main(){
    tablero Tablero(6,6); //creamos tablero;
     //Creo cosas para el tablero
    Tablero.colocar_objeto(0,0,0,0,OBSTACULO);
    Tablero.colocar_objeto(1,0,0,0,OBSTACULO);
    Tablero.colocar_objeto(2,0,0,0,OBSTACULO);
    Tablero.colocar_objeto(3,0,0,0,OBSTACULO);
    Tablero.colocar_objeto(4,0,0,0,OBSTACULO);
    Tablero.colocar_objeto(5,0,0,0,OBSTACULO);
    //presentamos
    HUB pantalla(Tablero);
    pantalla.principal();
    return 0;
}