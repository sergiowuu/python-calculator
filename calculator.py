def calculator():
    print("Selecione a operação:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    # Solicita ao usuário que escolha uma operação
    choice = input("Digite o número da operação (1/2/3/4): ")

    # Solicita ao usuário que insira dois números
    try:
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")
        return

    # Define as funções para cada operação
    def add(x, y):
        return x + y

    def subtract(x, y):
        return x - y

    def multiply(x, y):
        return x * y

    def divide(x, y):
        return x / y if y != 0 else "Erro: Divisão por zero"

    # Define as operações em um dicionário
    operations = {
        "1": add,
        "2": subtract,
        "3": multiply,
        "4": divide
    }

    # Obtém a operação correspondente e executa
    operation = operations.get(choice)
    if operation:
        result = operation(num1, num2)
    else:
        result = "Operação inválida"

    print(f"Resultado: {result}")

if __name__ == "__main__":
    calculator()