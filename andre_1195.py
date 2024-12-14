class NoArvore:
    def __init__(self, value):
        self.esq = None
        self.valor = value
        self.dir = None

def acha_pai(r, v):
    if r is None:
        return None
    else:
        if v <= r.valor:
            if r.esq is None:
                return r
            else:
                return acha_pai(r.esq, v)
        else:
            if r.dir is None:
                return r
            else:
                return acha_pai(r.dir, v)

def imprime_arvore(r):
    global tipo
    if r is not None:
        if tipo == 1:
            print(f" {r.valor}", end="")
            imprime_arvore(r.esq)
            imprime_arvore(r.dir)
        elif tipo == 2:
            imprime_arvore(r.esq)
            print(f" {r.valor}", end="")
            imprime_arvore(r.dir)
        elif tipo == 3:
            imprime_arvore(r.esq)
            imprime_arvore(r.dir)
            print(f" {r.valor}", end="")

def main():
    global tipo
    raiz = None
    n_casos = int(input())

    for c in range(1, n_casos + 1):
        raiz = None
        tam = int(input())
        valores = input().split()
        for i in range(tam):
            noh = int(valores[i])
            aux = NoArvore(noh)
            pai = acha_pai(raiz, noh)
            if pai is None:
                raiz = aux
            else:
                if noh <= pai.valor:
                    pai.esq = aux
                else:
                    pai.dir = aux

        print(f"Case {c}:")

        print("Pre.:", end="")
        tipo = 1
        imprime_arvore(raiz)
        print()

        print("In..:", end="")
        tipo = 2
        imprime_arvore(raiz)
        print()

        print("Post:", end="")
        tipo = 3
        imprime_arvore(raiz)
        print("\n")

if __name__ == "__main__":
    main()
