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

def lerCliente(x):
    cli = Ccliente()  
    cli.nome=input("Nome:")
    cli.sobrenome=input("Sobrenome:")
    cli.cpf=verificaCpf()
    cli.email=input("E-mail:")
    cli.endereco=input("Endereco:")
    cli.telefone=int(input("Telefone:"))
    cli.numConta=int(input("Número da conta:"))
    cli.saldo=float(input("Saldo:"))
    x.append(cli)
    

def listarClientes(x):
    for i in range(len(x)):
        print("id:",i)
        print("Nome:",vetClientes[i].nome,"",vetClientes[i].sobrenome)
        print("CPF:",vetClientes[i].cpf)
        print("E-mail",vetClientes[i].email)
        print("Endereço:",vetClientes[i].endereco)
        print("Telefone:",vetClientes[i].telefone)
        print("Número da conta corrente: ",vetClientes[i].numConta)
        print("Limite de crédito:",vetClientes[i].credito,"R$")
        print("Saldo:",vetClientes[i].saldo,"R$")
        print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")

def verificaCpf():
    ok=True
    while ok: 
        cpf=int(input("CPF:"))   
        for i in range(len(vetClientes)):
            print(i)
            if cpf == vetClientes[i].cpf:
                print("CPF já cadastrado!")
            else:
                ok=False 
                return cpf

                           

lerCliente(vetClientes)
sja=verificaCpf()
print(sja)

      
