import datos_graduados

def campers_graduadoss ():
    graduadoo={}
    graduadoo["nombre"]=input("Ingrese el nombre del campers graduado para guardarlo en la base de tatos graduados")
    
    datos_graduados.data.append(graduadoo)
    datos_graduados.guardar_datos()
    


def mostrar_camper_graduados():
    print("Los campers graduados son: ")
    for graduadoo in datos_graduados.data:
        print("Los campers son:" , graduadoo["nombre"])