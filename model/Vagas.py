class Vagas:
    def __init__(self, titulo, descricao, empresa, link):
        self.titulo = titulo
        self.descricao = descricao
        self.empresa = empresa
        self.link = link

    def __str__(self):
        return f"Vaga de Estágio:\nTítulo: {self.titulo}\nDescrição: {self.descricao}\nNome da empresa: {self.empresa}\nLink: {self.link}"

    def to_dict(self):
        return{
            'Título': self.titulo,
            'Descricao': self.descricao,
            'Empresa': self.empresa,
            'Link': self.link
        }