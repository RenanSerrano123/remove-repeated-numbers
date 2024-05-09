def imprimir_primeira_ocorrencia(vetor):
    ocorrencias = set()
    resultado = []
    for num in vetor:
        if num not in ocorrencias:
            ocorrencias.add(num)
            resultado.append(num)
    return resultado
def main():
    n = int(input())
    vetor = list(map(int, input().split()))
    resultado = imprimir_primeira_ocorrencia(vetor)
    for num in resultado:
        print(num, end=" ")
main()