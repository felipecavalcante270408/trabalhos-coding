class SalaDeAula:
    def __init__(self, numero, capacidade, bloco):
        self.numero = numero
        self.capacidade = capacidade
        self.bloco = bloco

    def exibir_info(self):
        print(f"Sala: {self.numero} | Bloco: {self.bloco} | Capacidade: {self.capacidade}")

    def verificar_capacidade(self, quantidade):
        return quantidade <= self.capacidade


class Professor:
    def __init__(self, nome, cpf, disciplina):
        self.nome = nome
        self.cpf = cpf
        self.disciplina = disciplina
        self.escolas = []

    def lecionar(self):
        print(f"{self.nome} está lecionando {self.disciplina}.")

    def adicionar_escola(self, escola):
        if escola not in self.escolas:
            self.escolas.append(escola)

    def listar_escolas(self):
        for escola in self.escolas:
            print(f"- {escola.nome}")


class Escola:
    def __init__(self, nome, cnpj, endereco):
        self.nome = nome
        self.cnpj = cnpj
        self.endereco = endereco
        self.salas = []
        self.professores = []

    def adicionar_sala(self, numero, capacidade, bloco):
        # Composição
        sala = SalaDeAula(numero, capacidade, bloco)
        self.salas.append(sala)
        return sala

    def remover_sala(self, sala):
        if sala in self.salas:
            self.salas.remove(sala)

    def adicionar_professor(self, professor):
        # Associação
        if professor not in self.professores:
            self.professores.append(professor)
            professor.adicionar_escola(self)

    def listar_professores(self):
        for professor in self.professores:
            print(f"- {professor.nome} - {professor.disciplina}")


class Endereco:
    def __init__(self, rua, numero, bairro, cidade, cep):
        self.rua = rua
        self.numero = numero
        self.bairro = bairro
        self.cidade = cidade
        self.cep = cep

    def exibir_endereco(self):
        print(f"{self.rua}, {self.numero} - {self.bairro}, {self.cidade} - CEP: {self.cep}")

    def atualizar(self, rua, numero, bairro, cidade, cep):
        self.rua, self.numero = rua, numero
        self.bairro, self.cidade, self.cep = bairro, cidade, cep


class Aluno:
    def __init__(self, nome, matricula, curso, endereco):
        self.nome = nome
        self.matricula = matricula
        self.curso = curso
        # Agregação
        self.endereco = endereco

    def exibir_dados(self):
        print(f"Nome: {self.nome} | Matrícula: {self.matricula} | Curso: {self.curso}")
        self.endereco.exibir_endereco()

    def alterar_curso(self, novo_curso):
        self.curso = novo_curso

    def definir_endereco(self, endereco):
        self.endereco = endereco


if __name__ == "__main__":
    escola = Escola("Escola ADS", "12.345.678/0001-90", "Rua Principal, 100")
    sala = escola.adicionar_sala("101", 40, "A")

    professor = Professor("Carlos", "111.222.333-44", "Programação")
    escola.adicionar_professor(professor)

    endereco = Endereco("Rua das Flores", "25", "Centro", "Parnaíba", "64200-000")
    aluno = Aluno("João", "2026001", "Análise e Desenvolvimento de Sistemas", endereco)

    print("--- SALA ---")
    sala.exibir_info()
    print("\n--- PROFESSORES ---")
    escola.listar_professores()
    print("\n--- ALUNO ---")
    aluno.exibir_dados()
