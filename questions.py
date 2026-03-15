#ESTE ES MI GRAN PROGRAMA

import random
categorias = {
    "programacion" :["python","programa","variable","funcion","bucle","cadena","entero","lista",],
    "paises" :[ "argentina","canada","mexico","guatemala","chile","china","uruguay"],
    "colores" :["rojo","amarillo","azul","verde","blanco","negro","marron","dorado","rosa","celeste"]
}
    
print("¡Bienvenido al Ahorcado!")
print()
#le imprimimo las categorias para que el jugador las sepa
print ("Estas son tus CATEGORIAS DISPONIBLES")
for cat in categorias.keys():
    print(f"- {cat}")
print()
#validacion para que elija una categoria valida
categoria_elegida = ""
while categoria_elegida not in categorias:
    categoria_elegida= input("Elegí una categoria: ").lower()
    if categoria_elegida not in categorias:
        print("Esa no es una categoría valida. Intenta de nuevo")

# Elegimos y mezclamos todas las palabras de la categoría seleccionada sin repetir
palabras_mezcladas = random.sample(categorias[categoria_elegida], len(categorias[categoria_elegida]))

print("------------Comienza el juego------------")

for word in palabras_mezcladas:
    guessed=[]
    attempts=6

    print("--- NUEVA RONDA ---")
    
    while attempts > 0:
        # Mostrar progreso: letras adivinadas y guiones para las que faltan
        progress = ""
        for letter in word:
            if letter in guessed:
                progress += letter + " "
            else:
                progress += "_ "
        print(progress)
        # Verificar si el jugador ya adivinó la palabra completa
        if "_" not in progress:
            print("¡Ganaste!")
            break
        print(f"Intentos restantes: {attempts}")
        print(f"Letras usadas: {', '.join(guessed)}")
        #Solicito y valido  lo ingresado y fuerzo a que sea minúscula
        letter = input("Ingresá una letra: ").lower()
        if len(letter)!=1 or not letter.isalpha():
           print("Entrada no válida") 
           print()
        else:
            if letter in guessed:
                print("Ya usaste esa letra.")
            elif letter in word:
                guessed.append(letter)
                print("¡Bien! Esa letra está en la palabra.")
            else:
                guessed.append(letter)
                attempts -= 1
                print("Esa letra no está en la palabra.")
                print()
    else:
        print(f"¡Perdiste! La palabra era: {word}")
    
    print(f"Tu puntuación final es {attempts}")
    if attempts != 0:
       print("Bien jugado.")
    else: 
        print("¡Toca mejorar! Mejor suerte la próxima.")
        
    seguir = input("¿Querés jugar otra ronda? (s/n): ").lower()
    if seguir != 's':
        break
else:
    print("¡Se agotaron las palabras de esta categoría!")