#ifndef APOYO_H
#define APOYO_H
//definicion de funciones de apoyo de proyecto
//--------------------------------------------

//----------------------------
// Definir las direcciones: {izquierda, derecha, arriba, abajo}
int direcciones_y[4]={-1,1,0,0};
int direcciones_x[4]={0,0,1,-1};
//------------------------------
enum tipoObjeto {VACIO, OBSTACULO, ESPEJO, LUZ}; //Definir los tipos de objetos posibles
//------------------------------
class objeto{/*los objetos pueden ser espejos, obstaculos, o fuentes de luz (crear objeto padre
            y luego crear hijos con base a cada objeto para despues agregarlo en el tablero)*/
    public:
        int x;
        int y;
        int direccion_x;
        int direccion_y;
        tipoObjeto tipo;
        objeto(); // Inicializamos como VACIO por defecto
        objeto(int posx, int posy, int direccionx, int direcciony, tipoObjeto _tipo); // Constructor cuando se especifica el objeto
};
class tablero{ //creacion de un tablero que almacene objetos sean vacios, obstaculos, espejos
    public:
        int filas;
        int columnas;
        int tamano;
        objeto **matriz;  // Matriz de objetos
    public:
        tablero(int f, int c);
        ~tablero();
    bool detectar_choque(int x, int y, int &dx, int &dy);
    void colocar_objeto(int posx, int posy, int dirx, int diry, tipoObjeto _tipo);
    void mostrar_tablero(); 
};
//-------------------------------------------------------------------------------------------------------------
    //Creacion de objeto "luz"
class luz: public objeto{
    public:
    luz(int posx, int posy, int direccionx, int direcciony, tipoObjeto LUZ);
    void viajar_luz(tablero mapa);
};
//---------------------------------------------------------------------------------------
    //Creacion de objeto "espejo"
class espejo : public objeto {
    public:
        espejo(int posx, int posy, int direccionx, int direcciony,tipoObjeto ESPEJO);
};
//--------------------------------------------------------------------------------------
    //Creacion de objeto "obstaculo"
class obstaculo : public objeto {
    public:
        obstaculo(int posx, int posy,int direccionx, int direcciony, tipoObjeto OBSTACULO);
};
//-----------------------------------------------------------------------------------------
    //UI del juego
class HUB{
    public:
        tablero matriz;
        HUB(tablero Tablero);
    void principal();
};
//-----------------------------------------------------------------------------------------
#endif