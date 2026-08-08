quantidade_de_notas = 4

notas = []
for i in range(quantidade_de_notas):
    while True:
            nota = float(input(f"Digite a nota {i + 1} (0-10): "))
            if 0 <= nota <= 10:
                notas.append(nota)
                break
            else:
                print("Nota errada. Digite uma nota entre 0 e 10.")


soma = 0
for nota in notas:
    soma += nota

    media = soma / quantidade_de_notas

    if media >= 7:
        classificacao = "desempenho satisfatório"
    elif 5 <= media < 7:
        classificacao = "desempenho insatisfatório"
    else:
        classificacao = "desempenho ruim"

print(f"A média das notas é: {media:.2f}")
print(f"A classificação do desempenho é: {classificacao}")
