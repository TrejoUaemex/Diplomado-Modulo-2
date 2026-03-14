def comparar_longitud (palabra1,palabra2):
    longitud1=len(palabra1)
    longitud2=len(palabra2)
    return longitud1==longitud2
 
Palabra1="Perro"
Palabra2="Gato22"

compara= comparar_longitud(Palabra1,Palabra2)
print(f"¿Son {Palabra1} y {Palabra2} dos palabras con las mism logitud?:{compara}")