def divisao_segura(a,b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Erro: divisão por zero não é permitida")
        return None
    except TypeError:
        print("Erro: os parâmetros devem ser números")
        return None

print(divisao_segura(10, 2))    # volta 5.0
print(divisao_segura(10, 0))    # Erro: divisão por zero
print(divisao_segura(10, "a"))  # Erro: tipo inválido