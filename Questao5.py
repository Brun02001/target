# Recebe a string do usuário

string = input("Digite uma string: ")

# Inicializa a string invertida

string_invertida = ""

# Percorre a string original do final para o início, adicionando cada caractere à string invertida

for i in range(len(string)-1, -1, -1):

    string_invertida += string[i]

# Imprime a string invertida

print("A string invertida é:", string_invertida)

