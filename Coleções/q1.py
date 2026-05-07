import random
print("=== Lotérica dos Britos ===")
sorteio = random.sample(range(1,41),25)
sorteio.sort()
print(f" os números sorteados são: \n{sorteio}")