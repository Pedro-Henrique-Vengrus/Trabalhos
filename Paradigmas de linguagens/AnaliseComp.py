def calculadora():
    print("Escolha a operação:")
    print("1 - Soma")
    print("2 - Divisão")
    print("3 - Multiplicação")
    print("4 - Divisão")

    operacao = int(input("Escolha uma operação(1-4): "))
    a = float(input("Digite o primeiro numero: "))
    b = float(input("Digite o segundo numero: "))

    match operacao:

        case 1:
            resultado = a + b
            return f"Soma: {round(resultado)}"
        
        case 2:
            resultado = a - b
            return f"Subtração: {round(resultado)}"
        
        case 3:
            if a == 0 or b == 0:
                return "Multiplicar número por zero é zero"
            resultado = a * b
            return f"Multplicação: {round(resultado)}"
            
        case 4:
            if b == 0:
                return "Não pode dividir por zero" 
            resultado = a / b
            return f"Divisão: {round(resultado)}"
        
        case _:
            return "Operação invalida!"
        
print(calculadora())
        