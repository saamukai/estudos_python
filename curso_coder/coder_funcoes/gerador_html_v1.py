def tag_bloco(texto, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    return f'<{tag} class="{classe}">{texto}</{tag}>'


if __name__ == '__main__':
    # Testes (assertions)
    print(tag_bloco('alguem te pergunto comé  q foi seu dia'))
    print(tag_bloco('agora eu sei exatamente como andar de skate', 'xorão'))
    print(tag_bloco('Cheia de mania, toda dengosa', 'Raça', True))
    print(tag_bloco(inline=True, texto='Trocando parametros de posição'))
    print(tag_bloco('Falha', classe="errror"))
