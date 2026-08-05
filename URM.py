# função pra calcular o URM 
def calcular_1rm(peso, repeticoes):
    calculo = peso * (1 + repeticoes/30)
    return round(calculo, 2)

# 1. Recebendo os dados
peso_usuario = float(input("Digite o peso levantado (kg): "))
reps_usuario = int(input("Digite o número de repetições: "))
exercicio = input('Qual o exercício?: ')

# 2. Fazendo o cálculo
resultado_estimado = calcular_1rm(peso_usuario, reps_usuario)

# 3. Mostrando na tela
print(f'O peso estimado é de {resultado_estimado} kg')

# 4. Salvando no histórico
with open("meu_historico_1rm.txt", "a") as arquivo:
    linha = f"Levantou {peso_usuario} kg por {reps_usuario} repetições no exercício {exercicio}. O 1RM estimado foi {resultado_estimado} kg\n"
    arquivo.write(linha)