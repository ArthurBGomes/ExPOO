frase = input("Digite uma frase: ")

frase = frase.lower()

for p in ".,!?":
    frase = frase.replace(p, "")

palavras = frase.split()

unicas = set(palavras)

frequencia = {}

for palavra in palavras:
    if palavra in frequencia:
        frequencia[palavra] += 1
    else:
        frequencia[palavra] = 1

print("\nPalavras únicas:")
for palavra in sorted(unicas):
    print(palavra)

print("\nFrequência das palavras:")
for palavra in sorted(frequencia):
    print(f"{palavra}: {frequencia[palavra]}")