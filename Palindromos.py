#Programa que calcula si un numero es palindromo o no

def palindromo(numero):
    primerNum = numero
    invertido = 0
    if numero >= 1 and numero <= 10000: 
      while numero > 0:
        r = numero % 10  
        invertido = invertido * 10 + r 
        numero = numero // 10  
    
      if primerNum == invertido:
        return True  
      else:
          return False 
    else:
     return False
     

n = 4554
if palindromo(n):
    print(f"El número {n} es un palíndromo.")
else:
    print(f"El número {n} no es un palíndromo.")
    
n = -343
if palindromo(n):
    print(f"El número {n} es un palíndromo.")
else:
    print(f"El número {n} no es un palíndromo.")
