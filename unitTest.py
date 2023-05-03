def test_sum():
    # Cria uma lista com os números 5, 10 e 20
    lista = [5, 10, 20]

    # Executa a função sum utilizando a lista como argumento
    resultado = sum(lista)

    # Verifica se o resultado é igual a 35
    if resultado == 35:
        print("Resultado igual a 35")
    else:
        print("Diferente de 35")

print(test_sum())