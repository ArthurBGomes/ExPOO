from cliente import Cliente
from ContaBancaria import ContaBancaria
from ContaCorrente import ContaCorrente
from ContaPoupanca import ContaPoupanca
cliente1 = Cliente("Arthur","123.456.789","Rua 1",196,"Bairro 2","Cidade 1")
 
c1 = ContaCorrente(cliente1, 1003, 200,1000,100)  
c2 = ContaPoupanca(cliente1, 1004, 20,0.1)
c3 = ContaBancaria(cliente1, 1005, 20)
cliente1.adicionar_conta(c1)
cliente1.adicionar_conta(c2)
cliente1.adicionar_conta(c3)
print(cliente1.possui_conta())
print(cliente1.buscar_conta(1004))
print(cliente1.consultar_saldo_total())