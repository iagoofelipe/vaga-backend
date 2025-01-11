"""

Solução para teste técnico de desenvolvedor.

Resultado esperado:

1. Soma
O valor da soma é 91

2. Teste Fibonacci
O número 8 pertence a sequência de Fibonacci
O número 9 não pertence a sequência de Fibonacci

3. Faturamento diário
        menor_faturamento: 373.7838
        maior_faturamento: 48924.2448
        dias_acima_media: 10

4. Percentual de faturamento mensal por estado
        SP:     37.53%
        RJ:     20.29%
        MG:     16.17%
        ES:     15.03%
        Outros: 10.98%

5. Invertendo string
o inverso de teste é etset

"""

# ----------------------------------------------------------------
# 1. Soma

indice, soma, k = 13, 0, 0

while k < indice:
    k += 1
    soma += k

print(f"1. Soma\nO valor da soma é {soma}")

# ----------------------------------------------------------------
# 2. Fibonacci
def checkFibonacci(num:int) -> bool:
    n1, n2 = 0, 1

    while n2 < num:
        proximo = n1 + n2
        n1 = n2
        n2 = proximo
    
    result = n2 == num

    if result:
        print(f'O número {num} pertence a sequência de Fibonacci')
    else:
        print(f'O número {num} não pertence a sequência de Fibonacci')

    return result

print('\n2. Teste Fibonacci')
checkFibonacci(8)
checkFibonacci(9)

# ----------------------------------------------------------------
# 3. Faturamento diário
import json
from typing import Iterable

# extraindo dados do arquivo json
with open('dados.json') as file:
    dados = [x['valor'] for x in json.load(file)]

def faturamentoDiario(dados:Iterable[int]) -> dict:
    # removendo zeros, levando em conta que apenas fins de semana possuem faturamento igual a zero
    dados = tuple(filter(lambda x: x != 0, dados))

    menor = dados[0]
    maior = dados[0]
    num_dias = len(dados)

    # menor e maior valor de faturamento
    for val in dados:
        if val < menor:
            menor = val
        
        if val > maior:
            maior = val

    # uma alternativa seria utilizar as funções min() e max() do python
    # menor = min(dados)
    # maior = max(dados)

    # número de dias com faturamento acima da média
    media = sum(dados) / num_dias
    dias_acima_media = len(tuple(filter(lambda x: x > media, dados)))

    return {
        'menor_faturamento': menor,
        'maior_faturamento': maior,
        'dias_acima_media': dias_acima_media
    }


print('\n3. Faturamento diário')
resultado = faturamentoDiario(dados)

for k, v in resultado.items():
    print(f'\t{k}: {v}')

# ----------------------------------------------------------------
# 4. Percentual de faturamento mensal

def percentualFaturamento(dados:dict[str, float]) -> dict[str, float]:
    total = sum(dados.values())
    resultado = {}

    for k, v in dados.items():
        resultado[k] = (v / total) * 100

    return resultado

dados = {
    'SP': 67836.43,
    'RJ': 36678.66,
    'MG': 29229.88,
    'ES': 27165.48,
    'Outros': 19849.53,
}

resultado = percentualFaturamento(dados)

print('\n4. Percentual de faturamento mensal por estado')
for k, v in resultado.items():
    print(f'\t{k}:\t{v:.2f}%')

# ----------------------------------------------------------------
# 5. Invertendo string

def inverteString(string:str) -> str:
    # uma forma muito comum seria utilizar o fatiamento de strings, como string[::-1]

    result = ''
    for i in range(len(string), 0, -1):
        result += string[i-1]

    return result

palavra = 'teste'
print('\n5. Invertendo string')
print(f'o inverso de {palavra} é {inverteString(palavra)}')
