# agenda inicicial
print("Agenda:") 
recordatorios = [['2021-01-01', "11:00", "Levantarse y ejercitar"],
 ['2021-05-01', "15:00", "No trabajar"],
 ['2021-07-15', "13:00", "No hacer nada es feriado"],
 ['2021-09-18', "16:00", "Ramadas"],
 ['2021-12-25', "00:00", "Navidad"]]
for recordatorio in recordatorios:
        print(recordatorio)  
# Cambios
resp0 = input("Quiere hacer un cambio s=si o n=no\n")
if resp0 =="s":
    resp1 = input("Que cambio quiere hacer: a =  agregar dato, r = revisar dato, e = eliminar dato\n")
# Agregar
    if resp1 =="a":
        fecha = input("Por favor, introduce la fecha del recordatorio (formato AAAA-MM-DD):\n")
        hora = input("Por favor, introduce la hora del recordatorio (formato HH:MM):\n")
        evento = input("Por favor, introduce la descripción del evento:\n")
        recordatorios.append([fecha, hora, evento])
        recordatorios.sort()
        for recordatorio in recordatorios:
            print(recordatorio)
# Revisar        
    if resp1 =="r":
        camb = int(input("linea a cambiar:\n")) - 1
        if camb < len(recordatorios):
            fecha = input("Introduce la nueva fecha del recordatorio (formato AAAA-MM-DD):\n")
            hora = input("Introduce la nueva hora del recordatorio (formato HH:MM):\n")
            evento = input("Introduce la nueva descripción del evento:\n")
            recordatorios[camb] = [fecha, hora, evento]
            recordatorios.sort()
            print("Agenda actualizada:")
            for recordatorio in recordatorios:
                print(recordatorio)
        else:
            print("El índice está fuera de rango.")
# Elimninar    
    if resp1 == "e":
        elim = int(input("linea a borrar:\n")) - 1
        if elim < len(recordatorios):
            del recordatorios[elim]
            recordatorios.sort()
            print("Agenda actualizada:")
            for recordatorio in recordatorios:
                print(recordatorio)
        else:
            print("El índice está fuera de rango.")      
else:
    print("Agenda")
    for recordatorio in recordatorios:
        print(recordatorio)


    

