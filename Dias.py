anos = int(input("Quantos anos você tem?"))
meses =  int(input("Quantos meses se passaram desde o último aniversario?"))
dias =  int(input("Quantos dias se passaram desde o último mês apontado na resposta anterior?"))

totalDias = (anos * 365) + (meses * 30) + dias

print("Total de dias foi:")
print(totalDias)
