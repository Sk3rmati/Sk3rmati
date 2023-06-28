import random

rand_list = []

for i in range (0, 20):
    random_num = random.randint(40, 350)
    rand_list.append(random_num)
print(rand_list)

while True:
    try:
        num_user = int(input("Digite un numero entre 40 y 350:\n "))
        if num_user >= 40 and num_user <= 350:
            break
        print("Digite un valor igual o mayor a 40")
        continue
    except ValueError:
        print("Digite un numero valido")

if num_user not in rand_list:
    print("\nEl numero no se encuentra en la lista")
else:
    oc = rand_list.count(num_user)
    print("\nEl número se encuentra en la lista")
    print("El número aparece:", oc)

