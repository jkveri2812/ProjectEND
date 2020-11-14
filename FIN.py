from datetime import datetime
from io import open
import random
import requests
    #Definición de coneccion a la api binance

_ENDPOINT = "https://api.binance.com" #aqui definimos la base de la URL del API de binance
def _url(api):
        return _ENDPOINT+api
        #esta funciona toma la base  y le concatena lo que le agregamos como api

def get_price(cripto):
    return requests.get(_url("/api/v3/ticker/price?symbol="+cripto))

def esmoneda (cripto):
    return cripto in monedas
user=[]
monedas=()
monedas_dic={}
saldo=30
historialTransacciones=[]

headers = {  'Accepts': 'application/json',  'X-CMC_PRO_API_KEY':  '4f6bb077-95a9-479c-8b97-9c01ed91a61a'}
lista = []
data = requests.get("https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest",headers=headers).json()

for cripto in data ["data"]:
    monedas_dic[cripto["symbol"]]=cripto["name"]

monedas = monedas_dic.keys()

for c in data["data"]:
	lista.append(c["symbol"])

listaTupla = tuple(lista)

def erase():
    delete=input("¿Deseas borrar los datos de tus monedas? "
    "Tendrías que agregarlas nuevamente (Y/N)"
    " Usa esta opción en caso de que hayas cometido un error): ").upper()
    if delete=="Y":
            print("Borrando...")
            archivo = open('moneda.txt','w')
            archivo.write('')
            archivo.close()
            seguirPrograma=input("¿Deseas continuar ejecutando el programa? (Y/N): ").upper()
            if seguirPrograma=="Y":
                print("Continuando el programa...")
            elif seguirPrograma=="N":
                print("Entendido. Saliendo...")
                exit()
            else:
                print("Elige 'Y' para sí y 'N' para no...")
                exit()
            datos()
            erase()
    elif delete=="N":
        print("Finalizando introducción de monedas...")
        pass
    else:
        print("Escribe Y o N según lo que escojas.")

def inicioRecepcion():
    print("Recepción de monedas.")
    datos()

