def tag(tag, *args, **kwargs):
    if 'css' in kwargs:
        kwargs['class'] = kwargs.pop('css')

    atrs = ''.join(f'{atr}={atr_name}' for atr, atr_name in kwargs.items())
    conteudo = ''.join(args)
    return f'<{tag} {atrs}>{conteudo}</{tag}>'


if __name__ == '__main__':
    print(tag('p',
              tag('span', 'Curso de Python 3, por '),
              tag('strong', 'Juracy Filho', id='jf'),
              tag('span', ' e '),
              tag('strong', 'Leonardo Leitão', id='ll'),
              tag('span', '.'),
              css='alert')
          )
