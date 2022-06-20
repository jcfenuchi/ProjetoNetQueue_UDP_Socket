

import time

lista = [
   "ficha 1 : Julio Cesar",
    "ficha 2 : brother",
    "ficha 3 : hello",
    "ficha 4 : teste",
    "ficha 5 : meme",
    "ficha 6 : teste2",
    "ficha 7 : Lukas"
    ]

def MenuAtendidos(lista,numero,posicao):
    if len(lista) >= numero:
        return lista[posicao]
    else:
        return "Aguardando Proximos"

def MenuProximo(nome):
    chamado1 = MenuAtendidos(lista,1,-1)
    chamado1 = f"✪ {chamado1:.<55}✪"
    chamado2 = MenuAtendidos(lista,2,-2)
    chamado2 = f"✪ {chamado2:.<55}✪"
    chamado3 = MenuAtendidos(lista,3,-3)
    chamado3 = f"✪ {chamado3:.<55}✪"
    chamado4 = MenuAtendidos(lista,4,-4)
    chamado4 = f"✪ {chamado4:.<55}✪"
    chamado5 = MenuAtendidos(lista,5,-5)
    chamado5 = f"✪ {chamado5:.<55}✪"
    prox = "PROXIMO"
    lent = int(len(nome)/2-2)
    lin1 = "✪"*(len(nome)+4)
    lin2 = "{}{}{}{}{}".format("✰"*lent," ",prox," ","✰"*lent)
    lin3 = "{}{}{}".format("✰ ",nome," ✰")
    lin4 = "{}".format("✪"*(len(nome)+4))
    lent = int(len(nome)/2-2)   
    print(f"""
{"-"*120}
| {"✰"*23} Já CHAMADOS {"✰"*23}|| -{"⇩"*20} ATENÇÂO {"⇩"*20}
| {chamado1:} ||  {lin1}
| {chamado2:} ||  {lin2}
| {chamado3:} ||  {lin3}
| {chamado4} ||  {lin4}
| {chamado5} ||
{"-"*120}
    """)

nome = "ficha 3 : Felipe Bruno"
MenuProximo(nome)