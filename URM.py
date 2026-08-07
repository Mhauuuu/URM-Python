
def calcular_1rm(peso, repeticoes):
    calculo = peso * (1 + repeticoes/30)
    return round(calculo, 2)


def gerar_tabela(um_rm):
    aquecimento = round(um_rm * 0.50, 2)
    hipertrofia = round(um_rm * 0.75, 2)
    forca = round(um_rm * 0.90, 2)
    
    print("\n--- TABELA DE CARGAS RECOMENDADAS ---")
    print(f"Aquecimento (50% do 1RM): {aquecimento} kg")
    print(f"Foco em Hipertrofia (75% do 1RM): {hipertrofia} kg")
    print(f"Foco em Força Pura (90% do 1RM): {forca} kg")
    print("-------------------------------------")

peso_usuario = float(input("Digite o peso levantado (kg): "))
reps_usuario = int(input("Digite o número de repetições: "))
exercicio = input('Qual o exercício?: ')

resultado_estimado = calcular_1rm(peso_usuario, reps_usuario)

print(f'\nNo exercício {exercicio}, o seu 1RM estimado é de {resultado_estimado} kg')


gerar_tabela(resultado_estimado)


with open("meu_historico_1rm.txt", "a") as arquivo:
    linha = f"Levantou {peso_usuario} kg por {reps_usuario} repetições no exercício {exercicio}. O 1RM estimado foi {resultado_estimado} kg\n"
    arquivo.write(linha)