#!/usr/bin/env python
# -*- coding: utf-8 -*-


#===================================== Server Client ==================================================
import socket

def send_msg(msg,ipv4,porta):
    serverAddressPort = (ipv4, porta)
    bufferSize = 1024
    bytesToSend = str.encode(msg)
    msgFromServer = None
    try:
        # Create a UDP socket at client side
        UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

        # Send to server using created UDP socket
        UDPClientSocket.sendto(bytesToSend, serverAddressPort)
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msgFromServer = str(msgFromServer[0].decode('utf-8'))
    except WindowsError:
        pass
    except Exception as ex:
        print("Sending msg error: {}".format(ex))
    # Release socket
    try:
        UDPClientSocket.close()
    except:
        pass

    return msgFromServer

#======================================= MENUS =========================================
def Menu():
    print("""
[ 1 ] Lista Proximo
[ 2 ] chamar o proximo
[ 3 ] Sair
[ 99 ] Listar Atendidos
""")
def MenuVoltar():
    var = input("Digite ou aperte Enter para Continuar!")

def MenuProximo(nome):
    prox = "PROXIMO"
    lent = int(len(nome)/2-2)
    print("✪"*(len(nome)+4))
    print("✰"*lent, prox,"✰"*lent)
    print("✰",nome,"✰")
    print("✪"*(len(nome)+4))

def SIM_OU_NAO():
    while True:
        print("Deseja Chamar ?")
        print("[ Sim / Não ]")
        pergunta = input("Digite Aqui:").strip().upper()
        if pergunta in "SIM" and len(pergunta) == 3:
            return "SIM"
        elif pergunta in "NÃONAO" and len(pergunta) == 3:
            return "NÃO"
        else:
            while True:
                print("Resposta Incorreta,Tente Novamente!")
                break


#=============================================== MAIN CODE ======================================

def main():
    op = ''
    servidor = "192.168.1.103" #input("Digite seu IPV4:")
    while op != '3':
        Menu()
        op = input('Digite a opção: ')
        if op == "1":
            response = send_msg("1",servidor,2022)
            if response:
                print("♤ ♠ ♧  LISTA DE ESPERA ♤ ♠ ♧")
                fila = response[0:-1]
                fila = fila.replace("{"," ")
                fila = fila.replace(",","\n✰")
                fila = fila.replace("\'","")
                fila = fila.replace("}"," ✰")
                fila = fila.replace("[","✰ ")
                print(fila)
                MenuVoltar()
        elif op == "2":
            pergunta = SIM_OU_NAO()
            if pergunta == "SIM":
                send = send_msg("3",servidor,2022)
                if send:
                    if send[10:16] == "------":
                        print("Todos Já Foram Atendos Por favor Adicione novos cotatos")
                    else:
                        try:
                            enviar = send_msg(send,servidor,2024)
                            if enviar:
                                print(enviar)
                                MenuVoltar()
                        except:
                            MenuVoltar()
                            pass
        elif op == "99":
            send = send_msg("99",servidor,2022)
            if send:
                res = str(send[0:-2])
                res = res.replace("\'","")
                res = res.replace(",","\n")
                res = res.replace("{","")
                res = res.replace("}","")
                res = res.replace("["," ")
                print("Lista dos Chamados!")
                print(res)
                MenuVoltar()

if __name__ == '__main__':
    main()