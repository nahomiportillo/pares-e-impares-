#Numeros pares e impares
print("---------------------------------")
print("-----Numeros Pares e Impares-----")
print("---------------------------------")
 
r = input('''
    Menu 
    1.Numeros pares 
    2.Numeros impares 
    seleccionar una opcion: ''')            
if r == '1':
       numero = 0
       while numero < 101:
        numero  % 2 == 0
        print(numero)
        numero += 1 
elif r == '2':
    numero = 0
    while numero < 101:
     numero  % 2 != 0
     print(numero)
     numero += 1 



