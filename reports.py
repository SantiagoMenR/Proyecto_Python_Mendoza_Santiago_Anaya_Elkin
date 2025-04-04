import json
from datetime import datetime

def cargar_envios():
    """Carga los datos de envíos desde el JSON"""
    try:
        with open('shipments.json', 'r', encoding='utf-8') as file:
            return json.load(file)
    except Exception as e:
        print(f"Error cargando envíos: {str(e)}")
        return []


def generar_informe():
    """Genera y muestra el informe básico"""
    envios = cargar_envios()
    if not envios:
        print("No hay datos de envíos disponibles")
        return

    # Contadores
    total_envios = 0
    entregados = 0
    
    print("\n=== INFORME DE ENVÍOS ===")
    
    for envio in envios:
        total_envios += 1
        estado = envio.get('Estado', 'Desconocido')
        
        if estado == "Entregado":
            entregados += 1
    
    # Mostrar resultados
    print(f"\nTotal de envíos: {total_envios}")
    print(f"Envíos entregados: {entregados} ({entregados/total_envios*100:.1f}%)")
    

def menu_informes():
    """Menú simple para informes"""
    while True:
        print("\n=== MENÚ INFORMES ===")
        print("1. Generar informe de envíos")
        print("2. Volver al menú principal")
        
        opcion = input("Selección: ")
        
        if opcion == "1":
            generar_informe()
        elif opcion == "2":
            break
        else:
            print("Opción no válida")