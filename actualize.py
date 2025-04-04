import json
from clients import customers
# Archivo donde se guardan los clientes (ajusta el nombre)
CLIENTS_FILE = "clients.json"

def load_clients():
    """Carga los datos de clientes desde el JSON."""
    try:
        with open(CLIENTS_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("¡Error! El archivo no existe.")
        return []
    except json.JSONDecodeError:
        print("¡Error! El archivo JSON está corrupto o vacío.")
        return []

def save_clients(data):
    """Guarda los datos actualizados en el JSON."""
    with open(CLIENTS_FILE, "w") as file:
        json.dump(data, file, indent=4)

def update_client_info():
    """Permite al cliente actualizar su información personal."""
    clients = load_clients()
    
    if not clients:
        print("No hay clientes registrados.")
        return

    print("\n----- ACTUALIZAR INFORMACIÓN CLIENTE -----")
    
    while True:
        try:
            client_id = str(input("Ingrese su número de identificación (o 'salir' para cancelar): "))
            
            if client_id.lower() == "salir":
                print("Operación cancelada.")
                return
            
            # Buscar cliente
            client_found = None
            for client in clients:
                if client["Identificacion"] == client_id:
                    client_found = client
                    break
            
            if not client_found:
                print("Cliente no encontrado. Intente de nuevo o escriba 'salir'.")
                continue
            
            # Mostrar datos actuales
            print(f"\nDatos actuales de {client_found['Nombre']}:")
            print(f"- Celular: {client_found.get('Celular', 'No registrado')}")
            print(f"- Direccion: {client_found.get('Direccion', 'No registrada')}")
            
            # Menú de actualización
            print("\n¿Qué desea actualizar?")
            print("1. Celular")
            print("2. Direccion")
            print("3. Salir")
            
            option = input("Seleccione una opción (1-3): ")
            
            if option == "1":
                new_phone = input("Nuevo Celular: ")
                client_found["Celular"] = new_phone
                save_clients(clients)
                print("Celular actualizado correctamente.")
            elif option == "2":
                new_address = input("Nueva dirección: ")
                client_found["Direccion"] = new_address
                save_clients(clients)
                print("Dirección actualizada correctamente.")
            elif option == "3":
                print("Saliendo...")
                return
            else:
                print("Opción no válida.")
            
            break  # Salir del bucle si la actualización fue exitosa
            
        except Exception as e:
            print(f"Error inesperado: {e}")