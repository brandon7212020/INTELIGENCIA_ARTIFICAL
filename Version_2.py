print ("Buenos dias.Ingrese con el respectivo numero de la lista cuales son los sintomas que padece")
print(" 1-Fiebre \n 2-Malestar \n 3-Dolor de garganta" )
print("Ingrese 0 si no padece ningun sintoma o termino de digitarlos")
gripe=[1,2]
faringitis=[2,3]

porcentaje_gripe=[0.2, 0.7]
porcentaje_faringitis=[0.6, 0.8]
num_gripe=0
num_faringitis=0
resultado_gripe=0
resultado_faringitis=0
var=0
var=int(input())


while var != 0:
   if var <= gripe[1]:
      if resultado_gripe != 0:
          resultado_gripe= resultado_gripe + (1 - resultado_gripe) * porcentaje_gripe[var-1]
      if resultado_gripe == 0:
          resultado_gripe= porcentaje_gripe[var-1]
       

   if var >= faringitis[0] and var <= faringitis[1]:
       if resultado_faringitis == 0:
          resultado_faringitis= porcentaje_faringitis[var-2]
       if resultado_gripe != 0:
          resultado_faringitis= resultado_gripe + (1 - resultado_gripe) * porcentaje_gripe[var-2]
   var=int(input())


if resultado_faringitis == resultado_gripe:
    print ("Lo sentimos pero no podemos diagnosticar su caso, porfavor consulte con un medico")
if resultado_faringitis > resultado_gripe:
    print ("Lamento informarle que tiene faringitis", resultado_faringitis)
if resultado_faringitis < resultado_gripe:
    print ("Lamento informarle que tiene gripe con un porcentaje de probabilidad de ",resultado_gripe )

