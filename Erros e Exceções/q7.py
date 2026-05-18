def verificar_nota(nota):
    if nota < 0 or nota > 10:
        raise ValueError('Nota inválida: deve estar entre 0 e 10')
    return nota
try:
    verificar_nota(8)
    print("Nota válida!")
except ValueError as e:
    print(f"Erro: {e}")

try:
    verificar_nota(11)
except ValueError as e:
    print(f"Erro: {e}")