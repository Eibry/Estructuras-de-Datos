materias = ('Programación Orientada a Objetos', 'Ingeniería de Software APC', 'Estructuras de Datos', 'Calculo Diferencial', 'Procesos de Desarrollo De Software', 'Desarrollo Humano y Valores', 'Ingles')

def run():
    print("Escribe las calificaciones de las siguientes materias")
    calificaciones = ()
    for materia in materias:
        calificacion = int(input(f'{materia}: '))
        calificaciones += (calificacion,)
    return calificaciones

def prom(calificacion):
    promedio = 0
    suma = 0
    for i in calificacion:
        suma += i
        promedio = suma / len(calificacion)
    return promedio
    

if __name__ == '__main__':
    calificaciones = run()
    promedio = prom(calificaciones)
    
print(f'El promedio final es: {round(promedio, 1)} ')