#
#
# autores:
# Michel Silva
# critiano
#
# data: 05/06/2023
#

# 2.	Em linguagem Python, elabore um programa 
# que leia n valores e mostre a soma de seus quadrados.
#
# usando o laço for
# entrada de dados
n = int(input("informe um valor n: "))

# quadrado de é n**2
# n=3
# range(1,4) = 1, 2, 3
# range(1,n+1) = 1, 2, 3
soma = 0
for maria in range(1,n+1):
  valor = int(input(f"informe um valor valor{maria}: "))
  soma = soma + valor **2
  
print(f"a soma total foi {soma}")