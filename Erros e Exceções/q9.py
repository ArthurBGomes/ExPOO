class SenhaCurtaError(Exception):
    pass
def cadrastar_senha(senha):
        try:
            if len(senha) < 8:
                raise SenhaCurtaError(' Mínimo de 8 Caracteres')
            print("Senha Cadastrada")
        except SenhaCurtaError as e:
            print(f'Erro: {e}')

cadrastar_senha('12345678')


cadrastar_senha('1234567')

