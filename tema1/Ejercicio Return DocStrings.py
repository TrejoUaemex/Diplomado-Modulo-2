def generar_mensaje(nombre, mensaje="Bienvenido al curso de Python"):
    """
    Genera un mensaje personalizado.

    Parametros:
    nombre (str): Nombre de la persona.
    mensaje (str, opcional): Mensaje a mostrar por defecto es "Bienvenido al curso de Python".

    Retorna:
    str: Un mensaje completo combinando el nombre y el mensaje.
    """
    
    return f"¡Hola, {nombre}! {mensaje}"

resultado = generar_mensaje("Jose Luis")
print(resultado) 