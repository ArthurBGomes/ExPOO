try:   
    print("Abrindo Arquivo...")
    print(1/0)
except ZeroDivisionError as e:
    print('não é permitido dividir por zero')
finally:
    print("Fechando Arquivo...")

