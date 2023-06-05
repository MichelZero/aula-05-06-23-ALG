#
# autores:
# Michel Silva, Crsitiano
#
# data: 05/06/2023

# 1.	Faça um programa que simula uma calculadora 
# que aceita as seguintes operações: soma, subtração,
# divisão e # multiplicação. O programa inicia
# pedindo para o usuário escolher uma opção do menu:
# 1. Somar
# 2. Subtrair
# 3. Dividir
# 4. Multiplicar
# 5. Sair.
# Ao escolher a opção, o programa solicita os 
# dois números a serem operados (exceto se a opção 
# escolhida for a 5),
# efetua a operação, mostra o resultado na
# tela e volta para o menu para que o usuário 
# escolha outra opção.
#
# obs:  essa solução é sem estrutura de repetição

# criar menu
# 1. Somar
# 2. Subtrair
# 3. Dividir
# 4. Multiplicar
# 5. Sair.

print("#######################")
print("### calculadora     ###")
print("### 1 - Somar       ###")
print("### 2 - Subtrair    ###")
print("### 3 - Dividir     ###")
print("### 4 - Multiplicar ###")
print("### 5 - Sair        ###")
print("#######################")

# entrada de dados
opcao = int(input("informe uma opção (1..5): "))
if opcao <=0 or opcao >=6:
  print("opção invalida")
else:
  valor1 = int(input("informe o valor 1: "))
  valor2 = int(input("informe o valor 2: "))

# processamento
if opcao == 1:
  print(f"{valor1} + {valor2} = {valor1 + valor2}")
elif opcao == 2:
  resultado = valor1 - valor2
  print(f"{valor1} - {valor2} = {resultado}")
elif opcao == 5:
  print("Saindo......")

  
  