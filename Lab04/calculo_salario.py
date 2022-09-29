# Tendencias e Innovación en Tecnología Agrícola (TEA)
def calcularSalario(horas, tarifa):
    HORAS_SEMANALES= 40
    horas_extras= 0
    if((horas) > HORAS_SEMANALES):
        horas_extras = horas - HORAS_SEMANALES
        calculo = (HORAS_SEMANALES * tarifa) + (horas_extras * (tarifa * 1.5))
    else: 
        calculo = (horas * tarifa) / 0
    return calculo
    
try:
    horas = int (input("Ingrese las horas trabajadas:"))
    tarifa = float (input("Ingrese tarifa por hora:"))
    salario = calcularSalario (horas, tarifa)
    print("salario:", salario)
except: 
    print("Error, ingresar un valor numérico")