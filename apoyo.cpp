#include <iostream>
#include "apoyo.h"
using namespace std;
//----------------------------
// Definir las direcciones: {izquierda, derecha, arriba, abajo}
//------------------------------
objeto::objeto() : tipo(VACIO), x(0), y(0) {}  // Inicializamos como VACIO por defecto
objeto::objeto(int posx, int posy, int dirx, int diry, tipoObjeto _tipo) : x(posx), y(posy),direccion_x(dirx),direccion_y(diry),tipo(_tipo) {}
tablero::tablero(int f, int c) {
    filas = f;
    columnas = c;
    tamano = f * c;

    // Asignación de memoria para la matriz de punteros a objetos
    matriz = new objeto*[filas];
    for (int i = 0; i < filas; ++i) {
        matriz[i] = new objeto[columnas];  // Cada fila es un array de objetos
    }

    // Inicialización de cada elemento de la matriz como un objeto VACIO
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            matriz[i][j] = objeto();  // Inicialización por defecto (VACIO)
        }
    }
}

tablero ::~tablero() {
            for (int i = 0; i < filas; ++i) {
                delete[] matriz[i];
            }
            delete[] matriz;
        }
bool tablero::detectar_choque(int x, int y, int &dx, int &dy) {
        if (matriz[x][y].tipo == ESPEJO) {
            cout << "La luz ha chocado con un espejo en (" << x << ", " << y << ")" << endl; //ayuda para indicar si ha chocado o no
            dx = matriz[x][y].direccion_x;
            dy= matriz[x][y].direccion_y;
            return false;
        } else if (matriz[x][y].tipo == OBSTACULO) {
            cout << "La luz ha chocado con un obstáculo en (" << x << ", " << y << ")" << endl; //ayuda para indicar si ha chocado o no
            dx = matriz[x][y].direccion_x;
            dy= matriz[x][y].direccion_y;
            return true;
        }
    }
void tablero::colocar_objeto(int posx, int posy, int dirx, int diry, tipoObjeto _tipo){
        if(_tipo == OBSTACULO){
            objeto OBJETO(posx,posy,0,0,_tipo);
            matriz[OBJETO.x][OBJETO.y]= OBJETO;
        }
        else{
            objeto OBJETO(posx,posy,dirx,diry,_tipo);
            matriz[OBJETO.x][OBJETO.y]= OBJETO;
        }
}
void tablero::mostrar_tablero(){
    for (int i = 0; i < filas; i++) {
        for (int j = 0; j < columnas; j++) {
            cout << "|";
            cout.flush();
            if (matriz[i][j].tipo == ESPEJO) cout << "E "; // espejo
            else if (matriz[i][j].tipo == OBSTACULO) cout << "OB"; // obstáculo
            else if (matriz[i][j].tipo == VACIO) cout << "  "; // espacio vacío
            cout << "|";
        }
        cout << endl;
    }

}

//-------------------------------------------------------------------------------------------------------------
    //Creacion de objeto "luz"
luz::luz(int posx, int posy,int dirx,int diry,tipoObjeto _tipo) : objeto(posx, posy, dirx, diry, LUZ) {}
void luz::viajar_luz(tablero mapa){
        if (mapa.detectar_choque(x, y,direccion_x,direccion_y)==true) {//choca con obstaculo
            return ;// Detiene el viaje si hay choque
        }
        // Continuar con las reglas de movimiento
        if (y+1 < mapa.filas and direccion_y == 1 and direccion_x == 0) {
            y = y + 1;
            viajar_luz(mapa);
        }
        else if (y - 1 >= 0 and direccion_y == -1 and direccion_x == 0) {
            y = y - 1;
            viajar_luz(mapa);
        }
        else if (x + 1 < mapa.columnas and direccion_y == 0 and direccion_x == 1) {
            x = x + 1;
            viajar_luz(mapa);
        }
        else if (x - 1 >= 0 and direccion_y == 0 and direccion_x == -1) {
            x = x - 1;
            viajar_luz(mapa);
        }
    }
//---------------------------------------------------------------------------------------
    //Creacion de objeto "espejo"
espejo::espejo(int posx, int posy,int dirx,int diry,tipoObjeto _tipo) : objeto(posx, posy, dirx, diry, ESPEJO) {}
//--------------------------------------------------------------------------------------
    //Creacion de objeto "obstaculo"
obstaculo::obstaculo(int posx, int posy,int dirx,int diry,tipoObjeto _tipo) : objeto(posx, posy, 0, 0, OBSTACULO) {}
//-----------------------------------------------------------------------------------------
