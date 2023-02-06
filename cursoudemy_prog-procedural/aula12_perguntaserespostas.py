# sisteminha de perguntas e respotas utilizando python

asks = {
    'Pergunta 1': {
        'pergunta':'Quanto é 2+2?',
        'respostas': {
            'a': '1',
            'b': '4',
            'c': '6',
        },
        'resposta_certa': 'b'
    },
    'Pergunta 2': {
        'pergunta':'Qual a capital do Brasil?',
        'respostas': {
            'a': 'São Paulo',
            'b': 'Rio de Janeiro',
            'c': 'Brasília',
        },
        'resposta_certa': 'c'
    },
    'Pergunta 3': {
        'pergunta':'Por que há uma discussão se vírus são ou não uma forma de vida?',
        'respostas': {
            'a': 'Porque virus é virus',
            'b': 'Porque deus quis',
            'c': 'Porque nao possui celulas',
        },
        'resposta_certa': 'c'
    },
    'Pergunta 4': {
        'pergunta':'Que dia é o carnaval?',
        'respostas': {
            'a': 'Essa porra é dias aleatórias de fevereiro, mas geralmente dia 21',
            'b': '1 de janeiros',
            'c': '25 de dezembro',
        },
        'resposta_certa': 'a'
    },
}

right_answers = 0
for ask_id, ask_value in asks.items():
    print(f'\n{ask_id}: {ask_value["pergunta"]}')

    print('Escolha uma opcao abaixo: ')
    for answer_key, answer_value in ask_value['respostas'].items():
        print(f'[{answer_key}]: {answer_value}')

    chosen_answer = input('Sua resposta: ')

    if chosen_answer == ask_value['resposta_certa']:
        print('Parabéns, vc sabe algo básico')
        right_answers += 1
    else:
        print('Você é idiota ou é só burro mesmo?')

amount_asks = len(asks)
hit_percent = right_answers / amount_asks * 100
print(f'Vocẽ acertou {right_answers} respostas')
print(f'A porcentagem de acerto foi de {hit_percent}%')
