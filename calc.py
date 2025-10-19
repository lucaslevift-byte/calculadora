# Função para calcular (adiciona flexibilidade para o futuro)
def calcular():
    # Mensagem de boas-vindas e opções
    print("Selecione a operação:")
    print("1 - Adição (+)")
    print("2 - Subtração (-)")
    print("3 - Multiplicação (*)")
    print("4 - Divisão (/)")

    # Pede a escolha da operação
    operacao = input("Digite o número da operação (1/2/3/4): ")

    # Pede os dois números. Usamos float para aceitar números com vírgula.
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Entrada inválida. Por favor, digite apenas números.")
        return # Sai da função se a entrada não for um número

    # Verifica a escolha e realiza o cálculo
    if operacao == '1':
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    
    elif operacao == '2':
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    
    elif operacao == '3':
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    
    elif operacao == '4':
        # Evita a divisão por zero
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Erro! Divisão por zero não é permitida.")
    
    else:
        print("Opção de operação inválida.")

# Chama a função para iniciar a calculadora
calcular()