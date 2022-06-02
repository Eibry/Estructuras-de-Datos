def asignaturas():
    materias = []
    num_materias = int(input("¿Cuántas materias tienes? "))
    for i in range(num_materias):
        materia = input(f'Materia no. {i + 1} ')
        materias.append(materia)
    return materias
    
if __name__ == '__main__':
    materias = asignaturas()
    contador = 0
    for materia in materias:
        contador += 1
        print(f'{contador}.- {materia} ')