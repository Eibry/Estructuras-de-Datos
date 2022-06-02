def alumnos():
    nombres = []
    apellidos = []
    alumnos = []
    num_alumnos = int(input("¿Cuántos alumnos son en total? "))
    for i in range(num_alumnos):
        nombre = input(f'Nombre del alumno no. {i + 1} ')
        apellido = input(f'Apellido del alumno no. {i + 1} ')
        nombres.append(nombre)
        apellidos.append(apellido)
    alumnos = [nombres, apellidos]
    return alumnos
    
if __name__ == '__main__':
    nombres, apellidos = alumnos()
    for i in range(len(nombres)):
        print(f'{i + 1}.- {nombres[i]} {apellidos[i]} ')  