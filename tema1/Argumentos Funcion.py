def orginizar_fiesta(x,tema="Pyhton",lugar="Aula informativa"):
    print(f"Preparando una fiesta para {x} invitados")
    print(f"Tema de la fiesta:{tema}")
    print(f"Lugar de la celebración: {lugar}")

#llamar a funcion unicamente con argumento para invitados
orginizar_fiesta(3)
print("\n")
#llamar a funcion unicamente proporcionando solo el número de invitados y el tema de la fiesta
orginizar_fiesta(4,"Java")
print("\n")
#llamar a funcion unicamente proporcionando todos los argumentos.
orginizar_fiesta(6,"C++","Laboratorio Redes") 