### Vendas da Cantina — Dia Campeão e Dias Acima da Média ###

vendas=[]
soma=0
maior=0
x=1
acima=[]
y=0
for i in range(0,5):
    dia=float(input(f'Vendas do dia {x}: R$ '))
    x+=1
    vendas.append(dia)
    soma+=dia

    if dia>maior:
        maior=dia
        data=x
media=soma/len(vendas)
for dia in vendas:
    if dia>=media:
        y+=1



print(f"Total da semana: R$ {soma:.2f} \nMédia diária: R$ {media:.2f}\nDia campeão: Dia {data} (valor de venda: R$ {maior:.2f})\nDias acima da média: {y}")
    

