dic = []

esc = input("a: ")
esc2 = input("b: ")
esc3 = input("c: ")

dic.append(esc)
dic.append(esc2)
dic.append(esc3)

print(dic)

remover = input("\nQual você deseja remover?: \n")

remover_int = int(remover)

dic.remove(dic[remover_int])

print(dic)