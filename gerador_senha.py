# import random
# import string

# def password_generator(password_length):
#     str_caracters = string.ascii_letters  # Contém letras minúsculas e maiúsculas
#     password = ''.join(random.choice(str_caracters) for _ in range(password_length))
#     return password

# # Solicita ao usuário o tamanho da senha
# password_length = int(input("Digite o tamanho da senha: "))
# password_created = password_generator(password_length)
# print("Senha gerada:", password_created)


import random
import string

# Funcao que gera senha aleatoria
# Utilizando a biblioteca Lib/string.py em https://docs.python.org/3/library/string.html
# É possível obter todos os caracteres como uma lista, facilitando iterar sobre a mesma com "random.choice"
def password_generator(password_length):
    str_caracters = string.ascii_letters  # Contém letras minúsculas e maiúsculas
    lista_caracters = []
    for str_caracter in range(password_length):
        lista_caracters.append(random.choice(str_caracters)) 
    password = ''.join(lista_caracters) #https://docs.python.org/pt-br/3/library/stdtypes.html#str.join com metodo join é possivel juntar os carcteres da lista em uma string
    return password #Retorna a senha aleatória

# Solicita ao usuário o tamanho da senha
password_length = int(input("Digite o tamanho da senha: "))
password_created = password_generator(password_length)
print("Senha gerada:", password_created)
