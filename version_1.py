def imprimir ():
    print ("Buenos dias.Ingrese con el respectivo numero de la lista cuales son los sintomas que padece")
    print(" 1-Dolor de cabeza \n 2-Malestar \n 3-Mucosa \n 4-Fiebre \n 5-Dolor de garganta \n 6-Tos" )
    print("Ingrese 0 si no padece ningun sintoma o termino de digitarlos")
gripe=[1,3]
faringitis=[4,6]

num_gripe=0
num_faringitis=0
imprimir()
var=0
var=int(input())


while var != 0:
   if var <= gripe[1]:
       num_gripe += 1
   if var >= faringitis[0] and var <= faringitis[1]:
       num_faringitis += 1
#    imprimir()
   var=int(input())




if num_gripe == num_faringitis:
    print ("Lo sentimos pero no podemos diagnosticar su caso, porfavor consulte con un medico")
if num_gripe < num_faringitis:
    print ("Lamento informarle que tiene faringitis")
if num_gripe > num_faringitis:
    print ("Lamento informarle que tiene gripe")
