print ("BEM VINDO AO CALCULA MÉDIA:")

nota_1 = float(input("Digite a nota do seu primeiro bimestre: "))
nota_2 = float(input("Digite a nota do seu segundo bimestre: "))
nota_3 = float(input("Digite a nota do seu terceiro bimestre: "))
nota_4 = float(input("Digite a nota do seu quarto bimestre: "))

media = (nota_1 + nota_2 + nota_3 + nota_4)/4

if media >= 7.0 :
    print(f"A sua nota foi {media}! Vc foi aprovado(a) ✅")

elif media >= 5.0 and media < 6.9:
    print(f"A sua nota foi {media}! Vc foi está de Recuperação ⚠️")

elif media < 5.0:
    print(f"A sua nota foi {media}! Vc foi Reprovado(a) ❌")