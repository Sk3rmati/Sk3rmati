trabajadores = [
    ["Juan",[700000,650000,690000]], 
    ["María",[681000,710000,590000]], 
    ["Pedro",[590000,635000,705000]]
                ]

def prom(trabajadores):
    prom_juann  = sum(trabajadores[0][1]) / len(trabajadores[0][1])
    prom_maria = sum(trabajadores[1][1]) /len(trabajadores[1][1])
    prom_pedro = sum(trabajadores[2][1]) / len(trabajadores[2][1])
    
    print(("El promedio de Juan es:",round(prom_juann,2)))
    print("\nEl promedio de María es:\n",round(prom_maria,2))
    print("\nEl promedio de Pedro es:",round(prom_pedro,2))

def sueldo(trabajadores):
    sueldo_juann  = max(trabajadores[0][1])
    sueldo_maria = max(trabajadores[1][1])
    sueldo_pedro = max(trabajadores[2][1])
    
    print("\nEl sueldo más alto de Juan es:\n", sueldo_juann)
    print("\nEl sueldo más alto de Maria es:\n", sueldo_maria)
    print("\nEl sueldo más alto de Pedro es:\n", sueldo_pedro)



def retencion_imp(trabajadores):
    todo_juann  = sum(trabajadores[0][1])
    todo_maria = sum(trabajadores[1][1])
    todo_pedro = sum(trabajadores[2][1])
    
    imp_juann  = todo_juann * 0.1225
    imp_maria = todo_maria * 0.1225
    imp_pedro = todo_pedro * 0.1225
    
    retencion_imp = (imp_juann, imp_maria, imp_pedro)
    mayor_imp = max(retencion_imp)
    
    print("\nLa retención de impuestos de Juan es de:\n",imp_juann)
    print("\nLa retención de impuestos de Maria es de:\n",imp_maria)   
    print("\nLa retención de impuestos de Pedro es de:\n",imp_pedro) 
    print("\nEl mayor impuesto retenido es de:\n",mayor_imp) 


prom(trabajadores)

sueldo(trabajadores)

retencion_imp(trabajadores)