def datos():
    global saldo
    global moneda
    global moneda2
    global moneda3
    global cantidad
    global cantidad2
    global cantidad3
    i=0
    while i<3:
        archivo_moneda=open('cantidadMoneda.txt', 'r+')
        #Listas de cantidad y moneda:
        leerMoneda=archivo_moneda.readlines()
        archivo_moneda.close()
        if i==0:
            moneda=input("Ingrese la moneda: ")
            try:
                cantidad=float(input("Ingrese la cantidad de "+moneda+": "))
            except:
                print("Ingresa una cantidad en números.")
            print("Nombre completo de la moneda: ", monedas_dic.get(moneda),
            " Nombre código de la moneda: ", moneda)
            #Moneda:
            archivo_moneda=open('moneda.txt','a')
            archivo_moneda.write(moneda)
            archivo_moneda.write(" \n")
            leerMoneda.append(moneda)
            print("leerMoneda:")
            print(leerMoneda)
            archivo_moneda.close()
            #Cantidad:


            if not moneda in listaTupla:
                print("La moneda es inválida")
                erase()
                inicioRecepcion()
            else:
                archivo_moneda=open('moneda.txt','r')
                print("Moneda correcta.")
                data = get_price(moneda+"USDT").json()
                print("El precio de",moneda,"es",data["price"])
                int(float(data["price"]))

                cotización=int(float(data["price"]))
                acumulado=cantidad*cotización
                print("Usted tiene ",acumulado,"USD de su moneda ",moneda)
                saldo = saldo + acumulado
                print("Por ahora, en tu billetera dígital posees: ",saldo)
                archivo_moneda.close()

        elif i==1:
            archivo_moneda=open('moneda.txt','a')
            moneda2=input("Ingrese la moneda 2: ")
            try:
                cantidad2=float(input("Ingrese la cantidad de "+moneda2+": "))
            except:
                print("Ingresa una cantidad en números.")
            print("Nombre completo de la moneda: ", monedas_dic.get(moneda2),
            " Nombre código de la moneda: ", moneda2)
            archivo_moneda.write(moneda2)
            archivo_moneda.write(" \n")
            leerMoneda.append(moneda2)
            print("leerMoneda:")
            print(leerMoneda)
            archivo_moneda.close()


            if not moneda2 in listaTupla:
                print("La moneda es inválida")
                erase()
                inicioRecepcion()
            else:
                archivo_moneda=open('moneda.txt','r')
                print("Moneda correcta.")
                data = get_price(moneda2+"USDT").json()
                print("El precio de",moneda2,"es",data["price"])
                int(float(data["price"]))

                cotización=int(float(data["price"]))
                acumulado=cantidad2*cotización
                print("Usted tiene ",acumulado,"USD de su moneda ",moneda2)
                saldo = saldo + acumulado
                print("Por ahora, en tu billetera dígital posees: ",saldo)
                archivo_moneda.close()
        elif i==2:
            archivo_moneda=open('moneda.txt','a')
            moneda3=input("Ingrese la moneda 3: ")
            try:
                cantidad3=float(input("Ingrese la cantidad de "+moneda3+": "))
            except:
                print("Ingresa una cantidad en números.")
                exit()

            print("Nombre completo de la moneda: ", monedas_dic.get(moneda3),
            " Nombre código de la moneda: ", moneda3)
            archivo_moneda.write(moneda3)
            archivo_moneda.write(" \n")
            leerMoneda.append(moneda3)
            print("leerMoneda:")
            print(leerMoneda)
            archivo_moneda.close()


            if not moneda3 in listaTupla:
                print("La moneda es inválida")
                erase()
                inicioRecepcion()
            else:
                archivo_moneda=open('moneda.txt','r')
                print("Moneda correcta.")
                data = get_price(moneda3+"USDT").json()
                print("El precio de",moneda3,"es",data["price"])
                int(float(data["price"]))

                cotización=int(float(data["price"]))
                acumulado=cantidad3*cotización
                print("Usted tiene ",acumulado,"USD de su moneda ",moneda3)
                saldo = saldo + acumulado
                print("Por ahora, en tu billetera dígital posees: ",saldo)
                archivo_moneda.close()

                archivo_saldo=open('saldo.txt','w')
                archivo_saldo.write(str(saldo))
                archivo_saldo.close()

                archivo_saldo=open('saldo.txt','r')
                leerSaldo=archivo_saldo.readlines()
                print("TOTAL billetera: ",leerSaldo)
                archivo_saldo.close()

                archivo_cantidad=open('cantidadMoneda.txt','w')
                archivo_cantidad.close()

                archivo_cantidad=open('cantidadMoneda.txt', 'w+')
                leerCantidad=archivo_cantidad.readlines()
                archivo_cantidad.write(str(cantidad))
                archivo_cantidad.write(" \n")
                archivo_cantidad.write(str(cantidad2))
                archivo_cantidad.write(" \n")
                archivo_cantidad.write(str(cantidad3))
                archivo_cantidad.write(" \n")
                leerCantidad.append(cantidad)
                leerCantidad.append(cantidad2)
                leerCantidad.append(cantidad3)
                print("Leer cantidad: ")
                print(leerCantidad)
                archivo_cantidad.close()
        else:
            pass
        i=i+1

print("Proyecto final fundamentos de progrmación en Python.")


entrada=input("Ingrese 'Y' para iniciar el programa, o 'N' para finalizar: ").upper()

while entrada!="Y":
    print("Cerrando...")
    entrada=input("Ingrese 'Y' para continuar, o 'N' para finalizar: ").upper()

