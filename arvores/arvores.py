class No:
    chave = None
    esq = None
    dir = None

def inserirNo(raiz, chave):
    if raiz == None:
        novoNo = No()
        novoNo.chave = chave
        return novoNo

    if raiz.chave > chave:
        raiz.esq = inserirNo(raiz.esq, chave)
        
    elif raiz.chave < chave:
        raiz.dir = inserirNo(raiz.dir, chave)
    
    return raiz

def exibirInOrder(raiz):
    if raiz == None:
        return
    
    exibirInOrder(raiz.esq)
    print(raiz.chave, end=' ')
    exibirInOrder(raiz.dir)

def exibirPreOrder(raiz):
    if raiz == None:
        return
    
    print(raiz.chave, end=' ')
    exibirPreOrder(raiz.esq)
    exibirPreOrder(raiz.dir)

def exibirPosOrder(raiz):
    if raiz == None:
        return

    exibirPosOrder(raiz.esq)
    exibirPosOrder(raiz.dir)
    print(raiz.chave, end=' ')

    
raiz = None
raiz = inserirNo(raiz, 90)
raiz = inserirNo(raiz, 40)
raiz = inserirNo(raiz, 50)
raiz = inserirNo(raiz, 110)
raiz = inserirNo(raiz, 108)
raiz = inserirNo(raiz, 30)
raiz = inserirNo(raiz, 190)

exibirInOrder(raiz)
print('\n')
exibirPreOrder(raiz)
print('\n')
exibirPosOrder(raiz)