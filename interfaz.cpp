#include <iostream>
#include "apoyo.h"
using namespace std;
//--------------------------
HUB::HUB(tablero Tablero): matriz (Tablero){}
void HUB::principal(){
    cout<<"\t\t\t\tJUEGO DE LOS ESPEJOS"<<endl;
    cout<<"El Juego de los Espejos podría ser un videojuego o simulador basado en la lógica y el reflejo de imágenes en espejos."<<
    "\n El objetivo podría ser guiar un rayo de luz o un objeto a través de un laberinto usando espejos, teniendo en cuenta las" 
    <<"\n reflexiones, ángulos y obstáculos que podrían estar presentes"<<endl;
    cout<<"\t\t\t\tNivel de Prueba"<<endl;
    matriz.mostrar_tablero();
}