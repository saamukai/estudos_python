
## suponha q um sistema de login:
logged_user = False

if logged_user:
    msg = 'Usuário Logado.'
else:
    msg = 'Usuário precisa logar'

print(msg)

## pode ser simplificado utilizando ternário
msg = 'Usuario Logado.' if logged_user else 'Usuario precisa logar'

print(msg)
