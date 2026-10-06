class Condutor:
    def __init__(self, nome, numero_cnh, categoria_cnh):
        self.nome = nome
        self.numero_cnh = numero_cnh
        self.categoria_cnh = categoria_cnh

    def validar_cnh(self):
        return bool(self.numero_cnh)

    def exibir_dados(self):
        print(f"Condutor: {self.nome}")
        print(f"CNH: {self.numero_cnh}")
        print(f"Categoria: {self.categoria_cnh}")


class ContratoLocacao:
    def __init__(self, data_inicio, data_termino, valor_total, status,
                 nome_condutor, numero_cnh, categoria_cnh):
        self.data_inicio = data_inicio
        self.data_termino = data_termino
        self.valor_total = valor_total
        self.status = status

        # Composição: Condutor é criado dentro do ContratoLocacao.
        self.condutor = Condutor(nome_condutor, numero_cnh, categoria_cnh)

    def calcular_total(self):
        return self.valor_total

    def finalizar_contrato(self):
        self.status = "finalizado"

    def exibir_contrato(self):
        print(f"Início: {self.data_inicio}")
        print(f"Término: {self.data_termino}")
        print(f"Valor total: R$ {self.valor_total:.2f}")
        print(f"Status: {self.status}")
        self.condutor.exibir_dados()


if __name__ == "__main__":
    contrato = ContratoLocacao(
        "05/10/2026", "10/10/2026", 750.00, "ativo",
        "João da Silva", "12345678900", "B"
    )

    print("--- CONTRATO DE LOCAÇÃO ---")
    contrato.exibir_contrato()

    contrato.finalizar_contrato()
    print(f"\nNovo status: {contrato.status}")
