def ehSimetrica( matriz ):
    for i in range(3):
        for j in range(3):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


matriz = []
for i in range(3):
    matriz.append( input().split() )

if ehSimetrica(matriz):
    print("sim")
else:
    print("nao")








# matriz = []
# for i in range(3):
#     matriz.append( input().split() )

# simetrica = True
# for i in range(3):
#     for j in range(3):
#         # print(i,j,sep="",end=" ")
#         if i < j:
#             if matriz[i][j] != matriz[j][i]:
#                 simetrica = False
#                 break
#     # print()

# print(simetrica)
# if simetrica:
#     print("sim")
# else:
#     print("nao")

