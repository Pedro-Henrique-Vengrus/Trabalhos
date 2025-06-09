def criar_no(valor):
    return {"valor": valor, "esquerda": None, "direita": None}

def inserir(no, valor):
    if no is None:
        return criar_no(valor)
    if valor < no["valor"]:
        no["esquerda"] = inserir(no["esquerda"], valor)
    else:
        no["direita"] = inserir(no["direita"], valor)
    return no

def menor_valor(no):
    atual = no
    while atual["esquerda"] is not None:
        atual = atual["esquerda"]
    return atual["valor"]

def remover(no, valor):
    if no is None:
        return None
    if valor < no["valor"]:
        no["esquerda"] = remover(no["esquerda"], valor)
    elif valor > no["valor"]:
        no["direita"] = remover(no["direita"], valor)
    else:
        if no["esquerda"] is None and no["direita"] is None:
            return None
        elif no["esquerda"] is None:
            return no["direita"]
        elif no["direita"] is None:
            return no["esquerda"]
        else:
            sucessor = menor_valor(no["direita"])
            no["valor"] = sucessor
            no["direita"] = remover(no["direita"], sucessor)
    return no

def em_ordem(no):
    if no is not None:
        em_ordem(no["esquerda"])
        print(no["valor"], end=" ")
        em_ordem(no["direita"])

arvore = None
for test in [50, 30, 20, 40, 70, 60, 80]:
    arvore = inserir(arvore, test)

print("Árvore original:")
em_ordem(arvore)

print(" ")

arvore = remover(arvore, 20)
print("\nApós remover 20:")
em_ordem(arvore)

print(" ")

arvore = remover(arvore, 50)
print("\nApós remover 30:")
em_ordem(arvore)

print(" ")

arvore = remover(arvore, 70)
print("\nApós remover 70:")
em_ordem(arvore)
