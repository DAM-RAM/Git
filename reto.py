#en el programa se desea que u
#un usuario digite la base de una potencia
#escojer esponente
# escojer el numero al que desea llegar
# y saber cual numero es divicible


def potencia(base, exponente_final,exponente_inicial, resultado,resultados,multiplo):
    while exponente_inicial <= exponente_final :
        exponente_inicial= exponente_inicial + 1
        resultado = base ** exponente_inicial
        if resultado % multiplo ==0:
            resultados.append(resultado)
    print(resultados)

def preguntar_si(respuesta):
    respuesta= respuesta.replace(" ","").lower()
    if respuesta == "si":
        return True
    elif respuesta == "no":
        return False
    else:
        print(" por favor diga una opcion valida entre si o no")




def run():
    introduccion = print ("""señor usurio sea biennido a la primera, pueba de codigo
en el programa se te pedira un numero base y una base)
""")
    base = int(input ("señor usuario por favor escriba la base para su potencia: "))
    exponente_inicial =int(input ( "señor usuario por favor escriba el exponente incial de su pontencia : "))
    exponente_final =  int(input ("señor usuario por favor escriba el exponente limite de su pontencia : "))
    resultado = [base ** exponente_inicial]
    respuesta = str(input("señor usuio responda no o si si desea encontrar multiplos: "))
    resultados=[]
    preguntar_si(respuesta)
    if preguntar_si(respuesta):
        multiplo=int(input("señor usuario escriba el numero que escriba el numero que sea saber sus multiplos: "))
        potencia(base, exponente_final,exponente_inicial, resultado,resultados,multiplo)
    
               
    else:
        multiplo=1
        potencia(base, exponente_final,exponente_inicial, resultado,resultados,multiplo)

    
    
    
if __name__ == "__main__" :
    run()