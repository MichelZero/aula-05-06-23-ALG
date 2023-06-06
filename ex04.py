#
# # 4.	Em linguagem Python, escreva um programa 
# que leia um número inteiro e calcule a soma de
# todos os divisores desse número, com exceção 
# dele próprio. Ex. a soma dos divisores do
# número 66 é 1 + 2 + 3 + 6 + 11 + 22 + 33 = 78

# numero % valor == 0
n = int(input("informe um número: "))
somatodos = 0
for i in range(1,n):
  if n % i == 0:
    somatodos += i
    
print(f"a soma foi {somatodos}")
