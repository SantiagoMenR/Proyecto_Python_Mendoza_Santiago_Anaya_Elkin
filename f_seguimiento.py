from envios import shipping_record

import json

JSON_FILE = "shipments.json"

def load_shipping_data():
    """Carga los datos de envíos desde el JSON."""
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("¡Error! El archivo no existe.")
        return []
    except json.JSONDecodeError:
        print("¡Error! El archivo JSON está corrupto o vacío.")
        return []

def follow_shipping():
    """Busca un paquete por número de guía y muestra su estado."""
    print("\n----- MENU DE SEGUIMIENTO -----")
    shipping_data = load_shipping_data()  # Cargar datos del JSON

    if not shipping_data:
        print("No hay envíos registrados.")
        return

    while True:
        try:
            number_g = input("Ingrese el número de guía del envío: ")
            break
        except ValueError:
            print("Error: Ingrese un número válido.")

    # Buscar el paquete en los datos cargados del JSON
    found = False
    for shipment in shipping_data:
        if shipment["Guia"] == number_g:
            print(f"\nPaquete encontrado:")
            print(f"- Número de guía: {shipment['Guia']}")
            print(f"- Estado actual: {shipment['Estado']}")
            if "Destino" in shipment:  # Opcional: Mostrar más detalles si existen
                print(f"- Destino: {shipment['Destino']}")
            found = True
            break

    if not found:
        print("No se encontró un envío con ese número de guía.")