num1 = int(input("digite "))
num2 = int(input("digite "))
operacao = input("digite (+, -, *, /): ")

if operacao =='+':
    print(num1 + num2)
elif operacao == '-':
    print(num1 - num2)
elif operacao == '*':
    print(num1 * num2)
elif operacao == '/':
    print(num1 / num2)
else:
    print("operação inválida")

   