else:
    print("El programa continua.")
    def borrar():
        archivo = open('usuario.txt','w')
        archivo.write('')
        archivo.close()
    def entrar():
        print("----------LOGIN----------")
        try:
            login=input("Introduce tu usuario: ")
            archivo_usuario=open('usuario.txt')

            leerUsuario=archivo_usuario.readlines()

            archivo_usuario.close()

            while login!=leerUsuario[0]:
                print("Incorrecto...")
                login=input("Introduce tu usuario: ")
            else:
                print("¡Correcto!")
                print("Bienvenido. Ingresa lo que deseas hacer \n"
                "1.Ir al menú principal \n"
                "2. Volver atrás. \n"
                "3. Borrar archivo \n")
                menu=input("Selecciona una de estas opciones: ")
                if menu=="1":
                    print("Ingresando al Menú principal...")
                    pass
                elif menu=="2":
                    entrar()
                elif menu=="3":
                    print("Borrando...")
                    eleccionBorrar()
                else:
                    print("Seleccione una de las tres opciones.")
        except:
            print("Este usuario no existe.")
            exit()

    def eleccionBorrar():
        borrarUser=input("¿Deseas borrar el usuario creado? (Y/N): ").upper()
        if borrarUser=="Y":
            borrar()
        elif borrarUser=="N":
            print("El usuario permanecera guardado.")
        else:
            print("Ingresa Y para sí, y N para no.")
    print("Hola")
    eleccion=input("Registrate con 'R', o realiza tu login con 'L', salir con 'E', o hacer reset con 'B': ").upper()
    while len(eleccion)>1:
        print("Solo una letra...")
        eleccion=input("Registrate con 'R', o realiza tu login con 'L', salir con 'E', o hacer reset con 'B': ").upper()
    if eleccion=="R":
        archivo_usuario=open('usuario.txt','w+')
        newUser=input("Introduce un nuevo usuario:  ")
        archivo_usuario.write(newUser)

        archivo_usuario.close()


        archivo_usuario=open('usuario.txt')
        print(archivo_usuario.read())
        archivo_usuario.close()
    elif eleccion=="L":
        entrar()
    elif eleccion=="E":
        print("Saliendo....")
        exit()
    elif eleccion=="B":
        print("Borrando datos...")
        borrar()
        exit()
    else:
        print("Escribe solo una letra, que sea de acuerdo a las opciones...")
        exit()

    start=input("Si ya tienes tus monedas registradas escribe 'Y'. Sí no, escribe 'N': ").upper()
    if start=="Y":
        borrarSisi=input("¿Deseas borrar los datos de tus monedas?"
        "(Escribe como siempre Y o N): ")
        if  borrarSisi=="Y":
            erase()
        else:
            print("Listo, continuemos...")
            pass
    elif start=="N":
        inicioRecepcion()
        erase()
    else:
        print("Escribe Y o N, no otra cosa...")
        exit()


    menuBucle=True
    while menuBucle==True:
        print("-------------------Menú de opciones: --------------------------")
        print("1-Recibir cantidad \n"
        "2-Transferir monto. \n"
        "3-Mostrar balance de una moneda. \n"
        "4-Mostrar balance general.\n"
        "5-Mostrar histórico de transacciones \n"
        "6-Salir del programa.")
        try:
            menu=int(input("Introduzca el número de la opción que elija: "))
        except:
            print("Introduce un número de acuerdo a las opciones, no una letra o un carácter.")
            menu=int(input("Introduzca el número de la opción que elija: "))


        if menu==1:
            print("-------------------Ingresando: Recibir cantidad.-------------------")
            print("Este apartado: \n"
            "Envia un monto en USD de alguna de las criptomonedas a un destinatario indicado (identificado por un código)")
            historialTransacciones.append("Ingresando: Recibir cantidad.")
            print("Revisaremos si tienes una solicitud de transferencia de monto...")
            solicitud=bool(random.getrandbits(1))
            print(solicitud)
            if solicitud==True:
                print("Efectivamente, tienes una solicitud de transferencia de monto.")
                preguntaRecibir=input("¿Deseas recibir el monto? (Y/N) ").upper()
                if preguntaRecibir=="Y":
                    recepcion=400
                    print("Vas a recibir una cantidad de... "+str(recepcion)+" dolares.")
                    saldo=saldo+recepcion
                    archivo_saldo=open('saldo.txt','w')
                    archivo_saldo.write(str(saldo))
                    archivo_saldo.close()
                    print("Ahora tienes en tu billetera:" +str(saldo)+" dolares.")
                elif preguntaRecibir=="N":
                    print("Se ha rechazado correctamente la transferencia de dinero.")
                else:
                    print("Introduce 'Y' para sí, o 'N' para no.")
            else:
                print("No, no tienes solicitudes pendientes.")


        elif menu==2:
            print("--------------Ingresando: Transferir monto.-------------------")
            print("Este apartado: \n"
            "Recibe de un enviador (identificado por un código) una cantidad de alguna criptomoneda")
            historialTransacciones.append("Ingresando: Transferir monto.")

            print("-------------------------------------------------")

            decisionTransferencia=print("¿Desea transferir su monto?")

            transferencia=input("Ingrese 'Y' para continuar, o 'N' para cancelar: ").upper()

            while transferencia!="Y":
                print("Cancelando. El programa ha finalizado.")
                break
            else:
                print("El programa continua en transferencia de monto.")
                name=input("Ingrese el nombre de usuario de la persona a la que va a transferir: ")
                while len(name)<7:
                    print("No existen nombres de usario menores a 7 carácteres. Intentalo de nuevo...")
                    name=input("Ingrese el nombre de usuario de la persona a la que va a transferir: ")
                else:
                    print("Usuario: ",name, "¿Seguro? ")
                    guita=input("Escriba Y/N: ").upper()
                    while guita!="Y":
                        print("cancel")
                    else:
                        print("Continua el programa.")
                        print("Recuerda que en tu billetera, en total posees: ",saldo)

                        try:
                            pasarDinero=int(input("Introduce qué cantidad de tu moneda deseas transferir: "))
                        except:
                            print("Introduce una cantidad válida de dinero.")
                            pasarDinero=int(input("Introduce qué cantidad de tu moneda deseas transferir: "))
                        if saldo<pasarDinero:
                            print("No tienes suficiente dinero.")
                        else:
                            saldo=saldo-pasarDinero
                            print("Transferencia completada.")

                            archivo_saldo=open('saldo.txt','w')
                            archivo_saldo.write(str(saldo))
                            archivo_saldo.close()
                            print("Ahora tienes en tu billetera: ",str(saldo))


        elif menu==3:
            print("-------------------Ingresando: Mostrar balance de una moneda.-------------------")
            print("Este apartado: \n"
            "Consulta el balance de cada una de las criptomonedas en USD.")
            historialTransacciones.append("Ingresando: Mostrar balance de una moneda.")
            balanceMoneda=input("Introduce la moneda que quieras validar su existencia: ")
            try:
                balanceCantidad=int(input("Introduce la cantidad de la moneda que deseas validar: "))
            except:
                print("Escribe una cantidad en números.")
                exit()
            if not balanceMoneda in listaTupla:
                print("La moneda es inválida, no existe, o esta mal escrita...")
            else:
                print("La moneda es válida, puedes usarla aquí.")
                print("Nombre completo de la moneda: ", monedas_dic.get(balanceMoneda),
                " Nombre código de la moneda: ", balanceMoneda)

                data = get_price(balanceMoneda+"USDT").json()
                print("El precio de",balanceMoneda,"es",data["price"])
                int(float(data["price"]))
                count=0
                while count < 1:
                    profit=random.uniform(-0.03,0.03)
                    balanceCantidad=balanceCantidad+(balanceCantidad*profit)
                    count=count+1
                    print("Saldo de",balanceMoneda,"el dia de hoy"," es de: %6.7f"%balanceCantidad+". Ganacia de %6.2f"%(profit*100),"%")


        elif menu==4:
            print("-------------------Ingresando: Mostrar balance general.-------------------")
            historialTransacciones.append("Ingresando: Mostrar balance general.")
            print("Este apartado: \n"
            "Consulta el balance general del usuario en USD usando el precio de la criptomoneda provisto por las APIs de coinmarketcap.com")

            count=0
            print("Primera moneda: ")

            archivo_moneda=open('moneda.txt','r')
            leerMoneda=archivo_moneda.readlines()
            archivo_moneda.close()
            print(leerMoneda[0])
            moneda=leerMoneda[0]

            print("Cantidad de la moneda 1:")
            archivo_cantidad=open('cantidadMoneda.txt','r')
            leerCantidad=archivo_cantidad.readlines()
            archivo_cantidad.close()
            print(leerCantidad[0])
            cantidad=int(float(leerCantidad[0]))

            while count < 7:
                profit=random.uniform(-0.03,0.03)
                cantidad=cantidad+(cantidad*profit)
                count=count+1
                print("Saldo de",moneda,"el dia",count,"es de: %6.7f"%cantidad+". Ganacia de %6.2f"%(profit*100),"%")

            print("Segunda moneda: ")

            archivo_moneda=open('moneda.txt','r')
            leerMoneda=archivo_moneda.readlines()
            archivo_moneda.close()
            print(leerMoneda[1])
            moneda2=leerMoneda[1]

            print("Cantidad de la moneda 2:")
            archivo_cantidad=open('cantidadMoneda.txt','r')
            leerCantidad=archivo_cantidad.readlines()
            archivo_cantidad.close()
            print(leerCantidad[1])
            cantidad2=int(float(leerCantidad[1]))

            count=0
            while count < 7:
                profit=random.uniform(-0.03,0.03)
                cantidad2=cantidad2+(cantidad2*profit)
                count=count+1
                print("Saldo de",moneda2,"el dia",count,"es de: %6.7f"%cantidad2+". Ganacia de %6.2f"%(profit*100),"%")

            print("Tercera moneda: ")

            archivo_moneda=open('moneda.txt','r')
            leerMoneda=archivo_moneda.readlines()
            archivo_moneda.close()
            print(leerMoneda[2])
            moneda3=leerMoneda[2]

            print("Cantidad de la moneda 3:")
            archivo_cantidad=open('cantidadMoneda.txt','r')
            leerCantidad=archivo_cantidad.readlines()
            archivo_cantidad.close()
            print(leerCantidad[2])
            cantidad3=int(float(leerCantidad[2]))

            count=0
            while count < 7:
                profit=random.uniform(-0.03,0.03)
                cantidad3=cantidad3+(cantidad3*profit)
                count=count+1
                print("Saldo de",moneda3,"el dia",count,"es de: %6.7f"%cantidad3+". Ganacia de %6.2f"%(profit*100),"%")

            archivo_saldo=open('saldo.txt','r')
            leerSaldo=archivo_saldo.readlines()
            print("TOTAL billetera: ",leerSaldo)
            archivo_saldo.close()


        elif menu==5:
            print("-------------------Ingresando: Mostrar histórico de transacciones.-------------------")
            print("Este apartado: \n"
            "Emite un histórico de transacciones del usuario indicando fecha, moneda, cantidad y monto en USD para el momento de la transacción")
            historialTransacciones.append("Ingresando: Mostrar histórico de transacciones.")
            print("Has accedido a lo siguiente: ")
            print(historialTransacciones[:])

            print("Has accedido bajo el usuario de: ")
            archivo_usuario=open('usuario.txt','r')
            mostrarHistorialUsuario=archivo_usuario.read()
            archivo_usuario.close()
            print(mostrarHistorialUsuario)

            ahora = datetime.now()
            print("La fecha completa y hora en la que hizo las transacciones fue: " + ahora.strftime("%A, %d de %B de %Y a las %I:%M:%S%p"))

        elif menu==6:
            print("-------------------Saliendo.-------------------")
            menuBucle=False
        else:
            print("Ingrese algun número del 1 al 6 de acuerdo a la opción que elija.")
    else:
        exit()











