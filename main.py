from helper.calc_helper import calc

resp = int(input("[1] - somar \n[2] - subtrair \n[3] - multiplicar \n[4] - dividir\n\n:"))
n1 = int(input("\nDigite um numero: "))
n2 = int(input("Digite outro numero: "))

calc(n1, n2, resp)

