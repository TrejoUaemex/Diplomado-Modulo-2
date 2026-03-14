palabra_adivianar="Hola esta es la palabra a adivinar"

def adivinar_palabra(letra_prueba,palabra_intento):
  letra_en_palabra= letra_prueba in palabra_adivianar 
  print(f"¿La letra de prueba se encuentra en la palbra? {letra_en_palabra}") 
  comparacion = palabra_intento == palabra_adivianar 
  comparacion2 =len(palabra_intento) == len(palabra_adivianar)
  resultado_adivinanza= comparacion and comparacion2
  print(f"El jugador gana: {resultado_adivinanza}")
  
  
adivinar_palabra("Hola","Hola esta es la palabra a adivinar")
