from envios import shipping_record
import json

states = ["Recibido", "En transito", "En ciudad de destino", "En bodega de la transportadora", "En reparto", "Entregado"]

JSON_FILE = "shipments.json"

def load_shipping_data():
    # Carga los datos de envíos desde el JSON.
    try:
        with open(JSON_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("¡Error! El archivo no existe.")
        return []
    except json.JSONDecodeError:
        print("¡Error! El archivo JSON está corrupto o vacío.")
        return []

def save_shipping_data(data):
    # Guarda los datos actualizados en el JSON.
    with open(JSON_FILE, "w") as file:
        json.dump(data, file, indent=4)

def actualize_state():
    # Actualiza el estado de un envío según su número de guía.
    shipping_data = load_shipping_data()
    
    if not shipping_data:
        print("No hay envíos registrados.")
        return

    while True:
        try:
            guide = input("\nEscriba el número de guía del paquete: ")
            break
        except ValueError:
            print("Error: Ingrese un número válido.")

    # Buscar el envío
    found_shipment = None
    for shipment in shipping_data:
        if shipment["Guia"] == guide:
            found_shipment = shipment
            break

    if not found_shipment:
        print("Envío no encontrado.")
        return

    print("\n--- ESTADOS DISPONIBLES ---")
    for i, state in enumerate(states, start=1):
        print(f"{i}. {state}")

    while True:
        try:
            option = int(input("\nSeleccione el nuevo estado: ")) - 1
            if 0 <= option < len(states):
                found_shipment["Estado"] = states[option]
                save_shipping_data(shipping_data)
                print(f"Estado actualizado a: {states[option]}")
                break
            else:
                print("Opción no válida. Intente de nuevo.")
        except ValueError:
            print("Error: Ingrese un número válido.")