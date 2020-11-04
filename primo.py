def nprimo(n):
    divisores=[]
    for i in range(1, n+1):
        if n%i ==0:
            divisores.append(i)
    quantidade=len(divisores)
    if quantidade > 2:
        return print('Falso | %d não é primo'%(n))
    else:
        return print('Verdadeiro | %d é primo'%(n))
def main():
    numero=int(input('Digite um numero:'))
    nprimo(numero)
if __name__ == '__main__':
    main()