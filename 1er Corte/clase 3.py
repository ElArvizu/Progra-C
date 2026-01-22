
print("ejercicios clase 3")

Cadena_1="hola"#define cadenas
Cadena_2="como estas, espero que mal JAJA" #define cadenas

print(Cadena_1, Cadena_2)# muestra cadenas
print(Cadena_2.upper())#cambia a mayusculas
print(Cadena_1.lower())#cambia a minusculas
print(Cadena_2.capitalize())#1ra letra a mayusculas
print(len(Cadena_1))#longitud de cadena
print(Cadena_1.find("a"))#encuentra a
print(Cadena_2.count("s"))#encuentra s

H=1
J=3
list[Cadena_1,Cadena_2,J,50,H]#creae cadena 
print(list)#muetsra lo que contiene la lista 
print(list[0])#muestra la posicion 0 de la lista 
list.append("1234") #agrega 1234 a la lista 
print(list)#muestra la lista actualizada
list.insert(2,"gato")#agrega gato a la posicion 2 
print(list)#muestra la lista actualizada
list.remove(50)#quita el 50 de la lista 
print(list)#muestra la lista actualizada 

A=10
B=3
X=6
Z=9

if A>B:
    print("A es mayor que B")
else:
    print("A es menos que B")
print ("fin")