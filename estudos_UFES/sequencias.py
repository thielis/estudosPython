def encontrar_sequencia(sequencia):
    """Encontra a primeira sequência de 3 ou mais caracteres iguais consecutivos.

    Args:
        sequencia: Uma string contendo apenas 0s e 1s.

    Returns:
        O índice do início da primeira sequência encontrada, ou -1 se não houver.
    """
    posicao = 0
    for i in range(2, len(sequencia)):
        if sequencia[i] == sequencia[i-1] == sequencia[i-2]:
            posicao = i - 2  # Retorna o índice do início da sequência
            break
        else:
            posicao = -1
        
    if posicao >= 0:
        print(f"Existe uma seqência de {sequencia[posicao]}'s, na posicao {posicao}.")
    else:
        print("Não existe!")

print("Verificando a existência uma sequência de 3 ou mais 0’s ou 1’s consecutivos")
# Testando a função com as sequências fornecidas
sequenciaA = "1100101010001011100"
sequenciaB = "0100111001001101000"
sequenciaC = "0110011001001101001"

encontrar_sequencia(sequenciaA)
encontrar_sequencia(sequenciaB)
encontrar_sequencia(sequenciaC)