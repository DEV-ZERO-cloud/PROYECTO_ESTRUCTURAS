import time
import os

# Nota: x = columnas , y  = filas
"""Class Tipos de movimiento: Ilustrativo
    (0,0) ->quieto
    (0,1) ->derecha
    (0,-1) ->izquierda
    (1,0) ->abajo
    (-1,0) ->arriba
    (1,1) ->diagonal derecha hacia abajo
    (1,-1) ->diagonal izquierda hacia abajo
    (-1,1) ->diagonal derecha hacia arriba
    (-1,-1) ->diagonal izquierda hacia arriba
##"""

class TipoObjeto:
    VACIO = 0
    OBSTACULO = 1
    ESPEJO = 2
    LUZ = 3

class TipoEspejo:
    DIAGONAL1 = 1  # Representa `/`
    DIAGONAL2 = 2  # Representa `\`
    LATERAL1 = 3   # Representaa '__'
    LATERAL2 = 4   # Representaa '|'

class Objeto:
    def __init__(self, x, y, tipo):
        self.x = x
        self.y = y
        self.tipo = tipo

class Tablero:
    def __init__(self, filas, columnas):
        self.filas = filas
        self.columnas = columnas
        self.matriz = [[Objeto(x, y, TipoObjeto.VACIO) for y in range(columnas)] for x in range(filas)]

    def colocar_objeto(self, x, y, objeto):
        self.matriz[x][y] = objeto

    def obtener_objeto(self, x, y):
        return self.matriz[x][y]
    
    def mostrar_tablero(self):
        # Limpia la consola antes de mostrar el tablero
        os.system('cls' if os.name == 'nt' else 'clear')
        
        for i in range(self.filas):
            for j in range(self.columnas):
                obj = self.matriz[i][j]
                if obj.tipo == TipoObjeto.ESPEJO:
                    if obj.tipo_espejo == TipoEspejo.DIAGONAL1: 
                        print("|", "/", end="|")
                    elif obj.tipo_espejo == TipoEspejo.DIAGONAL2: 
                        print("|", "\\", end="|")
                    elif obj.tipo_espejo == TipoEspejo.LATERAL1: 
                        print("|", "_", end="|")
                    elif obj.tipo_espejo == TipoEspejo.LATERAL2: 
                        print("|", "|", end="|")
                elif obj.tipo == TipoObjeto.OBSTACULO:
                    print("|", "OB", end="|")
                elif obj.tipo == TipoObjeto.LUZ:
                    print("|", "L", end="|")
                else:
                    print("|", " ", end="|")
            print()
        time.sleep(0.5)  # Pausa de 0.5 segundos para simular movimiento en tiempo real

class Espejo(Objeto):
    def __init__(self, x, y, tipo_espejo):
        super().__init__(x, y, TipoObjeto.ESPEJO)
        self.tipo_espejo = tipo_espejo

class Obstaculo(Objeto):
    def __init__(self, x, y):
        super().__init__(x, y, TipoObjeto.OBSTACULO)

class Luz(Objeto):
                #(px,py, arriba_abajo,izquierda o derecha)
                #direccion = 0, significa que no se mueve
    def __init__(self, x, y, direccion_x, direccion_y):
        super().__init__(x, y, TipoObjeto.LUZ)
        self.direccion_x = direccion_x
        self.direccion_y = direccion_y

    def detectar_choque(self, tablero):
        # Calcular la posición hacia la cual se moverá la luz
        proxima_x = self.x + self.direccion_x
        proxima_y = self.y + self.direccion_y

        # Comprobar si está dentro de los límites del tablero
        if not (0 <= proxima_x < tablero.filas and 0 <= proxima_y < tablero.columnas):
            print(f"La luz ha salido del tablero en la posición ({self.x}, {self.y})")
            return True

        objeto = tablero.obtener_objeto(proxima_x, proxima_y)
        if objeto.tipo == TipoObjeto.ESPEJO:
            print(f"La luz ha chocado con un espejo en ({proxima_y}, {proxima_x})")
            # Reflexión dependiendo del tipo de espejo
            if objeto.tipo_espejo == TipoEspejo.DIAGONAL1:  # `/`
                self.direccion_x, self.direccion_y = -self.direccion_y, -self.direccion_x
            elif objeto.tipo_espejo == TipoEspejo.DIAGONAL2:  # `\`
                self.direccion_x, self.direccion_y = self.direccion_y, self.direccion_x
            elif objeto.tipo_espejo == TipoEspejo.LATERAL1:  # `__`
                self.direccion_x, self.direccion_y = -self.direccion_x, self.direccion_y
            elif objeto.tipo_espejo == TipoEspejo.LATERAL2:  # `|`
                self.direccion_x, self.direccion_y = self.direccion_x, -self.direccion_y
            return False
        elif objeto.tipo == TipoObjeto.OBSTACULO:
            print(f"La luz ha chocado con un obstáculo en ({proxima_y}, {proxima_x})")
            return True
        return False
    
    def viajar_luz(self, tablero):
        while True:
            if self.detectar_choque(tablero):
                break

            # Actualizar la posición de la luz en el tablero
            tablero.colocar_objeto(self.x, self.y, Objeto(self.x, self.y, TipoObjeto.VACIO))  # Limpia la posición actual

            # Mueve la luz en la dirección asignada
            self.x += self.direccion_x
            self.y += self.direccion_y

            # Coloca la luz en la nueva posición y muestra el tablero
            tablero.colocar_objeto(self.x, self.y, self)
            tablero.mostrar_tablero()

            # Pausa para visualización
            time.sleep(0.5)
