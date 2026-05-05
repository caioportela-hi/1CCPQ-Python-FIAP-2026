## DADO UM CONJNTO DE 4 NOMES, IMPRIMA TODAS AS DUPLAS POSSÍVEIS:

# nomes = ["José", "Caio", "Russi", "Tiago"]
#
# duplas = []
# for i in range(len(nomes)):
#     for j in range(i + 1, len(nomes)):
#         duplas.append((nomes[i], nomes[j]))
#
# print(duplas)

## RESPOSTA DO PROFESSOR:

nomes = ["Ana", "Maria", "Enzo", "Leo"]

for i in range(len(nomes)):
    for j in range(i+1, len(nomes)):
        print(nomes[i], nomes[j])