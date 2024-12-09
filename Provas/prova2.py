class Cliente:
    def __init__(self, numero_conta, nome, valor_conta, credito_disponivel):
        self.numero_conta = numero_conta
        self.nome = nome
        self.valor_conta = valor_conta
        self.credito_disponivel = credito_disponivel
        self.proximo = None
        self.anterior = None

    def __str__(self):
        return f"Número da Conta: {self.numero_conta}, Nome: {self.nome}, Valor: R${self.valor_conta:.2f}, Crédito disponível: R${self.credito_disponivel:.2f}"

class Banco:
    def __init__(self):
        self.head = None
        self.tail = None
        self.inicializar_clientes()
    
    def inicializar_clientes(self):
        clientes_iniciais = [
            ("1", "Letícia", 15000, 5000),
            ("2", "Jomar", 3000, 200),
            ("3", "Vitor", 50, 100),
            ("4", "Mathias", 200, 1000),
            ("5", "Xilo", 30, 1500),
            ("6", "Ticia", 450, 500),
        ]
        anterior = None
        for id, nome, valor_conta, credito_disponivel in clientes_iniciais:
            novo_cliente = Cliente(id, nome, valor_conta, credito_disponivel)
            if self.head is None:
                self.head = novo_cliente
            else:
                anterior.proximo = novo_cliente
                novo_cliente.anterior = anterior
            anterior = novo_cliente
        self.tail = anterior

    def adicionar_cliente(self, numero_conta, nome, valor_conta, credito_disponivel):
        novo_cliente = Cliente(numero_conta, nome, valor_conta, credito_disponivel)
        if not self.head:
            self.head = novo_cliente
            self.tail = novo_cliente
            return
        self.tail.proximo = novo_cliente
        novo_cliente.anterior = self.tail
        self.tail = novo_cliente

    def remover_cliente(self, numero_conta):
        atual = self.head
        while atual and atual.numero_conta != numero_conta:
            atual = atual.proximo
        if atual is None:
            print("Cliente não encontrado.")
            return
        if atual.anterior:
            atual.anterior.proximo = atual.proximo
        if atual.proximo:
            atual.proximo.anterior = atual.anterior
        if atual == self.head:
            self.head = atual.proximo
        if atual == self.tail:
            self.tail = atual.anterior
        print(f"Cliente com número da conta {numero_conta} removido.")

    def listar_clientes(self):
        atual = self.head
        if not atual:
            print("Não há clientes cadastrados.")
        while atual:
            print(atual)
            atual = atual.proximo

    def ordenar_clientes_crescente(self):
        if not self.head or not self.head.proximo:
            return 

        trocou = True
        while trocou:
            trocou = False
            atual = self.head
            while atual.proximo:
                if atual.credito_disponivel > atual.proximo.credito_disponivel:
                    atual.numero_conta, atual.proximo.numero_conta = atual.proximo.numero_conta, atual.numero_conta
                    atual.nome, atual.proximo.nome = atual.proximo.nome, atual.nome
                    atual.valor_conta, atual.proximo.valor_conta = atual.proximo.valor_conta, atual.valor_conta
                    atual.credito_disponivel, atual.proximo.credito_disponivel = atual.proximo.credito_disponivel, atual.credito_disponivel
                    atual.proximo.anterior = atual
                    if atual.proximo.proximo:
                        atual.proximo.proximo.anterior = atual.proximo
                    trocou = True
                atual = atual.proximo

    def ordenar_clientes_decrescente(self):
        if not self.head or not self.head.proximo:
            return  
        
        trocou = True
        while trocou:
            trocou = False
            atual = self.head
            while atual.proximo:
                if atual.credito_disponivel < atual.proximo.credito_disponivel:
                    atual.numero_conta, atual.proximo.numero_conta = atual.proximo.numero_conta, atual.numero_conta
                    atual.nome, atual.proximo.nome = atual.proximo.nome, atual.nome
                    atual.valor_conta, atual.proximo.valor_conta = atual.proximo.valor_conta, atual.valor_conta
                    atual.credito_disponivel, atual.proximo.credito_disponivel = atual.proximo.credito_disponivel, atual.credito_disponivel
                    atual.proximo.anterior = atual
                    if atual.proximo.proximo:
                        atual.proximo.proximo.anterior = atual.proximo
                    trocou = True
                atual = atual.proximo

def main():
    banco = Banco()

    while True:
        print("\nGerenciamento de Banco")
        print("1. Listar todos os clientes")
        print("2. Adicionar cliente")
        print("3. Remover cliente")
        print("4. Ordenar clientes por crédito (crescente)")
        print("5. Ordenar clientes por crédito (decrescente)")
        print("6. Sair")

        escolha = int(input("Digite sua escolha: "))

        if escolha == 1:
            print("\nLista de todos os clientes:")
            banco.listar_clientes()
        elif escolha == 2:
            numero_conta = input("Digite o número da conta do cliente: ")
            nome = input("Digite o nome do cliente: ")
            valor_conta = float(input("Digite o valor da conta do cliente: "))
            credito_disponivel = float(input("Digite o crédito disponível do cliente: "))
            banco.adicionar_cliente(numero_conta, nome, valor_conta, credito_disponivel)
            print("Cliente adicionado com sucesso.")
        elif escolha == 3:
            numero_conta = input("Digite o número da conta do cliente a ser removido: ")
            banco.remover_cliente(numero_conta)
        elif escolha == 4:
            banco.ordenar_clientes_crescente()
            print("Clientes ordenados por crédito disponível em ordem crescente.")
            print("Digite 1 para listar os clientes.")
        elif escolha == 5:
            banco.ordenar_clientes_decrescente()
            print("Clientes ordenados por crédito disponível em ordem decrescente.")
            print("Digite 1 para listar os clientes.")
        elif escolha == 6:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()