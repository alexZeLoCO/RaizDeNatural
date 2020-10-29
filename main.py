n = int(input("Introduzca un número entero: "))     #SOLICITA VALOR
valor = 0       #VARIABLE CENTINELA
i=0     #PARTE ENTERA RAÍZ

while valor<=n:     #MIENTRAS CENTINELA SEA MENOR QUE VALOR
    i = i + 1       #AUMENTAR I EN 1
    valor = i**2        #CALCULAR CUADRADO DE I

i=i-1       #I EXCEDE EN 1 (DIO UNA VUELTA DE MÁS EN EL WHILE)

            #OUTPUT
print ("La parte entera de la raíz cuadrada del valor introducido es:",i)