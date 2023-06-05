#
#
# autores:
# Michel Silva
# critiano
#
# data: 05/06/2023
#
# 3.	Em linguagem Python, faça um programa que leia 
# 10 inteiros positivos, ignorando não positivos,
# e imprima sua média.
#
# entrada de dados
# range(10) ->0..9
# média = somatodos / quantidade de todos
somatodos = 0
for jose in range(5):  # 0 1 2 3 4 
  valor = int(input(f"informe o valor {jose}: "))
  if valor > 0:
    somatodos += valor # soma = soma + valor
  else:
    print(f"{valor} é invalido")
    jose = jose - 1
    
media = somatodos / 5

print(f"a média foi {media}")