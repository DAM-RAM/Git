#buscar un red donde entre ciertos host
#encontrar el numero de host que pueda albergar redes

    
    

def mensaje(posicion):
    mensajes=print("escribe el "+posicion+" de la mascara de red: ")
    

def binarios_ip(introducion):
    if introducion == 1:
        numero_host=int(input("escria el numero de host que desea encontrar en la red"))


    elif introducion == 2 :
        primer_numero=int(input(mensaje("primer")))
        if primer_numero == 255 :
            segundo_numero=int(input(mensaje("segundo")))
        elif primer_numero == 254 :
            primer_numero=ip_255
            segundo_numero=ip_0
            tercer_numero =ip_0
        elif primer_numero == 252 :
            primer_numero=ip_252
            segundo_numero=ip_0
            tercer_numero =ip_0
        elif primer_numero == 248 :
            primer_numero=ip_248
            segundo_numero=ip_0
            tercer_numero =ip_0
        elif primer_numero == 240 :
            primer_numero=ip_240
            segundo_numero=ip_0
            tercer_numero =ip_0
        elif primer_numero == 224 :
            primer_numero=ip_224
            segundo_numero=ip_0
            tercer_numero =ip_0
        elif primer_numero == 192 :
            primer_numero=ip_192
            segundo_numero=ip_0
            tercer_numero =ip_0
        elif primer_numero == 128 :
            primer_numero=ip_128
            segundo_numero=ip_0
            tercer_numero =ip_0
        elif primer_numero == 0 :
            primer_numero=ip_0
            segundo_numero=ip_0
            tercer_numero =ip_0
        else:

            print("ingresa un valor valido de mascara")
            if segundo_numero == 255 :
                tercer_numero=int(input(mensaje("tercer")))
                if tercer_numero ==255 :
                    cuarto_numero=int(input(mensaje("cuarto")))

    else :
        print("por favor escribe un valor que sea 1 o 2")
    

def run():
    mensaje="""
    Hola Bienvido al el programa que nos auyuda a
    ver y encontrar mascaras de red 

    Escribe 

    1 para encontrar la mascara de red donde existan x# de host
    2 para encontrar la cantidad de host que pueda entrar en una mascara
    """
    ip_255=(1,1,1,1,1,1,1,1)
    ip_254=(1,1,1,1,1,1,1,0)
    ip_252=(1,1,1,1,1,1,0,0)
    ip_248=(1,1,1,1,1,0,0,0)
    ip_240=(1,1,1,1,0,0,0,0)
    ip_224=(1,1,1,0,0,0,0,0)
    ip_192=(1,1,0,0,0,0,0,0)
    ip_128=(1,0,0,0,0,0,0,0)
    ip_0=(0,0,0,0,0,0,0,0)
    introducion=int(input(mensaje))
    contador=0
    for i in binarios_ip(introducion):
        for i in primer_numero:
            if i ==0:
                contador+1
        for i in segundo_numero:
            if i ==0:
                contador+1        
        for i in tercer_numero:
            if i ==0:
                contador+1
        for i in cuarto_numero:
            if i ==0:
                contador+1        


if __name__ == "__main__":
    run()