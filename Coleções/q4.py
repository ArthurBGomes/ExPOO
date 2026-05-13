import string

frase = input("Digite uma frase: ")

frase = frase.lower()
frase = frase.translate(str.maketrans('', '', string.punctuation))

palavras = frase.split()

palavras_unicas = set(palavras)

frequencia = {}
for palavra in palavras:
    frequencia[palavra] = frequencia.get(palavra, 0) + 1

print("\nPalavras únicas (ordenadas alfabeticamente):")
for palavra in sorted(palavras_unicas):
    print(f"  {palavra}")

print("\nFrequência de cada palavra (ordenadas alfabeticamente):")
for palavra in sorted(frequencia):
    print(f"  {palavra}: {frequencia[palavra]}")