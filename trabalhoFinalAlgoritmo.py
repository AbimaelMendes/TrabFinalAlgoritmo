vetClientes=[]

class Ccliente:
    cpf = 0
    email = ""
    nome = ""
    sobrenome = ""  
    endereco = ""
    telefone = 0
    numConta = 0
    saldo = 0
    credito = 0  

def lerCliente():
    cli = Ccliente()  
    cli.nome=input("Nome:")
    cli.sobrenome=input("Sobrenome:")
    cli.cpf=int(input("CPF:"))
    cli.email=input("E-mail:")
    cli.endereco=input("Endereco:")
    cli.telefone=int(input("Telefone:"))
    cli.numConta=int(input("Número da conta:"))
    cli.saldo=float(input("Saldo:"))
    vetClientes.append(cli) 

def listarClientes(x):
    for i in vetClientes:
        print("Nome:",i.nome,"",i.sobrenome)
        print("CPF:",i.cpf)
        print("E-mail",i.email)
        print("Endereço:",i.endereco)
        print("Telefone:",i.telefone)
        print("Número da conta corrente: ",i.numConta)
        print("Limite de crédito:",i.credito,"R$")
        print("Saldo:",i.saldo,"R$")
        print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")
        
    

lerCliente()
lerCliente()
listarClientes(vetClientes)        
