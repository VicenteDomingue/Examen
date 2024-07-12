import random
trabajadores = ["Juan Pérez","María García","Carlos López","Ana Martínez","Pedro Rodríguez","Laura Hernández","MiguelSánchez","Isabel Gómez","Francisco Díaz","Elena Fernández"]
listaTrabajadoresSueldos=[]

def asignar_sueldos_aleatorios():
    for NombreDeTrabajador in trabajadores:
        Sueldos=random.randint(300000,2500000)
        listaTrabajadoresSueldos.append([NombreDeTrabajador,Sueldos])
        
sueldosMenores=[]
sueldosMedios=[]
sueldosMayores=[]

def Clasificar_Sueldos():
    
    for trabajadores,sueldos in listaTrabajadoresSueldos:
        if sueldos<800000:
            sueldosMenores.append(sueldos)
        elif sueldos>=800000 and sueldos<2000000:
            sueldosMedios.append(sueldos)
        elif sueldos>=2000000:
            sueldosMayores.append(sueldos)

def Ver_estadísticas():
    estadísticas=[sueldosMayores,sueldosMedios,sueldosMenores]
    estadísticas.sort()

def Salir_del_programa():
    print("Finalizando programa…")
    exit
    
    
asignar_sueldos_aleatorios()    
print(listaTrabajadoresSueldos)


Clasificar_Sueldos()

print (sueldosMenores)
print (sueldosMedios)
print (sueldosMayores)

Ver_estadísticas()

Salir_del_programa()