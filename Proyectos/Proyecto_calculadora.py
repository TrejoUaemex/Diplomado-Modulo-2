#probado
def calcular_imc(peso_kg, altura_m): 
    """ 
    Calcula el Índice de Masa Corporal (IMC). 
    Fórmula: IMC = peso / (altura^2) 
    """ 
    imc = peso_kg / (altura_m ** 2) 
    return imc
    
def es_peso_saludable(imc): 
    """ 
    Determina si el IMC está en rango saludable (18.5 - 24.9). 
    """ 
    return imc >= 18.5 and imc <= 24.9

def tiene_bajo_peso(imc): 
    """ 
    Determina si hay bajo peso (IMC < 18.5). 
    """ 
    return imc < 18.5
    
def tiene_sobrepeso(imc): 
    """ 
    Determina si hay sobrepeso (IMC >= 25). 
    """ 
    return imc >= 25 

def calcular_calorias_diarias(peso_kg, altura_cm, edad, es_hombre):
    """
    Calcula las calorías diarias recomendadas usando Fórmula de Harris-Benedict.
    """
    edad = int(edad)

    calorias_hombre = 88.362 + (13.397 * peso_kg) + (4.799 * altura_cm) - (5.677 * edad)
    calorias_mujer = 447.593 + (9.247 * peso_kg) + (3.098 * altura_cm) - (4.330 * edad)

    return es_hombre * calorias_hombre + (1 - es_hombre) * calorias_mujer

def calcular_agua_diaria(peso_kg): 
    """ 
    Calcula litros de agua recomendados al día (35ml por kg de peso). 
    """ 
    return peso_kg * 0.035


def calcular_ritmo_cardiaco_maximo(edad): 
    """ 
    Calcula el ritmo cardíaco máximo (220 - edad). 
    """ 
    return 220 - int(edad)

def datos_personales(nombre,peso_kg,altura_m,edad,genero):
    print("========================================================")    
    print(f"REPORTE DE FITNESS Y SALUD - {nombre}")    
    print("========================================================\n")    

    print(f"Peso: {peso_kg} kg")
    print(f"Altura: {altura_m} m")
    print(f"Edad: {edad} años")

    es_hombre = genero == "H"
    print(f"¿Hombre?: {es_hombre}")


nombre = input("¿Cual es tu nombre?: ")
peso_kg = input("¿Cuanto pesas? (Kg): ")
altura_m = input("¿Cuanto mides? (metros): ")
edad = input("¿Cuantos años tienes?: ")
genero = input("¿Eres hombre o mujer? (H/M): ")
datos_personales(nombre,peso_kg,altura_m,edad,genero)

# Conversiones
conversion_peso = float(peso_kg)
conversion_altura = float(altura_m)
altura_cm = conversion_altura * 100
es_hombre = genero == "H"


imc = calcular_imc(conversion_peso,conversion_altura)

print("\nIndice de Masa Corporal (IMC):")
print("Tu IMC:", imc)
print("¿Peso saludable?", es_peso_saludable(imc))
print("¿Sobrepeso?", tiene_sobrepeso(imc))
print("¿Bajo peso?", tiene_bajo_peso(imc))

print("\nNutricion:")
print("Calorias diarias recomendadas:", calcular_calorias_diarias(conversion_peso,altura_cm,edad,es_hombre))
print("Agua diaria recomendada:", calcular_agua_diaria(conversion_peso), "litros")

print("\nSalud Cardiaca:")
print("Ritmo cardiaco maximo:", calcular_ritmo_cardiaco_maximo(edad))