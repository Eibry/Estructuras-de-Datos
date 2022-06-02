estudiantes = {}

def run():
    alumnos = int(input("¿Cuántos alumnos hay en la clase? "))
    for alumno in range(alumnos):
        nombre = input(f'¿Cómo se llama el {alumno+1}º alumno? ')
        estudiantes[nombre] = None
    
    for key in estudiantes.keys():
        clases = int(input(f'¿Cuántas materias tiene {key}? '))
        materias = {}
        for clase in range(clases):
            materia = input(f'Nombre de la {clase+1}ª materia: ')
            calificacion = int(input(f'Calificación en {materia}: '))
            materias[materia] = calificacion
        
        estudiantes[key] = dict(materias)
        
    print(estudiantes)

if __name__ == '__main__':
    run()