from datetime import datetime
import random
from clients import customers
import json
shipping_record=[]

def register_shipment():
    file=open("shipments.json","w")
    # Esta funcion permite registrar los datos de un envio, generar un numero de guia aleatorio y asignar un estado
    shipping= {"Fecha":"",
               "Hora":"",
               "Destinatario":{"Nombre":"",
                               "Direccion":"",
                               "Telefono":"",
                               "Ciudad":"",
                               "Barrio":""},
               "Identificacion":"",
               "Guia":"",
               "Estado":"",
               }
    now = datetime.now()
    shipping["Fecha"]=now.strftime("%Y-%m-%d")
    shipping["Hora"]=now.strftime("%H:%M:%S")
    shipping_record.append(shipping)
    shipping["Destinatario"]["Nombre"]=str(input("Escriba el nombre completo del destinatario\n"))
    shipping["Destinatario"]["Direccion"]=str(input("Escriba la direccion del destinatario\n"))
    while True:
        shipping["Destinatario"]["Telefono"]=int(input("Por favor ingrese el numero de telefono del destinatario\n"))
        #Se cambia el tipo de dato a cadena para poder calcular su longitud
        length=len(str(shipping["Destinatario"]["Telefono"]))
        shipping["Destinatario"]["Telefono"]=str(shipping["Destinatario"]["Telefono"])
        #Se verifica la longitud del numero y que el primer digito del numero sea 3, de lo contrario no es valido
        if length == 10 and shipping["Destinatario"]["Telefono"][0]=="3":
            break    
        else:
            print("Error: Numero de celular no valido\nVuelvalo a ingresar")
    shipping["Destinatario"]["Ciudad"]=str(input("Escriba la ciudad de residencia del destinatario\n"))
    shipping["Destinatario"]["Barrio"]=str(input("Escriba el barrio de residencia del destinatario\n"))
    while True:
        try:
            identificacion = input("Escriba el número de identificación del remitente\n")

            remitente_encontrado = None
            for customer in customers:
                if customer["Identificacion"] == identificacion:
                    remitente_encontrado = customer
                    break

            if remitente_encontrado:
                shipping["Identificacion"] = identificacion
                print("Remitente encontrado. Registro exitoso del envío.")
                break  
            else:
                print("Remitente no encontrado. Vuelva a ingresar el número de identificación.")
        except ValueError:
            print("Error: Tipo de dato no válido")
    shipping["Guia"]=random.randint(100000,999999)
    shipping["Guia"]=str(shipping["Guia"])
    print(f'El numero de guia es: {shipping["Guia"]}')
    shipping["Estado"]="Recibido"
    shipping_record.append(shipping)
    shipment=json.dumps(shipping_record)
    file.write(shipment)