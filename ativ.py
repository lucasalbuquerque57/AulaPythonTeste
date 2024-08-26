def saudacao():
    print("Olá, mundo!")

saudacao()

def saudacao_personalizada(name):
    print("Olá, ", name, "!")

def soma(a, b):
    resultado = a + b
    return resultado

total = soma(3, 5)
print(total)


def somar(x, y):
    return x+y

def subtrair(x, y):
    return x-y

def multiplicar(x, y):
    return x*y

def dividir(x, y):
    if y==0:
        return "Erro: Divisão por zero!"
    else:
        return x/y