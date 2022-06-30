#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#  a Tela Fica Responsavel de Exibir Informações!

import socket
import time
filaAtendidos = []

# ==================== Menu para Exibir =============================#
def MenuAtendidos(lista,numero,posicao):
    if len(lista) >= numero:
        return lista[posicao]
    else:
        return "Aguardando Proximos"

def MenuProximo(nome,lista):
    chamado1 = MenuAtendidos(lista,1,-1)
    chamado1 = f"✪ {chamado1:.<70}✪"
    chamado2 = MenuAtendidos(lista,2,-2)
    chamado2 = f"✪ {chamado2:.<70}✪"
    chamado3 = MenuAtendidos(lista,3,-3)
    chamado3 = f"✪ {chamado3:.<70}✪"
    chamado4 = MenuAtendidos(lista,4,-4)
    chamado4 = f"✪ {chamado4:.<70}✪"
    chamado5 = MenuAtendidos(lista,5,-5)
    chamado5 = f"✪ {chamado5:.<70}✪"
    prox = "PROXIMO"
    lent = int(len(nome)/2-2)
    lin1 = "✪"*(len(nome)+4)
    lin2 = "{}{}{}{}{}".format("✰"*lent," ",prox," ","✰"*lent)
    lin3 = "{}{}{}".format("✰ ",nome," ✰")
    lin4 = "{}".format("✪"*(len(nome)+4))
    lent = int(len(nome)/2-2)   
    print(f"""
{"-"*118}
| {"✰"*30} Já CHAMADOS {"✰"*31}|| -{"⇩"*10} ATENÇÂO {"⇩"*10}
| {chamado1:} ||  {lin1}
| {chamado2:} ||  {lin2}
| {chamado3:} ||  {lin3}
| {chamado4} ||  {lin4}
| {chamado5} ||  {lin1}
{"-"*118}
    """)

def save(lista,nome):
    hora = time.localtime()
    t = time.strftime("%H:%M:%S", hora)
    hora = f"->Hora:{t} data:{hora.tm_mday}/{hora.tm_mon}/{hora.tm_year}."
    lista.append(f"{nome} {hora}")
#=============== Totem ========================#
def totem_start():
    localip = "0.0.0.0"
    localport = 2024
    tamanhodamensagem = 1024
    continua_loop = True

    try:
        serverUDP = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        serverUDP.bind((localip, localport))
        print("Aguardando clientes.")
    except Exception as erro:
        print(f"erro de inicialização:{erro}")
        continua_loop = False


    while (continua_loop):
        try:
            msgRecebida = serverUDP.recvfrom(tamanhodamensagem)
            mensagem = msgRecebida[0].decode("utf-8")
            iprecebido = msgRecebida[1]
            #print(mensagem, iprecebido)
            if mensagem:
                save(filaAtendidos,mensagem)
                print("-"*len(mensagem)*4)
                MenuProximo(mensagem,filaAtendidos)
                serverUDP.sendto(str(f"{mensagem}, Foi chamado!").encode(), iprecebido)
            else:
                serverUDP.sendto(str("erro").encode(), iprecebido)

        except KeyboardInterrupt as ex:
            print(f"erro {ex}")        

        except Exception as ex:
            print(f"erro de execução:{str(ex)}")

    try:
        serverUDP.close()
    except:
        print(".")

def main():
    op = ""
    while op != "2":
        op = input("[1] Inicia, [2] Sair :")
        if op == "1":
            totem_start()

if __name__ == "__main__":
    main()