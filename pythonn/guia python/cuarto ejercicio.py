n1 = input("Digite la primera palabra: \n")
n2 = input("Digite el segundo palabra: \n")

if n1[0] == n2[0] and n1[-1] == n2[-1]:
 print("Ambos palabras comienzan y terminan con la misma letra")
else:
   if n1[0] == n2[0] and n1[-1] != n2[-1]:
      print("Ambas palabras comienzan con la misma letra")
   else:
      if n1[-1] == n2[-1] and n1[0] != n2[0]:
         print("Ambas palabras terminan con la misma letra")