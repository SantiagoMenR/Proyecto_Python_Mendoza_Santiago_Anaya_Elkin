import json
from clients import register_clients
from envios import register_shipment
from f_seguimiento import follow_shipping
from state import actualize_state
from actualize import update_client_info
from reports import menu_informes
while True:
    print("------- MENU PRINCIPAL -------")
    option=int(input("1. Registrar cliente\n2. Menu de empleado\n3. Seguimiento de envio\n4. Actualizar estado del envio\n5. Actualizar datos del cliente\n6. Generar informe\n7. Salir\n"))
    
    if option==1:
        register_clients()
    elif option==2:
        register_shipment()
    elif option==3:
        follow_shipping()
    elif option==4:
        actualize_state()
    elif option==5:
        update_client_info()
    elif option==6:
        menu_informes()
    elif option==7:
        break
    else:
        print("Opcion no valida\nIngrese otra opcion")

print("Saliendo del programa...")
    
        
    

