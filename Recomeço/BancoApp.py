import tkinter as tk
from tkinter import messagebox, simpledialog
from ContaBancaria import ContaBancaria
from cliente import Cliente
from endereco import Endereco
from ContaPoupanca import ContaPoupanca
from ContaCorrente import ContaCorrente
from ContaSalario import ContaSalario


cliente2 = Cliente("Giovanna","984.654.321","Rua 2",123,"Bairro 2","Cidade 1")
cliente1 = Cliente("Arthur","123.456.789","Rua 1",196,"Bairro 2","Cidade 1")
cliente3 = Cliente("George","987.654.321","Rua 2",123,"Bairro 2","Cidade 1")


class BancoApp:
    def __init__(self, janela):
        self.janela = janela
        self.janela.title("Sistema Bancário - POO em Python")
        self.janela.geometry("950x500")

        self.contas = [
            ContaCorrente(cliente1, 1004, 200,1000,100),
            ContaPoupanca(cliente2, 1003, 20,0.1),
            ContaBancaria(cliente2, 1005, 20),
            ContaSalario(cliente3, 1006, 2000,"SENAI",0,2)
        ]
        if(self.contas[0].existe_conta_duplicada()):
            messagebox.showerror("Erro","Existe Conta Duplicada")
            messagebox.showinfo("Contas",self.contas[0].contas_duplicadas())
            exit()
        self.criar_interface()
    
    def criar_interface(self):
        titulo = tk.Label(
            self.janela,
            text="Banco Python - Contas Bancárias",
            font=("Arial", 18, "bold")
        )
        titulo.pack(pady=15)
        btn_criar_conta = tk.Button(
            self.janela,
            text="Criar Conta",
            width=15,
            command=lambda :self.criar_conta()
                )
                # btn_sacar.config(state="active")
        btn_criar_conta.pack(pady=2)
        self.frame_contas = tk.Frame(self.janela)
        self.frame_contas.pack()

        self.atualizar_tela()

    def atualizar_tela(self):
        for widget in self.frame_contas.winfo_children():
            widget.destroy()

        for conta in self.contas:
            frame = tk.Frame(
                self.frame_contas,
                borderwidth=2,
                relief="groove",
                padx=10,
                pady=10
            )
            frame.pack(side="left", padx=10, pady=10)
           

            lbl_titular = tk.Label(
                frame,
                text=conta.get_cliente().get_nome(),
                font=("Arial", 14, "bold")
            )
            lbl_titular.pack()

            lbl_numero = tk.Label(
                frame,
                text=f"Conta: {conta.get_numero()}"
            )
            lbl_numero.pack()

            lbl_saldo = tk.Label(
                frame,
                text=f"Saldo: R$ {conta.get_saldo():.2f}",
                font=("Arial", 12)
            )
            lbl_saldo.pack(pady=5)

            lbl_tipo_conta = tk.Label(
                frame,
                text=f"{conta.get_tipo_conta()}",
                font=("Arial", 12)
            )
            lbl_tipo_conta.pack(pady=5)
            btn_depositar = tk.Button(
                frame,
                text="Depositar",
                width=15,
                command=lambda conta=conta: self.depositar(conta)
            )
            # btn_depositar.config(state="active")
            btn_depositar.pack(pady=2)

            btn_sacar = tk.Button(
                frame,
                text="Sacar",
                width=15,
                command=lambda conta=conta: self.sacar(conta)
            )
            # btn_sacar.config(state="active")
            btn_sacar.pack(pady=2)

            btn_transferir = tk.Button(
                frame,
                text="Transferir",
                width=15,
                command=lambda conta=conta: self.transferir(conta)
            )
            # btn_transferir.config(state="active")
            btn_transferir.pack(pady=2)

            btn_dados = tk.Button(
                frame,
                text="Exibir Dados",
                width=15,
                command=lambda conta=conta: self.exibir_dados(conta)
            )
            # btn_dados.config(state="active")
            btn_dados.pack(pady=2)

            btn_rendimento = tk.Button(
                frame,
                text="Render Juros",
                width=15,
                command=lambda conta=conta: self.render_juros(conta)
            )
            if conta.get_tipo_conta() == "Conta Poupança":
                btn_rendimento.config(state="active")
            else:
                btn_rendimento.config(state="disabled")
            btn_rendimento.pack(pady=2)

            btn_taxa = tk.Button(
                frame,
                text="Cobrar Taxa",
                width=15,
                command=lambda conta=conta: self.cobrar_taxa(conta)
            )
            if conta.get_tipo_conta() == "Conta Corrente":
                btn_taxa.config(state="active")
            else:
                btn_taxa.config(state="disabled")
            btn_taxa.pack(pady=2)
            btn_salario = tk.Button(
                frame,
                text="Receber Salário",
                width=15,
                command=lambda conta=conta: self.receber_salario(conta)
            )
            if conta.get_tipo_conta() == "Conta Salário":
                btn_salario.config(state="active")
            else:
                btn_salario.config(state="disabled")
            btn_salario.pack(pady=2)
            btn_contas = tk.Button(
                frame,
                text="Contas do Cliente",
                width=15,
                command=lambda conta=conta: self.contas_cliente(conta)
            )
            btn_contas.pack(pady=2)

    def depositar(self, conta):
        valor = simpledialog.askfloat("Depósito", "Digite o valor do depósito:")

        if valor is not None:
            if conta.depositar(valor):
                messagebox.showinfo("Sucesso", "Depósito realizado.")
            else:
                messagebox.showerror("Erro", "Valor inválido.")

        self.atualizar_tela()

    def sacar(self, conta):
        valor = simpledialog.askfloat("Saque", "Digite o valor do saque:")

        if valor is not None:
            if conta.sacar(valor):
                messagebox.showinfo("Sucesso", "Saque realizado.")
                
            else:
                messagebox.showerror("Erro", "=== Opções de Falha ===\n1- Valor Inválido\n2- Saldo/Limite Insuficiente\n3- Conta não disponibiliza saque\n4- Limite de Saques Atingido")

        self.atualizar_tela()

    def transferir(self, conta_origem):
        valor = simpledialog.askfloat("Transferência", "Digite o valor:")

        if valor is None:
            return

        numero_destino = simpledialog.askinteger(
            "Transferência",
            "Digite o número da conta destino:"
        )

        conta_destino = None

        for conta in self.contas:
            if conta.get_numero() == numero_destino:
                conta_destino = conta
                break

        if conta_destino is None:
            messagebox.showerror("Erro", "Conta destino não encontrada.")
            return

        if conta_origem == conta_destino:
            messagebox.showerror("Erro", "Não é possível transferir para a mesma conta.")
            return

        if conta_origem.transferir(valor, conta_destino):
            messagebox.showinfo("Sucesso", "Transferência realizada.")
        else:
            messagebox.showerror("Erro", "Saldo/Limite insuficiente ou valor inválido.")

        self.atualizar_tela()

    def exibir_dados(self, conta):
        messagebox.showinfo("Dados da Conta", conta.exibir_dados())

    def render_juros(self, conta):
        if(conta.get_tipo_conta() == "Conta Poupança"):
            conta.render_juros()
            messagebox.showwarning("Sucesso", "Rendimento efetuado.")
        else:
            messagebox.showerror("Erro", "Conta não disponibiliza rendimento")
        self.atualizar_tela()
    
    def cobrar_taxa(self, conta):
        if(conta.get_tipo_conta() == "Conta Corrente"):
            conta.cobrar_taxa()
            messagebox.showwarning("Sucesso", "Cobrança efetuada.")
        else:
            messagebox.showerror("Erro", "Cobrança invalida para essa conta")
        self.atualizar_tela()

    def receber_salario(self, conta):
        if(conta.get_tipo_conta() == "Conta Salário"):
            valor = simpledialog.askfloat("Salário", "Digite o valor do salário:")

            if valor is not None:
                conta.receber_salario(valor)
            messagebox.showwarning("Sucesso", " Salário efetuado.")
        else:
            messagebox.showerror("Erro", "Conta não recebe Salário")
        self.atualizar_tela()
    def contas_cliente(self, conta):
        cliente = conta.get_cliente()

        texto = ""

        for conta in self.contas:
            if conta.get_cliente().get_cpf() == cliente.get_cpf():
                texto += (
                    f"{conta.get_tipo_conta()} - "
                    f"Conta {conta.get_numero()} - "
                    f"Saldo: R${conta.get_saldo():.2f}\n"
                )

        messagebox.showinfo("Contas do Cliente", texto)

    def criar_conta(self):
        janela_cadastro = tk.Toplevel(self.janela)
        janela_cadastro.title("Criar nova conta")
        janela_cadastro.geometry("800x800")
        janela_cadastro.resizable(False,False)

        tk.Label(janela_cadastro, text="Titular:").pack(pady=5)
        entrada_titular = tk.Entry(janela_cadastro)
        entrada_titular.pack()

        tk.Label(janela_cadastro, text="CPF:").pack(pady=5)
        entrada_cpf = tk.Entry(janela_cadastro)
        entrada_cpf.pack()
        tk.Label(janela_cadastro, text="Tipo de Conta:").pack(pady=5)
        entrada_tipoconta = tk.Entry(janela_cadastro)
        entrada_tipoconta.pack()
        tk.Label(janela_cadastro, text="Número da conta:").pack(pady=5)
        entrada_numero = tk.Entry(janela_cadastro)
        entrada_numero.pack()

        tk.Label(janela_cadastro, text="Saldo inicial:").pack(pady=5)
        entrada_saldo = tk.Entry(janela_cadastro)
        entrada_saldo.pack()
        tk.Label(janela_cadastro, text="Rua:").pack(pady=5)
        entrada_rua = tk.Entry(janela_cadastro)
        entrada_rua.pack()

        tk.Label(janela_cadastro, text="Número:").pack(pady=5)
        entrada_numerocasa= tk.Entry(janela_cadastro)
        entrada_numerocasa.pack()
        tk.Label(janela_cadastro, text="Bairro:").pack(pady=5)
        entrada_bairro = tk.Entry(janela_cadastro)
        entrada_bairro.pack()

        tk.Label(janela_cadastro, text="Cidade:").pack(pady=5)
        entrada_cidade = tk.Entry(janela_cadastro)
        entrada_cidade.pack()
        tk.Label(janela_cadastro, text="Empresa:").pack(pady=5)
        entrada_empresa = tk.Entry(janela_cadastro)
        entrada_empresa.pack()
        tk.Label(janela_cadastro, text="Taxa Rendimento:").pack(pady=5)
        entrada_taxa = tk.Entry(janela_cadastro)
        entrada_taxa.pack()
        tk.Label(janela_cadastro, text="Limite de Saques:").pack(pady=5)
        entrada_limite_saques = tk.Entry(janela_cadastro)
        entrada_limite_saques.pack()
        tk.Label(janela_cadastro, text="Saques Realizados:").pack(pady=5)
        entrada_saques_realizados = tk.Entry(janela_cadastro)
        entrada_saques_realizados.pack()
        tk.Label(janela_cadastro, text="Cobrança da Tarifa:").pack(pady=5)
        entrada_tarifa = tk.Entry(janela_cadastro)
        entrada_tarifa.pack()


        

        def salvar_conta():
            titular = "Lennedy"
            cpf = "123-654-321-21"
            rua  = "Rua 4"
            numerocasa = 192
            bairro = "Bairro 7"
            cidade = "Cidade 2"
            saldo = 2000
            numero = 1008
            tipo = "Poupança"
            limite = 1000
            tarifa_mensal = 50
            empresa = "IFRN"
            saques_realizados = 0
            limite_saques = 3
            taxa_rendimento = 0.1

            # titular = entrada_titular.get()
            # cpf = entrada_cpf.get()
            # rua  = entrada_rua.get()
            # numerocasa = entrada_numerocasa.get()
            # bairro = entrada_bairro.get()
            # cidade = entrada_cidade.get()
            # saldo = entrada_saldo.get()
            # numero = entrada_numero.get()
            # tipo = entrada_tipoconta.get()

            if titular == "" or cpf == "" or numero == "" or saldo == "" or  rua == "" or bairro == "" or cidade == "" or numerocasa == "" or tipo =="" :
                messagebox.showerror("Erro", "Preencha todos os campos.")
                return

            try:
                numero = int(numero)
                saldo = float(saldo)
            except ValueError:
                messagebox.showerror("Erro", "Número da conta e saldo devem ser valores numéricos.")
                return
            cliente = Cliente(titular,cpf,rua,numerocasa,bairro,cidade)
            if tipo == "Bancária":
                nova_conta = ContaBancaria(cliente, numero, saldo)
                self.contas.append(nova_conta)
            if tipo == "Corrente":
                nova_conta = ContaCorrente(cliente, numero, saldo,limite,tarifa_mensal)
                self.contas.append(nova_conta)
            if tipo == "Poupança":
                nova_conta = ContaPoupanca(cliente, numero, saldo,taxa_rendimento)
                self.contas.append(nova_conta)
            if tipo == "Salário":
                nova_conta = ContaSalario(cliente, numero, saldo,empresa,saques_realizados,limite_saques)
                self.contas.append(nova_conta)
            

            messagebox.showinfo("Sucesso", "Conta criada com sucesso.")

            # janela_cadastro.destroy()
            self.atualizar_tela()

        btn_salvar = tk.Button(
            janela_cadastro,
            text="Salvar conta",
            width=15,
            command=salvar_conta
        )
        btn_salvar.pack(pady=15)
janela = tk.Tk()
app = BancoApp(janela)
janela.mainloop()