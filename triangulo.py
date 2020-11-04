a = int(input("Digite um valor"))
b = int(input("Digite um valor"))
c = int(input("Digite um valor"))

if a + b > c & a + c > b & b + c > a:
    Area = (a + b + c) / 2
    print("A área do trinangulo é,".format(Area))
    print("Forma um triangulo.")
else:
    print("Não forma triângulo algum.")