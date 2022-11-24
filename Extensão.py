# Programa que recebe as notas do aluno


print("Digite as notas do aluno de 0 até 10: ")


num1 = float( input("Nota 1 ") )
num2 = float( input("Nota 2 ") )
num3 = float( input("Nota 3 ") )

maior = num1

if (num2 > maior):
        maior = num2
if (num3 > maior):
        maior = num3


# Aqui ele mostra  a maior nota do aluno

print('Maior: ',maior)

menor = num1

if (num2 < menor):
        menor = num2
if (num3 < menor):
        menor = num3

# Aqui ele mostra a menor nota do aluno        
print('Menor: ',menor)



num4 = num1 + num2 + num3 
media = num4/3

# Aqui mostra a media do aluno
print(f"Media do aluno {media:.2f}")


# Aqui mostra se o aluno foi aprovado ou reprovado baseado na sua media
if media > 6:
    print("Aprovado")

if media < 6:
    print("Reprovado")