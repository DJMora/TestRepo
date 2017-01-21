#name = input("Nombre ")
#for letter in name:
    #if letter is 'u':
    #print("letter ",letter)
        #continue

from random import randint

equipos = ["Saprissa","Alajuela","Heredia","Cartago"]

def add(num1,num2):
    print("La suma de los 2 numeros = ",int(num1)+int(num2))

def substract(num1,num2):
    print("{num1} - {num2} = ",num1-num2)

def menu(userOption):
    if userOption == "1":
        add(num1,num2)
    elif userOption == "2":
        substract(num1,num2)

def crearPartido(listParam):
    equipo1 = equipos[randint(0,3)]
    equipo2 = equipos[randint(0,3)]

    if equipo1 is equipo2:
        equipo2 = "Belen"
    print(f"Partido Creado: {equipo1} vs {equipo2}")
    

def main():
    global num1,num2
    num1 = input("Digite el primer numero  ")
    num2 = input("Digite el segundo numero ")

    userOption = input("Que deasea hacer con estos numeros? (1 para sumar / 2 para restar) ")
    menu(userOption)

if __name__ == "__main__":
    main()
