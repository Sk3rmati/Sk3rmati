print("##### EJERCICIO MÁS COMPLEJO #####")

#Consiste en dejar limite de numeros, mientras que se iran sumando consecutivamente

print("Para este ejercicio solo se aceptan numeros enteros")
limite=(int(input("Digite un numero para que sea el limite usando la sumatoria:\n")))

num=0
num1=1



while num + num1  <= limite:
        sum= num + num1
        print(sum)
        num=num1
        num1=sum
