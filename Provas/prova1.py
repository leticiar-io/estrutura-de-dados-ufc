class Midia:
    def __init__(self, titulo, duracao):
        self.titulo = titulo
        self.duracao = duracao

    def exibir_informacoes(self):
        print(f"✨ Mídia: {self.titulo} | Duração: {self.duracao} ✨")

class Video(Midia):
    def __init__(self, titulo, duracao, resolucao):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao

    def exibir_informacoes(self):
        print(f"✨ Título: {self.titulo} | Duração: {self.duracao} | Resolução: {self.resolucao} ✨")

class Audio(Midia):
    def __init__(self, titulo, duracao, formato):
        super().__init__(titulo, duracao)
        self.formato = formato

    def exibir_informacoes(self):
        print(f"✨ Título: {self.titulo} | Duração: {self.duracao} | Formato: {self.formato} ✨")

class Foto(Midia):
    def __init__(self, titulo, duracao, resolucao, formato):
        super().__init__(titulo, duracao)
        self.resolucao = resolucao
        self.formato = formato

    def exibir_informacoes(self):
        print(f"✨ Título: {self.titulo} | Duração: {self.duracao} | Resolução: {self.resolucao} | Formato: {self.formato} ✨")

class Playlist:
    def __init__(self):
        self.midias = [] # Lista de objetos de midias

    def adicionar_midia(self, midia):
        self.midias.append(midia)
        print(f"A Mídia '{midia.titulo}' foi adicionada na playlist.")

    def remover_midia(self, titulo):
        for midia in self.midias:
            if midia.titulo == titulo:
                self.midias.remove(midia)
                print(f"Mídia '{titulo}' foi removida da playlist.")
            else: 
                print(f"Mídia '{titulo}' não encontrada na playlist.")

    def exibir_playlist(self):
        if not self.midias: 
            print("A playlist está vazia.")
        else: 
            for midia in self.midias:
                midia.exibir_informacoes()

class Usuario:
    def __init__(self, nome, id):
        self.nome = nome
        self.id = id
        self.playlist = Playlist()

    def adicionar_midia_playlist(self, midia):
        self.playlist.adicionar_midia(midia)

    def remover_midia_playlist(self, titulo):
        self.playlist.remover_midia(titulo)

    def exibir_playlist_usuario(self):
        print(f"Playlist do usuário {self.nome}:")
        self.playlist.exibir_playlist()

class Biblioteca:
    def __init__(self):
        self.usuarios = {}

    def adicionar_usuario(self, usuario):
        self.usuarios[usuario.id] = usuario
        print(f"Usuário '{usuario.nome}' adicionado com ID {usuario.id}.")

    def remover_usuario(self, id):
        if id in self.usuarios:
            del self.usuarios[id]
            print(f"Usuário com ID {id} removido.")
        else:
            print(f"Usuário com ID {id} não encontrado.")

    def listar_usuarios(self):
        print("-"*20)
        if not self.usuarios:
            print("Nenhum usuário cadastrado.")
        else:
            for usuario in self.usuarios.values():
                print(f"Nome: {usuario.nome} | ID: {usuario.id}")
        print("-"*20)

    def exibir_playlist_usuario(self, id):
        print("-"*20)
        if id in self.usuarios:
            self.usuarios[id].exibir_playlist_usuario()
        else:
            print(f"Usuário com ID {id} não encontrado.")
        print("-"*20)

def menu():
    biblioteca = Biblioteca()
    while True:
        print("\n✨--- Menu de Gerenciamento de Mídia ---✨")
        print("1. Adicionar Usuário")
        print("2. Remover Usuário")
        print("3. Listar Usuários")
        print("4. Adicionar Mídia na Playlist do Usuário")
        print("5. Remover Mídia da Playlist do Usuário")
        print("6. Exibir Playlist de um Usuário")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome do usuário: ")
            id = input("Digite o ID do usuário: ")
            usuario = Usuario(nome, id)
            biblioteca.adicionar_usuario(usuario)

        elif opcao == "2":
            id = input("Digite o ID do usuário a ser removido: ")
            biblioteca.remover_usuario(id)

        elif opcao == "3":
            biblioteca.listar_usuarios()

        elif opcao == "4":
            id = input("Digite o ID do usuário: ")
            tipo = input("Digite o tipo de mídia (Video, Audio, Foto): ")
            titulo = input("Digite o título da mídia: ")
            duracao = input("Digite a duração da mídia: ")

            if tipo == "Video":
                resolucao = input("Digite a resolução do vídeo: ")
                midia = Video(titulo, duracao, resolucao)
            elif tipo == "Audio":
                formato = input("Digite o formato do áudio: ")
                midia = Audio(titulo, duracao, formato)

            elif tipo == "Foto":
                resolucao = input("Digite a resolução da foto: ")
                formato = input("Digite o formato da foto: ")
                midia = Foto(titulo, duracao, resolucao, formato)
            else:
                print("Tipo de mídia inválido.")
                continue

            usuario = biblioteca.usuarios.get(id)
            if usuario:
                usuario.adicionar_midia_playlist(midia)
            else:
                print("Usuário não encontrado.")

        elif opcao == "5":
            id = input("Digite o ID do usuário: ")
            titulo = input("Digite o título da mídia a ser removida: ")
            usuario = biblioteca.usuarios.get(id)
            if usuario:
                usuario.remover_midia_playlist(titulo)
            else:
                print("Usuário não encontrado.")

        elif opcao == "6":
            id = input("Digite o ID do usuário: ")
            biblioteca.exibir_playlist_usuario(id)

        elif opcao == "0":
            print("Saindo do sistema. Até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

menu()