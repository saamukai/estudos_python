
# atributos pre definidos para serem aceitos nas funções
bloco_atrs = ('bloco_accesskey', 'bloco_id')
ul_atrs = ('ul_id', 'ul_style')

# funcao  que filtra os atributos
def filtrar_atrs(informados, suportados):
    return ' '.join(f'{key.split("_")[-1]}="{value}"'
                    for key, value in informados.items()
                    if key in suportados)


# funcoa que gera um bloco de codigo em html
def tag_bloco(conteudo, *args, classe='sucess', inline=False, **kwargs):
    tag = 'span' if inline else 'div'
    html = conteudo if not callable(conteudo) else conteudo(*args, **kwargs)
    atributos = filtrar_atrs(kwargs, bloco_atrs)
    return f'<{tag} {atributos} class="{classe}">{html}</{tag}>'


# função que gera uma lista em html
def tag_lista(*itens, **kwargs):
    lista = ''.join(f'<li>{item}</li>' for item in itens)
    atributos = filtrar_atrs(kwargs, ul_atrs)
    return f'<ul {atributos}>{lista}</ul>'


if __name__ == '__main__':
    print(tag_bloco(tag_lista, 'item1', 'item2', classe='info',
                    bloco_accesskey='m', bloco_id='conteudo', ul_id='lista'))
