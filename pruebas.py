LARGO = 10

def graficar(funcion):
    
    for i in range(LARGO):
        q = i #Valor con el que se va a graficar, el pixel 1024 representa el valor 10,24
        #try:
        print(funcion(q))
        #except:
            #print('Error en el valor: ' + str(q))
    
text = '4*x'

def funcion_geogebra(x):
    return round(eval(text))

graficar(funcion_geogebra)