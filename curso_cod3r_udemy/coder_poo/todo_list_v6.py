from datetime import datetime, timedelta


class Projeto:

    # Construtor, criar projeto.
    def __init__(self, nome):
        self.nome = nome
        self.tarefas = []

    # Iterar sobre tarefas sem chamar (projetos.tarefas)
    # Tornando projetos iteráveis
    def __iter__(self):
        return self.tarefas.__iter__()

    # Print nome projeto + projetos pendentes
    def __str__(self):
        return f'{self.nome} ({len(self.pendentes())} tarefa(s) pendente(s))'

    # MÉTODOS PRIVADOS
    def _add_tarefa(self, tarefa, **kwargs):
        self.tarefas.append(tarefa)

    def _add_nova_tarefa(self, descricao, **kwargs):
        self.tarefas.append(Tarefa(descricao, kwargs.get('Vencimento', None)))

    # Chama metodo privado dependendo do tipo da tarefa
    def add(self, tarefa, vencimento=None, **kwargs):
        funcao_escolhida = self._add_tarefa if isinstance(tarefa, Tarefa) \
            else self._add_nova_tarefa
        kwargs['vencimento'] = vencimento
        funcao_escolhida(tarefa, **kwargs)

    # retornar tarefas pendentes
    def pendentes(self):
        return [tarefa for tarefa in self.tarefas if not tarefa.feito]

    # procurar uma tarefa na lista de tarefas
    def procurar(self, descricao):
        # Possível IndexError
        return [tarefa for tarefa in self.tarefas
                if tarefa.descricao == descricao][0]


class Tarefa:
    # Cosntrutor de tarefa
    def __init__(self, descricao, vencimento=None):
        self.descricao = descricao
        self.feito = False
        self.criacao = datetime.now()
        self.vencimento = vencimento

    # Printar tarefas e status
    def __str__(self):
        status = []
        if self.feito:
            status.append('(Concluída)')
        elif self.vencimento:
            if datetime.now() > self.vencimento:
                status.append('(Vencida)')
            else:
                dias = (self.vencimento - datetime.now()).days
                status.append(f'(Vence em {dias} dias)')

        return f'{self.descricao} ' + ' '.join(status)

    # Concluir tarefa
    def concluir(self):
        self.feito = True


class TarefaRecorrente(Tarefa):  # Tarefa reconrrente, se repete
    # construir tarefa reconte, recebe como herança Tarefa
    def __init__(self, descricao, vencimento, dias=7):
        super().__init__(descricao, vencimento)
        self.dias = dias

    # concluir tarefa e adiciona novo vencimento para que se repita
    def concluir(self):
        super().concluir()
        novo_vencimento = datetime.now() + timedelta(days=self.dias, minutes=2)
        return TarefaRecorrente(self.descricao, novo_vencimento, self.dias)


if __name__ == '__main__':
    casa = Projeto('Tarefas de Casa')
    mercado = Projeto('Compras Mercado')

    casa.add(TarefaRecorrente('Trocar Lençóis', datetime.now() + timedelta(7)))
    casa.add(TarefaRecorrente('Lavar louça', datetime.now() + timedelta(2), 1))
    casa.add('Limpar chão')

    mercado.add(TarefaRecorrente('Verduras', datetime.now() + timedelta(2), 7))
    mercado.add('Produtos de Limpeza')
    mercado.add('Arroz')

    print(f'\n{casa}')
    for tarefa in casa:
        print(f'- {tarefa}')

    print(f'\n{mercado}')
    for tarefa in mercado:
        print(f'- {tarefa}')
