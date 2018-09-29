Matriz = [8.5, 9.5, 10, 6.5, 8.0]
Importancia = [0.65, 0.5,0.2,0.55]

def compara_matriz(m,i):
    matriz = [0]*len(i)
    for a in range(0, len(i)):
        if (i[a] >= 0.5):
            matriz[a] = m[a]
        # else:
        #     matriz[a] = 0
    return matriz

print(compara_matriz(Matriz,Importancia))