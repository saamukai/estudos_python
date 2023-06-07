
# funcoa que gera um bloco de codigo em html
def tag_bloco(conteudo, *args, classe='sucess', inline=False):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args)
    return f'<{tag} class="{classe}">{html}</{tag}>'


# função que gera uma lista em html
def tag_lista(*itens):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    return f'<ul>{lista}</ul>'


if __name__=='__main__':
    print(tag_bloco(tag_lista, 'Sábado', 'Domingo', classe='fds'))
