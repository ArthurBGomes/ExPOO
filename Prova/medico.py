from abc import ABC,abstractmethod
class DocumentoSaude(ABC):
    def gerar_relatorio(self):
        pass
class Pessoa:
    def __init__(self,nome,endereco):
        self.nome = nome
        self.endereco= endereco
class Medico(Pessoa):
    def __init__(self,nome,endereco,especialidade,crm):
        super().__init__(nome,endereco)
        self.especialidade = especialidade 
        self.crm = crm 
    def apresentar_medico(self):
        return (
            f"Médico: {self.nome} | "
            f"Endereço: {self.endereco} | "
            f"Especialidade: {self.especialidade} | "
            f"CRM: {self.crm} | "
        )
class MedicoEspecialista(Medico):
    def __init__(self, nome, endereco, especialidade, crm,registro_especialidade):
        super().__init__(nome, endereco, especialidade, crm)
        self.registro_especialiade = registro_especialidade
    def apresentar_medico(self):
        return (
                f"Médico: {self.nome} | "
                f"Endereço: {self.endereco} | "
                f"Especialidade: {self.especialidade} | "
                f"CRM: {self.crm} | "
                f"Registro Especialidade: {self.especialidade} | "
            ) 
class Paciente(Pessoa):
    def __init__(self,nome,endereco,cpf,contato,data_nascimento):
        super().__init__(nome,endereco)
        self.__cpf = cpf
        self.contato = contato
        self.data_nascimento = data_nascimento
    @property
    def cpf(self):
        return self.__cpf
    @cpf.setter
    def cpf(self,cpf):
        if len(cpf) != 11:
            print("CPF inválido")
        else:
            self.__cpf = cpf
    def exibir_informacoes(self):
        return (
            f"Paciente: {self.nome} | "
            f"Endereço: {self.endereco} | "
            f"CPF {self.cpf} | "
            f"Contato: {self.contato} | "
            f"Nascimento: {self.data_nascimento} | "
        )
    def __str__(self):
        return  (
            f"Paciente: {self.nome} | "
            f"CPF {self.cpf} | ")
class PacienteNaoCadrastradoError(Exception):
    pass
class Clinica:
    def __init__(self,nome_unidade):
        self.nome_unidade = nome_unidade 
        self.corpo_clinico = []
        self.lista_pacientes = []
    def adicionar_medico(self,medico):
        self.corpo_clinico.append(medico)
        print("Médico Adicionado")
    def adicionar_paciente(self,paciente):
        self.lista_pacientes.append(paciente)
        print("Paciente adicionado")
    def buscar_paciente_por_cpf(self,cpf):
        for paciente in self.lista_pacientes:
            if paciente.cpf == cpf:
                return paciente
        raise PacienteNaoCadrastradoError('Paciente não encontrado')
class Agendamento(DocumentoSaude):
    def __init__(self,medico,paciente,data_hora):
        self.medico = medico 
        self.paciente = paciente 
        self.data_hora:str = data_hora
        # é Agregação,pois os objetos são criados fora da classe e sua existência não depende da classe Agendamento,são passados como parâmetros na instanciação
    def gerar_relatorio(self):
        return f'Consulta Com doutor(a) {self.medico.nome} marcada para o(a) paciente {self.paciente.nome} na data/hora ás {self.data_hora}'
    
m1 = Medico("Esther","Brasilia","Psicologa","120101")
me1 = MedicoEspecialista("Esther","Brasilia","Psicologa","120101","Psicologa")
lista_medicos = [m1,me1]
for medico in lista_medicos:
    print(medico.apresentar_medico())
p1 = Paciente("Vitória","São Geraldo","122389123-43","9415-9642","07/09/09")


print(p1)
print(p1.exibir_informacoes())
print(m1.apresentar_medico())
c1 = Clinica("Clínica dos Britos")
c1.adicionar_medico(m1)
c1.adicionar_paciente(p1)
a1 =  Agendamento(m1,p1,"11H 19/05")
print(a1.gerar_relatorio())
try:
    print(c1.buscar_paciente_por_cpf("122389123-43"))
except PacienteNaoCadrastradoError as error:
    print(f"Erro: {error}")




    