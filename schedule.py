class Agenda:
    def __init__(self):
        self.contatos = {}

    def adicionar_contato(self):
        """Adiciona um novo contato na agenda através de entrada de dados do usuário."""
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        email = input("Digite o email do contato: ")
        
        if nome in self.contatos:
            print("Contato já existe.")
        else:
            self.contatos[nome] = {'telefone': telefone, 'email': email, 'favorito': False}
            print(f"Contato {nome} adicionado com sucesso.")

    def editar_contato(self):
        """Edita as informações de um contato existente através de entrada de dados do usuário."""
        nome = input("Digite o nome do contato a ser editado: ")
        
        if nome in self.contatos:
            telefone = input("Digite o novo telefone do contato (ou pressione Enter para manter o atual): ")
            email = input("Digite o novo email do contato (ou pressione Enter para manter o atual): ")
            
            if telefone:
                self.contatos[nome]['telefone'] = telefone
            if email:
                self.contatos[nome]['email'] = email
            print(f"Contato {nome} editado com sucesso.")
        else:
            print("Contato não encontrado.")

    def deletar_contato(self):
        """Remove um contato da agenda através de entrada de dados do usuário."""
        nome = input("Digite o nome do contato a ser deletado: ")
        
        if nome in self.contatos:
            del self.contatos[nome]
            print(f"Contato {nome} deletado com sucesso.")
        else:
            print("Contato não encontrado.")

    def marcar_favorito(self):
        """Marca ou desmarca um contato como favorito através de entrada de dados do usuário."""
        nome = input("Digite o nome do contato a ser marcado/desmarcado como favorito: ")
        
        if nome in self.contatos:
            self.contatos[nome]['favorito'] = not self.contatos[nome]['favorito']
            status = "favorito" if self.contatos[nome]['favorito'] else "não favorito"
            print(f"Contato {nome} marcado como {status}.")
        else:
            print("Contato não encontrado.")

    def exibir_contatos(self):
        """Exibe todos os contatos na agenda."""
        if self.contatos:
            print("\n--- Lista de Contatos ---")
            for nome, info in self.contatos.items():
                favorito = " (Favorito)" if info['favorito'] else ""
                print(f"Nome: {nome} | Telefone: {info['telefone']} | Email: {info['email']}{favorito}")
        else:
            print("Agenda vazia.")

def menu():
    agenda = Agenda()
    while True:
        print("\n--- Menu da Agenda ---")
        print("1. Adicionar Contato")
        print("2. Editar Contato")
        print("3. Deletar Contato")
        print("4. Marcar/Desmarcar Favorito")
        print("5. Exibir Contatos")
        print("6. Sair")
        
        opcao = input("Escolha uma opção: ")
        
        if opcao == '1':
            agenda.adicionar_contato()
        elif opcao == '2':
            agenda.editar_contato()
        elif opcao == '3':
            agenda.deletar_contato()
        elif opcao == '4':
            agenda.marcar_favorito()
        elif opcao == '5':
            agenda.exibir_contatos()
        elif opcao == '6':
            print("Saindo da agenda...")
            break
        else:
            print("Opção inválida! Tente novamente.")

# Executa o menu da agenda
menu()
