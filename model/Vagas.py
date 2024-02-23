class Vagas:
    def __init__(self, titulo, descricao, requisitos, nome_empresa, bolsa_auxilio, modalidade, localizacao,  origem, link):
        self.titulo = titulo
        self.descricao = descricao
        self.requisitos = requisitos
        self.nome_empresa = nome_empresa
        self.bolsa_auxilio = bolsa_auxilio
        self.modalidade = modalidade
        self.localizacao = localizacao
        self.origem = origem
        self.link = link

    def __str__(self):
        return f"Vaga de Estágio:\nTítulo: {self.titulo}\nDescrição: {self.descricao}\nCompetências: {', '.join(self.requisitos)}\nNome da Empresa: {self.nome_empresa}\nBolsa Auxílio: R${self.bolsa_auxilio}\nModalidade: {self.modalidade}\nOutros Campos: {self.outros_campos}"
