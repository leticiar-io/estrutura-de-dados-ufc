class Cliente:
    def __init__(self, numero_conta, nome, valor_conta, credito_disponivel):
        self.numero_conta = numero_conta
        self.nome = nome
        self.valor_conta = valor_conta
        self.credito_disponivel = credito_disponivel
        self.proximo = None

    def __str__(self):
        return f"Número da Conta: {self.numero_conta}, Nome: {self.nome}, Valor: R${self.valor_conta:.2f}, Crédito disponível: R${self.credito_disponivel:.2f}"

class Pilha:
    def __init__(self):
        self.topo = None  # Topo da pilha
        self.tamanho = 0
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
        for id, nome, valor_conta, credito_disponivel in clientes_iniciais:
            self.empilhar(id, nome, valor_conta, credito_disponivel)

    def empilhar(self, numero_conta, nome, valor_conta, credito_disponivel):  # Adicionar cliente no topo
        novo_cliente = Cliente(numero_conta, nome, valor_conta, credito_disponivel)
        novo_cliente.proximo = self.topo
        self.topo = novo_cliente
        self.tamanho += 1

    def desempilhar(self):  # Remover cliente do topo
        if not self.topo:
            print("Pilha vazia, não há clientes para remover.")
            return None
        cliente_removido = self.topo
        self.topo = self.topo.proximo
        self.tamanho -= 1
        print(f"Cliente com número da conta {cliente_removido.numero_conta} removido.")
        return cliente_removido

    def listar_clientes(self):
        atual = self.topo
        if not atual:
            print("Não há clientes na pilha.")
        while atual:
            print(atual)
            atual = atual.proximo

    def ordenar_clientes_crescente(self):
        if not self.topo or not self.topo.proximo:
            return

        trocou = True
        while trocou:
            trocou = False
            atual = self.topo
            while atual.proximo:
                if atual.credito_disponivel > atual.proximo.credito_disponivel:
                    # Troca os dados dos clientes
                    atual.numero_conta, atual.proximo.numero_conta = atual.proximo.numero_conta, atual.numero_conta
                    atual.nome, atual.proximo.nome = atual.proximo.nome, atual.nome
                    atual.valor_conta, atual.proximo.valor_conta = atual.proximo.valor_conta, atual.valor_conta
                    atual.credito_disponivel, atual.proximo.credito_disponivel = atual.proximo.credito_disponivel, atual.credito_disponivel
                    trocou = True
                atual = atual.proximo

    def ordenar_clientes_decrescente(self):
        if not self.topo or not self.topo.proximo:
            return

        trocou = True
        while trocou:
            trocou = False
            atual = self.topo
            while atual.proximo:
                if atual.credito_disponivel < atual.proximo.credito_disponivel:
                    # Troca os dados dos clientes
                    atual.numero_conta, atual.proximo.numero_conta = atual.proximo.numero_conta, atual.numero_conta
                    atual.nome, atual.proximo.nome = atual.proximo.nome, atual.nome
                    atual.valor_conta, atual.proximo.valor_conta = atual.proximo.valor_conta, atual.valor_conta
                    atual.credito_disponivel, atual.proximo.credito_disponivel = atual.proximo.credito_disponivel, atual.credito_disponivel
                    trocou = True
                atual = atual.proximo

    def mostrar_tamanho(self):
        return self.tamanho


def main():
    pilha = Pilha()

    while True:
        print("\nGerenciamento de Banco (Pilha)")
        print("1. Listar todos os clientes")
        print("2. Adicionar cliente")
        print("3. Remover cliente")
        print("4. Ordenar clientes por crédito (crescente)")
        print("5. Ordenar clientes por crédito (decrescente)")
        print("6. Mostrar tamanho da pilha")
        print("7. Sair")

        escolha = int(input("Digite sua escolha: "))

        if escolha == 1:
            print("\nLista de todos os clientes:")
            pilha.listar_clientes()
        elif escolha == 2:
            numero_conta = input("Digite o número da conta do cliente: ")
            nome = input("Digite o nome do cliente: ")
            valor_conta = float(input("Digite o valor da conta do cliente: "))
            credito_disponivel = float(input("Digite o crédito disponível do cliente: "))
            pilha.empilhar(numero_conta, nome, valor_conta, credito_disponivel)
            print("Cliente adicionado com sucesso.")
        elif escolha == 3:
            pilha.desempilhar()
        elif escolha == 4:
            pilha.ordenar_clientes_crescente()
            print("Clientes ordenados por crédito disponível em ordem crescente.")
            print("Digite 1 para listar os clientes.")
        elif escolha == 5:
            pilha.ordenar_clientes_decrescente()
            print("Clientes ordenados por crédito disponível em ordem decrescente.")
            print("Digite 1 para listar os clientes.")
        elif escolha == 6:
            tamanho = pilha.mostrar_tamanho()
            print(f"Tamanho da pilha: {tamanho}")
        elif escolha == 7:
            print("Saindo...")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
