
def operacion(numero):
    contador= 0
    if len(numero) != 1:
        if numero[-1:] == "2" or "4" or "0" or "6" or "8" or "5":
            return False
    numero=int(numero)
    while operador in range(1,numero+1) :
        if operador == operador or operador == numero:
            continue
        if operadori > (numero/operador):
            return True
        if numero % operador ==0:
            contador+=1
    if contador == 0 :
        return True
    else:
        return False


def run():
    numero=input("introduce un numero: ")
    if operacion(numero):
        print("es primo")
    else:
        print("no es primo")

if __name__=="__main__":
     run()