from datetime import datetime


class Projeto:
    def __init__(self, nome):
        self.nome = nome
        self.tasks = []


    def __iter__(self):
        return self.tasks.__iter__()

    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefas pendentes)'

    def add(self, descricao):
        self.tasks.append(Tarefa(descricao))

    def pendentes(self):
        return [task for task in self.tasks if not task.feito]

    def procurar(self, descricao):
        return [task for task in self.tasks
                if task.descricao == descricao][0]


class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def __str__(self):
        return f'{self.descricao} {("(CONCLUÍDA)" if self.feito else "")}'

    def concluir(self):
        self.feito = True

    def reabrir(self):
        self.feito = False


def main():
    estudos = Projeto('Estudos')
    estudos.add('Estudar python')
    estudos.add('Estudar Redes')
    estudos.add('Estudar Matemática')
    print(estudos)

    estudos.procurar('Estudar python').concluir()
    [print(f' - {task}') for task in estudos]
    print(f'\n{estudos}')

    mercado = Projeto('Compra mercado')
    mercado.add('Frutas Secas')
    mercado.add('Carne')
    mercado.add('Tomate')

    print(f'\n{mercado}')

if __name__ == '__main__':
    main()
