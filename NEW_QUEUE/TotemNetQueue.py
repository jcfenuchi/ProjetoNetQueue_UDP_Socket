#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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


def MenuVoltar():
    var = input("Digite ou aperte Enter para Continuar!")

def Menu():
    print("""
[ 1 ] Adicinar ao Ultimo
[ 2 ] Sair
""")

def main():
    op = ''
    servidor = "192.168.1.103" #input("Digite seu IPV4:")
    while op != '2':
        Menu()
        op = input("Digite a opção:")
        if op == "1":
            send = send_msg("2",servidor,2022)
            if send:
                print(f"Proximo Sera -> {send}!")
                nome = input("Digite o Nome:").strip().title()
                eco = send_msg("ƃ"+nome,servidor,2022)                
                if eco:
                    print(eco)
                    MenuVoltar()

if __name__ == '__main__':
    main()