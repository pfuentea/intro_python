import sys

if len(sys.argv) < 5: # 5 cantidad de argumentos 
    print("Error: falta argumentos")
    print("Uso: python conversiones.py 0.0046 0.093 10000")
    sys.exit(1)
else:
    sol=float(sys.argv[1])
    peso_argentino=float(sys.argv[2])
    dolar=float(sys.argv[3])
    pesos_chilenos=float(sys.argv[4])

    print(f"Los {pesos_chilenos} pesos equivalen a:")
    print(f"{pesos_chilenos * sol} Soles")
    print(f"{pesos_chilenos * peso_argentino} Pesos Argentinos")
    print(f"{pesos_chilenos * dolar} Dólares")


