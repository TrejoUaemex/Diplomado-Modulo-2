def contadar_caracteres(arg1):
    
    """Esta funcion cuenta el numero de careteres de la frase ingresada
    
    keyword arguments:
    
    arg1 --- primer agumento de la función ('Arg Tipo String')
    """
    
    print(f"La frase {arg1} tiene {len(arg1)} caracteres") #Imprime la frase y realiza el conteno de caracteres
     
def Convertir_numeros(int):
    """Esta funcion realiza la conversion de un Int a String y Float
    
    keyword arguments:
    
    arg1 --- primer agumento de la función ('Arg Tipo INT')
    """
    
    String=str(int) #Almacena en la variable String la conversión del Entero a cadena
    Float=float(int)  #Almacena en la variable String la conversión del Entero a flotante
  
    print(f"Entero:{int},Tipo:{type(int)}") 
    print(f"Cadena:{String},Tipo:{type(String)} ")
    print(f"Flotante:{Float},Tipo:{type(float)} ")

      
     
contadar_caracteres("Esto es una prueba")
Convertir_numeros(2)
          