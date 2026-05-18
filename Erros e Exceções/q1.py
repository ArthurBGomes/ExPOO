def adicionar_valor(inicial:int,adicional:int):
    if adicional <= 0:
        raise ValueError("Somente valores positivos devem ser adicionados ao valor inicial")
    return inicial + adicional
try:
    a = adicionar_valor(10,12)
    print(f" o Resultado da Soma é {a}")

except ValueError as e:
    print(f"Erro: {e}")
try:
    a = adicionar_valor(10,-12)
    print(a)  
except ValueError as e:
    print(f"Erro: {e}")

