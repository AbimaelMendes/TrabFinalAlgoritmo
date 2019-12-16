#vetor onde os clintes serão armazenados.
vetClientes=[]

#classe clientes com seus atributos.
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
    stotal = 0  

#Essa função le os dados digitados pelo gerente e armazena no vetor.
def lerCliente(x):
    cli = Ccliente()  
    cli.nome=input("Nome:")
    cli.sobrenome=input("Sobrenome:")
    cli.email=input("E-mail:")
    cli.endereco=input("Endereco:")
    cli.telefone=int(input("Telefone:"))
    cli.saldo=float(input("Saldo:"))
    cli.credito=1000
    cli.stotal=cli.saldo + cli.credito
    x.append(cli)
    cli.cpf=verificaCpf(vetClientes)
    cli.numConta=verificaConta(vetClientes)
    

#Lisa de forma ordenadas todos os clientes.
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
        print("Saldo total:",vetClientes[i].stotal)
        print("zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz")

#verifica se o cpf ja existe no vetor.
def verificaCpf(vetClientes):
    ok=True
    while ok: 
        cpf=int(input("CPF:"))   
        for i in range(len(vetClientes)):
            if cpf != vetClientes[i].cpf:
                ok=False 
                return cpf
            else:
                print("CPF já cadastrado!")
                break
                

#verifica se a conta ja existe no vetor.
def verificaConta(vetClientes):
    ok=True
    while ok: 
        conta=int(input("Número da conta:"))   
        for i in range(len(vetClientes)):
            if conta == vetClientes[i].numConta:
                print("Conta já cadastrada!")
                break
            else:   
                ok=False 
                return conta

#altera os dados de determinado cliente, selhecionado pelo cpf do memso.
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
                        atualiza=verificaCpf(vetClientes)
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
                                        atualiza=verificaConta(vetClientes)
                                        vetClientes[i].numConta=atualiza
                                        print("Novo Número da conta:",vetClientes[i].numConta) 

#Exclui um determinado cliente do vetor de determinado cpf.
def excluiClinte(vetClientes):
    cliente=(int(input("Busca cliente por CPF:")))
    for i in range(len(vetClientes)):
        if cliente == vetClientes[i].cpf:
            print("Cliente:",vetClientes[i].nome,"",vetClientes[i].sobrenome)
            op=input("Deseja excluir este cliente? S/N:")
            if op.lower() != "s" and op.lower() != "n":
                print("opção inválida!")
            else:
                if op.lower() == "s":
                    vetClientes.pop(i)

#Faz movimentações na conta do cliente tais como adição e subtração do saldo.
def movimentoConta(vetClientes):
    print("========|GERENCIAMENTO DE CONTA CORRENTE|=========")
    for i in range(len(vetClientes)):
        print("Nome:",vetClientes[i].nome, "CPF:",vetClientes[i].cpf,"Saldo Total:",vetClientes[i].stotal)
        print("==========================================================================================")
    print("Digite o cpf do cliente que será feito as operações!")
    op=int(input(":"))
    for i in range(len(vetClientes)):
        if op == vetClientes[i].cpf:
            print("Nome:",vetClientes[i].nome,"Saldo Total:",vetClientes[i].stotal)
            op=int(input("1- Crédito ou 2- Débito:"))
            if op != 1 and op != 2:
                print("Opção inválida!")
            else:
                if op == 1:
                    valor=float(input("Valor:"))
                    vetClientes[i].stotal += valor
                else:
                    if op == 2:
                        valor=float(input("Valor:"))
                        if valor > vetClientes[i].stotal:
                            print("Saldo insuficiente!")
                        else:
                            vetClientes[i].stotal -= valor    




#loop da tela de menu.
x=True            
while x:
    print("=============|BEM VINDO ao vBANL|==============")
    print("1- Inserir clientes")
    print("2- Alterar dados de um cliente")
    print("3- Excluir Cliente")
    print("4- Listar todos os Clientes")
    print("5- Movimento da Conta")
    print("6- Sair")
    ok=True
    while ok:
        op=int(input("Digite a opção:"))
        if op < 1 or op > 6:
            print("Opção inválida!")
        else:
            if op == 1:
                lerCliente(vetClientes)
                ok=False
            else:
                if op == 2:
                    alteraCadastro(vetClientes)
                    ok=False
                else:
                    if op == 3:
                        excluiClinte(vetClientes)
                        ok=False
                    else:
                        if op == 4:
                            listarClientes(vetClientes)
                            ok=False
                        else:
                            if op == 5:
                                movimentoConta(vetClientes)
                                ok=False
                            else:
                                ok=False
                                print("Se você sair perderá todas as informações dos clientes!")
                                sair=input("Realmente deseja sair? S/N:")
                                if sair.lower() != "s" and sair.lower() != "n":
                                    print("opção inválida!")
                                else:
                                    if sair.lower() == "s": 
                                        x=False

                                