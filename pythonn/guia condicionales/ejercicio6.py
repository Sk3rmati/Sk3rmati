import time
for horas in range(24):
    for minutos in range(60):
        for segundos in range(60):
            print (f"{horas:02}:{minutos:02}:{segundos:02}")
            time.sleep(1)    
        