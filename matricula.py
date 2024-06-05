import datos_matricula

def matricula_camper ():
    matriculas={}
    print("Bienvenido a matriculas")
    print("Aqui ingresara a los camper que pasaron la prueba inicial ")
    matriculas["nom_matricula"]= input("nombre_del_camper")
    matriculas["Estado"]= "En proceso de inscricion"
 
    datos_matricula.data.append(matriculas)
    datos_matricula.guardar_datos()
   
    
def mostrar_camper_admitidos():
    print("Los Campers registrados son:")
    for matriculas in datos_matricula.data: 
        print("Camper que paso la prueba", matriculas["nom_matricula"], "En Estado" , matriculas ["Estado"])