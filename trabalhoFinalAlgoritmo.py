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
    cli.email=input("E-mail:")
    cli.endereco=input("Endereco:")
    cli.telefone=int(input("Telefone:"))
    cli.saldo=float(input("Saldo:"))
    x.append(cli)
    cli.cpf=verificaCpf()
    cli.numConta=verificaConta()
    

def listarClientes(vetClientes):
    for i in range(len(vetClientes)):
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
            if cpf == vetClientes[i].cpf:
                print("CPF já cadastrado!")
            else:
                ok=False 
                return cpf

def verificaConta():
    ok=True
    while ok: 
        conta=int(input("Número da conta:"))   
        for i in range(len(vetClientes)):
            if conta == vetClientes[i].numConta:
                print("Conta já cadastrado!")
            else:
                ok=False 
                return conta

def alteraCadastro(vetClientes):
    cliente=(int(input("Busca cliente por CPF:")))
    for i in range(len(vetClientes)):
        if cliente == vetClientes[i].cpf:
            print("id:",i)
            print("1-Nome:",vetClientes[i].nome,"",vetClientes[i].sobrenome)
            print("2-CPF:",vetClientes[i].cpf)
            print("3-E-mail",vetClientes[i].email)
            print("4-Endereço:",vetClientes[i].endereco)
            print("5-Telefone:",vetClientes[i].telefone)
            print("6-Número da conta corrente: ",vetClientes[i].numConta) 
            print("ZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZZ")
            op=int(input("Digite o número da informação que você deseja alterar."))
            if op <=0 and ap >6:
                print("Opção inválida!")
            else:
                if op == 1:
                    print("Nome:",vetClientes[i].nome,"",vetClientes[i].sobrenome)
                    atualiza=input("Novo nome: ")
                    vetClientes[i].nome=atualiza
                    atualiza=input("Novo sobrenome:")
                    vetClientes[i].sobrenome=atualiza
                    print("Atualizado:",vetClientes[i].nome,"",vetClientes[i].sobrenome)
                else:
                    if op == 2:
                        print("CPF atual:",vetClientes[i].cpf)
                        atualiza=verificaCpf()
                        vetClientes[i].cpf=atualiza
                        print("Novo CPF:",vetClientes[i].cpf)
                    else:
                        if op == 3:
                            print("E-mail atual:",vetClientes[i].email)
                            atualiza=input("Novo E-mail:")
                            vetClientes[i].email=atualiza
                            print("Novo E-mail:",vetClientes[i].email)
                        else:
                            if op == 4:
                                print("Endereço atual:",vetClientes[i].endereco)  
                                atualiza=input("Novo endereço:")  
                                vetClientes[i].endereco=atualiza
                                print("Novo endereço:",vetClientes[i].endereco)    
                            else:
                                if op == 5:
                                    print("Telefone atual:",vetClientes[i].telefone)  
                                    atualiza=input("Novo telefone:")  
                                    vetClientes[i].telefone=atualiza
                                    print("Novo telefone:",vetClientes[i].telefone)
                                else:
                                    if op == 6:
                                        print("Número da conta atual:",vetClientes[i].numConta)
                                        atualiza=verificaConta()
                                        vetClientes[i].numConta=atualiza
                                        print("Novo Número da conta:",vetClientes[i].numConta) 
                                           
lerCliente(vetClientes)
lerCliente(vetClientes)
alteraCadastro(vetClientes)
alteraCadastro(vetClientes)
listarClientes(vetClientes) 

