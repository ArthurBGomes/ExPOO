contagem = {}
while True:
    entrada = input("Diga o ano:").strip()
    if entrada == "":
        break
    ano = int(entrada)
    contagem[ano] = contagem.get(ano, 0) + 1
print("\n" + "=" * 40)
print(f"{'RELATÓRIO DE NASCIMENTOS':^40}")
print("=" * 40)
 
if not contagem:
    print("Nenhum dado informado.")
else:
    print(f"{'Ano':<15} {'Pessoas':>10}")
    print("-" * 40)
    for ano in sorted(contagem):
        print(f"{ano:<15} {contagem[ano]:>10}")
    print("-" * 40)
    print(f"{'Total':<15} {sum(contagem.values()):>10}")
 
print("=" * 40)