import random

def adivinar_numero():
  ran= random.randint(1,50)
  adivinado=False
  intento=0
  
  print("¡Bienvenido a \"adivina el número\"! ¿podrás adivinarlo en pocos intentos?")
  while adivinado != True:
    num = input("Ingrese un numero: ")
    
    if num.isdigit():
      num = int(num)
      intento +=1
      
      if num > ran:
        print(f"El numero es menor que {num}")
      elif num < ran:
        print(f"El numero es mayor que {num}")
      else:
        print(f"¡Felicidades! el numero es {num}, has ganado en {intento} intentos")
        adivinado = True
        
    else:
      print("el valor ingresado no es valido:")

adivinar_numero()