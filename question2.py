
def receber_valor():
    print('Informe um valor inteiro positivo para verificar se ele faz parte da sequência de Fibonacci ')

    while True:
        try:
            valor = int(input(">> "))
            n = abs(valor) 
            if valor == n: 
                return n 
            else:
                print('Digite um número válido')
        except ValueError:
            print('Digite um número válido')


def pertence_fibonnacci(valor):
    ram = 0
    i = 1
    fibonnacci = 0
    while fibonnacci <= valor: 
        if valor == fibonnacci:
            return True
        fibonnacci = ram + i
        i = ram
        ram = fibonnacci
    return False
    

def main():
    valor = receber_valor()
    if pertence_fibonnacci(valor) == True:
        print(f"O número {valor} pertence a sequência de fibonnacci!!")
    else:
        print(f"O número {valor} não pertence a sequeência de fibonnacci!!")
    
main()