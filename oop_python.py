from os import getlogin


class Funcionario:
    def __init__(self, nome, cpf, cargo):
        self.nome = nome
        self.cpf = cpf
        self._cargo = cargo

    def __str__(self):
        print('-' * 42)
        return f'nome: {self.nome}\ncpf: {self.cpf}\ncargo: {self._cargo}'

    @property
    def cargo(self):
        return self._cargo

    @cargo.setter
    def cargo(self, cargo):
        self._cargo = cargo


class Gerente(Funcionario):
    def __init__(self, nome, cpf, cargo, id_especial):
        super().__init__(nome, cpf, cargo)
        self.__id_especial = id_especial

    @property
    def id_especial(self):
        return self.__id_especial

    @id_especial.setter
    def id_especial(self, id_especial):
        self.__id_especial = id_especial

    def __str__(self):
        print('-' * 42)
        return f'nome: {self.nome}\ncpf: {self.cpf}\ncargo: {self.cargo}\nId: {self.id_especial}'


class FuncionarioComum(Funcionario):
    def __init__(self, nome, cpf, cargo, apelido):
        super().__init__(nome, cpf, cargo)
        self._apelido = apelido

    def __str__(self):
        print('-'*42)
        return f'nome: {self.nome}\ncpf: {self.cpf}\ncargo: {self.cargo}\napelido: {self.apelido}'

    @property
    def apelido(self):
        return self._apelido

    @apelido.setter
    def apelido(self, apelido):
        self._apelido = apelido


class Departamento:
    def __init__(self, nome, funcionarios, gerente):
        self.nome = nome
        self.funcionarios = funcionarios
        self.__gerente = gerente

    def __getitem__(self, item):
        return self.funcionarios[item]

    @property
    def gerente(self):
        return self.__gerente

    @gerente.setter
    def gerente(self, gerente):
        self.__gerente = gerente


def teste():
    print()
    print('***'*5 + ' Exercicio 1' + '***'*5)

    """ Criando classes para treinar Herança e Criando métodos especiais para usar polimorfismo """

    bob_esponja = FuncionarioComum('bob esponja', 1000, 'mestre cuca', 'bob')
    print(bob_esponja)

    lula_molusco = FuncionarioComum('lula molusco', 2000, 'caixa', 'lula')
    print(lula_molusco)

    seu_sirigueijo = Gerente('Sirigueijo', 22, 'chefe', 200)
    print(seu_sirigueijo)

    print()
    print('***'*5 + ' Exercicio 2' + '***'*5)

    """ Criando uma lista de Funcionarios e exibindo """
    departamento_da_cozinha = Departamento('cosinha', [bob_esponja, lula_molusco], seu_sirigueijo)
    print(f'Nome do Departamento: {departamento_da_cozinha.nome}\nGerente: {departamento_da_cozinha.gerente.nome}')

    for f in departamento_da_cozinha:
        print(f)

    print('-'*42)

    "BRINCANDO COM A LIB OS"
    print(f'SEU LOGIN: {getlogin().upper()}')  # DA O NOME DO DONO DO PC


if __name__ == '__main__':
    teste()
