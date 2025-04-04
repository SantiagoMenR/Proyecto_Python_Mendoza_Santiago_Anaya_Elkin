import json

customers=[]

def register_clients():
    file=open("clients.json","w")
    # Esta funcion permite hacer el registro del cliente que va a enivar el paquete
    # Guardando sus datos y validando que sean datos permitidos
    customer= {"Nombre":"",
               "Apellidos":"",
               "Identificacion":"",
               "Tipo":"",
               "Direccion":"",
               "Fijo":"",
               "Celular":"",
               "Barrio":""
               }
    customer["Nombre"]=str(input("Por favor ingrese sus nombres\n")).title()
    customer["Apellidos"]=str(input("Por favor ingrese sus apellidos\n")).title()
    try:
        while True:
            customer["Tipo"]=int(input("Por favor escoja la opcion para su tipo de identificacion\n1. CC\n2. TI\n3. CE\n"))
            if customer["Tipo"] == 1:
                customer["Tipo"]="CC"
                break
            elif customer["Tipo"]==2:
                customer["Tipo"]="TI"
                break
            elif customer["Tipo"]==3:
                customer["Tipo"]="CE"
                break
            else:
                print("Error: Opcion no valida\nVuelvala a ingresar")
    except ValueError:
        print("Error: Tipo de dato no valido")
    
    # Se pide la identificacion como entero para que no pueda ingresar otro tipo de datos
    try:
        customer["Identificacion"]=int(input("Por favor ingrese su numero de identificacion\n"))
    except ValueError:
        print("Error: Tipo de dato no valido")
    
    customer["Identificacion"]=str(customer["Identificacion"])
    customer["Direccion"]=str(input("Por favor ingrese su direccion\n"))
    try:
        customer["Fijo"]=int(input("Por favor ingrese su telefono fijo\n"))
    except ValueError:
        print("Error: Tipo de dato no valido")
            
    while True:
        try:   
            customer["Celular"]=int(input("Por favor ingrese su numero de celular\n"))
            #Se cambia el tipo de dato a cadena para poder calcular su longitud
            length=len(str(customer["Celular"]))
            #Se cambia el tipo de dato para despues verificar su primer digito y se verifica que el primer digito sea 3
            customer["Celular"]=str(customer["Celular"])
            if length == 10 and customer["Celular"][0]=="3":
                break
            else:
                "Error: Numero de celular no valido\nVuelvalo a ingresar"
        except ValueError:
            print("Tipo de dato no valido")
    customer["Barrio"]=str(input("Por favor ingrese su barrio de residencia\n"))
    customers.append(customer)
    client=json.dumps(customers)
    file.write(client)
    print("Cliente registrado exitosamente")