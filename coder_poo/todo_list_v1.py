from datetime import datetime

class Tarefa:
    def __init__(self, descricao):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()

    def __str__(self):
        return f'{self.descricao} = {("CONCLUÍDA" if self.feito else "")}'

    def concluir(self):
        self.feito = True

    def reabrir(self):
        self.feito = False


def main():
    tasks = []
    tasks.append(Tarefa('Lavar louça'))
    tasks.append(Tarefa('Estudar Python'))
    tasks.append(Tarefa('Estudar Linux'))
    tasks.append(Tarefa('Estudar Redes'))

    # Concluir se a tarefa for -> Lavar louça
    [task.concluir() for task in tasks if task.descricao == 'Lavar louça']


if __name__ == '__main__':
    main()
