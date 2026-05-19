from livro import Livro
from livrodigital import LivroDigital
from membro import Membro
from biblioteca import Biblioteca
from emprestimo import Emprestimo
from livroerror import LivroNaoEncontradoError


print("\n=== QUESTÃO 1 ===")

livro1 = Livro(
    "Python Orientado a Objetos",
    "Leandro Oliveira",
    "123456"
)

print(livro1.exibir_detalhes())

print("""
Explicação:
- __init__ é o construtor da classe.
- Ele é executado automaticamente ao criar objetos.
- self representa o próprio objeto da classe.
""")


print("\n=== QUESTÃO 2 ===")

biblioteca = Biblioteca("Biblioteca IFRN")

membro1 = Membro(
    "João",
    "Rua A",
    1,
    "joao@email.com",
    "10/05/2026"
)

biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_membro(membro1)

emprestimo = Emprestimo(
    livro1,
    membro1,
    "10/05/2026",
    "17/05/2026"
)

print("Empréstimo criado com sucesso.")

print("""
Explicação:
A relação é de agregação porque Livro e Membro podem existir
independentemente do objeto Emprestimo.
""")


print("\n=== QUESTÃO 3 ===")

print(membro1)

membro1.id_membro = -5

print(membro1)


print("\n=== QUESTÃO 4 ===")

livro_digital = LivroDigital(
    "Python Avançado",
    "Maria Silva",
    "999999",
    "PDF",
    15
)

lista_livros = [livro1, livro_digital]

for livro in lista_livros:
    print(livro.exibir_detalhes())

print("""
Polimorfismo:
O método exibir_detalhes() se comporta de maneira diferente
para Livro e LivroDigital.
""")


print("\n=== QUESTÃO 5 ===")

print("ISBN do livro:", livro1.get_identificador())

print("""
Vantagem da classe abstrata:
Ela garante que todas as subclasses implementem
o método get_identificador().
""")

try:
    livro_encontrado = biblioteca.buscar_livro_por_isbn("000000")
    print(livro_encontrado.exibir_detalhes())

except LivroNaoEncontradoError as erro:
    print("Erro:", erro)


print("\n=== QUESTÃO 6 ===")

membro_buscado = biblioteca.buscar_membro_por_id(1)

print(membro_buscado)

print("""
Vantagem do dicionário:
A busca é muito mais rápida usando a chave id_membro,
sem precisar percorrer toda a coleção.
""")
