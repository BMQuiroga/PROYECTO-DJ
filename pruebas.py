LARGO = 1024
ALTO = 696

def pixel_to_number(pixel):
    return (pixel - (LARGO/2)) / 100

def number_to_pixel(number):
    return round ((number*-100) + (ALTO/2))

def graficar(funcion):
    
    for i in range(LARGO):
        q = pixel_to_number(i) #Valor con el que se va a graficar, el pixel 1024 representa el valor 10,24
        #try:
        print(number_to_pixel(funcion(q)))
        #except:
            #print('Error en el valor: ' + str(q))
    
text = '4*x'

def funcion_geogebra(x):
    return eval(text)

graficar(funcion_geogebra)