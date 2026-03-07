def cabecera():
    """Muestra la cabecera de la aplicación
    """
    titulo=r"""
                                                             ___                                    
                                                        (   )                                   
  .--.     .---.   ___ .-. .-.     .--.    ___ .-.       | |_       .---.    .--.       .--.    
 /    \   / .-, \ (   )   '   \   /    \  (   )   \     (   __)    / .-, \  /    \    /  _  \   
;  ,-. ' (__) ; |  |  .-.  .-. ; |  .-. ;  | ' .-. ;     | |      (__) ; | ;  ,-. '  . .' `. ;  
| |  | |   .'`  |  | |  | |  | | |  | | |  |  / (___)    | | ___    .'`  | | |  | |  | '   | |  
| |  | |  / .'| |  | |  | |  | | |  |/  |  | |           | |(   )  / .'| | | |  | |  _\_`.(___) 
| |  | | | /  | |  | |  | |  | | |  ' _.'  | |           | | | |  | /  | | | |  | | (   ). '.   
| '  | | ; |  ; |  | |  | |  | | |  .'.-.  | |           | ' | |  ; |  ; | | '  | |  | |  `\ |  
'  `-' | ' `-'  |  | |  | |  | | '  `-' /  | |           ' `-' ;  ' `-'  | '  `-' |  ; '._,' '  
 `.__. | `.__.'_. (___)(___)(___) `.__.'  (___)           `.__.   `.__.'_.  `.__. |   '.___.'   
 ( `-' ;                                                                    ( `-' ;             
  `.__.                                                                      `.__.              
                                🕹️¡Crea tu identidad gamer!🎮 
    """
    print(titulo) 


def tag_basico(nombre):
    """
    Crea un GamerTag basico utilzando las primeras 4 letras del nombre
    
    parametros:
    nombre(str): Ingrese el nombre del usuario
    
    retorna:
    Str: GamerTag Basico
    """
    tag=nombre[0:4]
    return tag

#cabecera()
#print(tag_basico("Jose Luis Trejo Monroy"))
    
def tag_invertido(nombre):
    """
        Crear un gamertag invirtiendo el nombre completo. 
        Parámetro: 
        nombre (str): El nombre del usuario 
        Retorna: 
        str: Nombre invertido 
    """
    tag_inv=nombre[::-1]
    return tag_inv

def tag_intercalado(nombre, apellido):
    """
        Crea un gamertag combinando letras del nombre y apellido. 
        Ejemplo: nombre="Juan", apellido="Perez" → "JPuanerez" 
        Parámetros: 
        nombre (str): El nombre del usuario 
        apellido (str): El apellido del usuario 
        Retorna: 
        None (imprime directamente) 
    """
    letra1nombre = nombre[0]
    completanombre = nombre[1:]
    letra1prime = apellido[0]
    completapellido = apellido[1:]

    print("3.TAG INTERCALADO:",letra1nombre, letra1prime, completanombre, completapellido, sep="")

#tag_intercalado("Jose","Trejo")

def tag_elite(nombre):
    """
        Crea un gamertag "elite" usando inicio y final del nombre. 
        Ejemplo: "Santiago" → "Sago" 
        Parámetro: 
        nombre (str): El nombre del usuario 
        Retorna: 
        None (imprime directamente) 
    """
    dosprimerasletrasnombre=nombre[:2]
    dosultimasletrasnombre=nombre[-2:]
    print("4.TAG ELITE:",dosprimerasletrasnombre, dosultimasletrasnombre, sep="")
        
#tag_elite("Jose Luis")

def tag_numero(nombre,numero):
    """
        Crea un gamertag añadiendo número al final. 
        Parámetros:
        nombre (str): El nombre del usuario 
        numero_favorito (int): Número favorito del usuario 
        Retorna: 
        None (imprime directamente) 
    """
    letrasnombre=nombre[:5]
    print("5.TAG CON NUMERO:",letrasnombre,numero,sep="")

#tag_numero("Jose",2)

def mostrar_estadisticas(nombre):
    """
    Muestra estadisticas del nombre proporcionada.
    Paramtro:
    nombre (str): El nombre a analizar
    
    Retorna:
    None(IMprime directamente)
    """
    longitud=len(nombre)
    print("\nEstadisticas De Tu Nombre")
    print("Nombre completo:",(nombre))
    print("Longitud del nombre",longitud)
    print("Primera Letra:",nombre[0])
    print("Ultima Letra:", nombre[-1])
    
def generar_todas_las_opciones(nombre,apellido,numero):
    """
    Genera y muestra todas las opciones de gamerstags
    
    Parametros:
    nombre (str): Nombre del usuario
    apellido (str): Apellido del usuario
    numero (str): Numero favorito del usuario
    
    Retorna:
    Nano (Imprime directamente)
    """
    print("\n =========================")
    print("TUS OPCIONES DE GAMERTAG:")
    print("===========================")
    
    tag_basico2=tag_basico(nombre)
    print("\n1.TAG BASICO:",tag_basico2)
    print("2.TAG INVERTIDO:",tag_invertido(nombre))
    tag_intercalado(nombre,apellido)
    tag_elite(nombre)
    tag_numero(nombre,numero)
    
print("======================================")
#===========================================
#APP PRINCIPAL
#===========================================
#llama a la funcion cabecera
cabecera()
#Solicitar datos al usuario
nombre =input("\n Introduce tu nombre: ")
apellido= input("\n Introduce tu apellido:")
numero=input("\n Introduce tu número favorio:")
#mostrar estadisticas del nombre
mostrar_estadisticas(nombre)
generar_todas_las_opciones(nombre,apellido,numero)


print("\n ¡Elige tu favorito y conquista el mundo gamer!\n")