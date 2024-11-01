"""GRUPO 6 - 
    Nombres: 1. Andres Felipe Rubiano Marrugo -T00077084 
             2. Cristian Benitez - T00078658
             3. Jesús Andrés Pérez -T00078491
             4. Israel Hoyos  -T00069427
             5. Santiago payares - T00068704"""
import apoyo as ap
from mapas import Mapas

def main():
    # Mostrar mapas disponibles
    Mapas.listar_mapas()
    
    while True:
        try:
            nivel = int(input("\nSeleccione un nivel (1-2): "))
            if nivel not in [1, 2]:
                print("Por favor seleccione un nivel válido")
                continue
            break
        except ValueError:
            print("Por favor ingrese un número válido")
    
    # Obtener configuración del mapa
    config_mapa = Mapas.obtener_mapa(nivel)
    
    # Crear instancia del juego con la configuración del mapa
    juego = ap.Juego(tamano=config_mapa['tamano'])
    
    # Configurar el nivel
    juego.configurar_nivel_personalizado(
        pos_luz=config_mapa['luz_pos'],
        dir_luz=config_mapa['luz_dir'],
        pos_meta=config_mapa['meta_pos'],
        obstaculos=config_mapa['obstaculos']
    )
    
    # Mostrar descripción del nivel
    print(config_mapa['descripcion'])
    input("Presione Enter para comenzar...")

    while True:
        juego.mostrar_tablero()
        print("\nOpciones:")
        print("1. Colocar espejo")
        print("2. Simular trayectoria de luz")
        print("3. Ver historial")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción: ")
        
        if opcion == "1":
            try:
                x = int(input("Ingrese posición X: "))
                y = int(input("Ingrese posición Y: "))
                print("\nTipos de espejo:")
                print("1: Diagonal (/)   2: Diagonal (\\)")
                print("3: Horizontal (─)  4: Vertical (│)")
                tipo = int(input("Seleccione tipo de espejo: "))
                if tipo not in [1, 2, 3, 4]:
                    print("Tipo de espejo inválido")
                    continue
                    
                exito, mensaje = juego.colocar_espejo(x, y, tipo)
                print(mensaje)
            except ValueError:
                print("Entrada inválida")
                
        elif opcion == "2":
            juego.simular_luz()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "3":
            juego.mostrar_historial()
            input("\nPresione Enter para continuar...")
            
        elif opcion == "4":
            print("¡Gracias por jugar!")
            break

if __name__ == "__main__":
    main()
