import json

data = {}

RUTA_ARCHIVO = "gestioncamper.json"

def guardar_datos():
    global data
    global RUTA_ARCHIVO
    try:
        contenido = json.dumps(data, indent=4)
        with open(RUTA_ARCHIVO, "w") as file:
            file.write(contenido)
        print("Datos guardados exitosamente!!")
    except Exception:
        print("Error al guardar datos")

def cargar_datos():
    global data
    global RUTA_ARCHIVO
    try:
        with open(RUTA_ARCHIVO, "r") as file:
            data = json.load(file)
        print("Datos cargados exitosamente!!")
    except Exception:
        print("Error al cargar datos")

def registrar_camper():
    global data 
    doc = int( input("Ingrese el documento: "))
    camper = {}
    camper["Nombre"] = input("Ingrese el nombre del camper: ")
    camper["apellido"] = input("Ingrese los apellidos del camper: ")
    camper["direccion"] = input("Ingrese la dirección del camper: ")
    camper["acudiente"] = input("Ingrese el nombre del acudiente del camper: ")
    try:
        camper["telefono"] = int(input("Ingrese el número de contacto: "))
    except ValueError:
        print("Ingrese un valor válido para el número de contacto!")
        return
    camper["estado"] = ("")
    camper["riesgo"] = ("")
    camper["ruta"] = ("")
    camper["nota"] = ("")
    camper["grupo"] = ("")
    data[doc] = camper
    
    guardar_datos()
    
    
def estado_camper():
    global data
    doc = input("Ingrese el documento del camper al que se le asignara el estado: ")
    if doc in data:
        estado_del_camper = input("Ingrese el nuevo estado del camper: ")
        data[doc]["estado"] = estado_del_camper
        print("estado actualizado")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.")
        
def riesgo_camper():
    global data
    doc = input("Ingrese el documento del camper al que se le asignara el estado: ")
    if doc in data:
        riesgocamper = input("Ingrese el nuevo estado del camper ")
        data[doc]["riesgo"] = riesgocamper
        print("estado actualizado")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.")
        
def ruta_camper():
    global data
    doc = input("Ingrese el documento del camper al que se le asignara la ruta: ")
    if doc in data:
        rutacamper = input("Ingrese la ruta: ")
        data[doc]["ruta"] = rutacamper
        print("ruta actualizada")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.")

def nota_camper():
    global data
    doc = input("Ingrese el documento del camper al que se le asignara la nota: ")
    if doc in data:
        nota1 = float(input("Ingrese la primera nota (60%): "))
        porcentaje1 = 60

        nota2 = float(input("Ingrese la segunda nota (30%): "))
        porcentaje2 = 30

        nota3 = float(input("Ingrese la tercera nota (10%): "))
        porcentaje3 = 10

        if not isinstance(nota1, (int, float)) or not isinstance(nota2, (int, float)) or not isinstance(nota3, (int, float)):
            print("Las notas deben ser valores numéricos.")
            return

        if porcentaje1 + porcentaje2 + porcentaje3 != 100:
            print("Los porcentajes deben sumar 100%.")
            return

        nota_final = (nota1 * porcentaje1 / 100) + (nota2 * porcentaje2 / 100) + (nota3 * porcentaje3 / 100)

        data[doc]["nota"] = nota_final
        guardar_datos()
        print(f"La nota final del camper es: {nota_final}")
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.")
        
        
def eliminar_camper():
    global data
    doc = input("Ingrese el documento del camper que desea eliminar: ")
    if doc in data:
        del data[doc]
        print("Camper eliminado exitosamente!!")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.")


def grupo_camper():
    global data
    doc = input("Ingrese el documento del camper al que se le asignara el grupo: ")
    if doc in data:
        grupocamper = input("Ingrese el grupo al que sera asignado: ")
        data[doc]["grupo"] = grupocamper
        print("grupo asignado")
        guardar_datos()
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.")


def imprimir_nota_camper():
    global data
    doc = input("Ingrese el documento del camper para imprimir la nota: ")
    if doc in data:
        camper = data[doc]
        nombre = camper.get("Nombre", "")
        apellido = camper.get("apellido", "")
        nota = camper.get("nota", "")
        if nombre and apellido and nota:
            print(f"Nombre: {nombre} {apellido}, Nota Final: {nota}")
        else:
            print(f"No se encontró información completa para el camper.")
    else:
        print("El documento ingresado no corresponde a ningún camper registrado.") 
        
def imprimir_camper_info():
    global data
    print("Información de todos los Campers:\n")
    for doc, camper in data.items():
        nombre = camper.get("Nombre", "")
        apellido = camper.get("apellido", "")
        if nombre and apellido:
            print(f"Documento: {doc}, Nombre: {nombre} {apellido}")
        else:
            print(f"No se encontró información completa para el camper con documento {doc}.")
