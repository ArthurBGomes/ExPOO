from abc import ABC, abstractmethod

class PessoaHospital(ABC):

    @abstractmethod
    def get_identificacao(self):
        pass

class Paciente(PessoaHospital):
    def __init__(self, nome, cpf, idade):
        self.nome = nome
        self.cpf = cpf
        self.__idade = None
        self.idade = idade

    @property
    def idade(self):
        return self.__idade
    
    @idade.setter
    def idade(self, idade):
        if idade < 0:
            print('Erro: a idade não pode ser negativa\n-----------------------------')
        else:
            self.__idade = idade

    def exibir_dados(self):
        return f'Nome: {self.nome}\nCPF: {self.cpf}\nIdade: {self.idade}\n-----------------------------'
    
    def get_identificacao(self):
        return f'IDENTIFICAÇÃO PELO CPF: {self.cpf}\n-----------------------------'
    
class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario = salario

class Medico(Funcionario):
    def __init__(self, nome, salario, crm, especialidade, plantao):
        super().__init__(nome, salario)
        self.crm = crm
        self.especialidade = especialidade
        self.plantao = plantao

    def __str__(self):
        return f'Nome: {self.nome}\nSalário: {self.salario}\nCRM: {self.crm}\nEpecialidade: {self.especialidade}\nPlantão: {self.plantao}\n-----------------------------'
    
class MedicoCirurgiao(Medico):
    def __init__(self, nome, salario, crm, especialidade, plantao, tipo_cirurgia):
        super().__init__(nome, salario, crm, especialidade, plantao)
        self.tipo_cirurgia = tipo_cirurgia
    
    def __str__(self):
        return f'Nome: {self.nome}\nSalário: {self.salario}\nCRM: {self.crm}\nEpecialidade: {self.especialidade}\nPlantão: {self.plantao}\nTipo Cirurgia: {self.tipo_cirurgia}\n-----------------------------'

# 1- b) o método __init___ é o método construtor da classe, aquele que é chamado assim que a instancio, sendo como a base do meu objeto. O parâmetro self se refere à instância atual da minha classe 

class PacienteNaoEncontradoError(Exception):
    pass

class Clinica:
    def __init__(self, nome_clinica):
        self.nome_clinica = nome_clinica
        self.dicionario_pacientes = {}
        self.lista_medicos = []

    def adicionar_paciente(self, paciente):
        self.dicionario_pacientes[paciente.cpf] = paciente

    def adicionar_medico(self, medico):
        self.lista_medicos.append(medico)

    def buscar_paciente_por_cpf(self, cpf):
        if cpf in self.dicionario_pacientes:
            return self.dicionario_pacientes[cpf]
        else:
            raise PacienteNaoEncontradoError(
                'Paciente nao encontrado'
            )
        
class Consulta:
    def __init__(self, paciente, medico, data_consulta, horario):
        self.paciente = paciente
        self.medico = medico
        self.data_consulta = data_consulta
        self.horario = horario

# 2- b) Esse é um exemplo de agração porque usamos objetos criados a partir de outra classe para instanciar a classe consulta

p1 = Paciente('Esther', 383877229, 16)
print(p1.exibir_dados())
p2 = Paciente('Helia', 393948488, 17)
p2.idade = -17
print(p2.exibir_dados())
print(p1.get_identificacao())

m1 = Medico('Maria', 5000, 838839293, 'clinica geral', 'TER/QUI')
m2 = Medico('Rafaela',7000, 9838378293, 'Pediatria', 'SEG/QUA')
ms1 = MedicoCirurgiao('Gabriela', 6000, 49494848, 'neurologia', 'DOM', 'Cerebral')

clinica1 = Clinica('Medfisio')
clinica1.adicionar_paciente(p1)
clinica1.adicionar_paciente(p2)
clinica1.adicionar_medico(m1)
clinica1.adicionar_medico(m2)
clinica1.adicionar_medico(ms1)

lista_medicos = [m1, m2, ms1]
for medico in lista_medicos:
    print(medico)

try:
    paciente = clinica1.buscar_paciente_por_cpf(383877229)
    print(paciente.exibir_dados())

except PacienteNaoEncontradoError as erro:
    print(erro)