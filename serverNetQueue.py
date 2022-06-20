#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import socket

#=================================== NET QUEUECODE ======================================
fila = [
    {"Ficha 1": "João"},
    {"Ficha 2": "Henrique"},
    {"Ficha 3": "joao pedro"},
    {"Ficha 4": "Meruem"},
    {"Ficha 5": "Light"},
    {"Ficha 6": "Gustavo"},
    ]

chamados = []

def proximoDaFila(ficha):
    return (ficha[0],ficha[-1])



def deletaPrimeiro(dicionario):
    ultimo = str(proximoDaFila(fila)[1].keys())
    ultimo = ultimo[12:-3]
    if len(dicionario) == 1 or len(dicionario) == 0:
        dicionario.append({ultimo: "-------"})    
    dicionario.pop(0)

def Adicionar(Dicionario,ultimodafila,Nome):
    fist = str(proximoDaFila(Dicionario)[0].items())
    fist = fist[25:-4]
    numficha = ultimodafila
    num = str(numficha.keys())
    num = int(num[18:-3])+1
    prox = "Ficha "+str(num)
    Dicionario.append({prox:Nome})
    if fist == "-------":
        Dicionario.pop(0)

def ultimomaisUm(ultimo):
    numficha = ultimo
    num = str(numficha.keys())
    num = int(num[18:-3])+1
    prox = "Ficha "+str(num)
    return prox

#====================================== SERVER ====================================
def print_menu():
    print(20*'*')
    print('1 - Iniciar o servidor')
    print('2 - Sair')
    print(20*'*')

def start_server():
    localIP = "0.0.0.0"
    localPort = 2022
    bufferSize = 1024
    continue_loop = True
    try:
        # Create a datagram socket
        UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
        # Bind to address and ip
        UDPServerSocket.bind((localIP, localPort))
        print("Server waiting for data... (CTRL+C to Stop)")
    except Exception as ex:
        print("Startup error: {}".format(ex))
        continue_loop = False

        
    while (continue_loop):
        try:
            # Listen for incoming datagrams
            bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
            message = bytesAddressPair[0].decode('utf-8')
            address = bytesAddressPair[1]
            print('Message from {}: {}'.format(address, message))
            if message == "1":
                UDPServerSocket.sendto(str(fila).encode(), address)
            elif message == "2":
                prox = ultimomaisUm(proximoDaFila(fila)[1])
                UDPServerSocket.sendto(str(prox).encode(), address)
            elif message[0] == "ƃ":
                Adicionar(fila,proximoDaFila(fila)[1],message[1:])
                UDPServerSocket.sendto(str("Cadastrado Com Sucesso!").encode(), address)
            elif message == "3":
                prox = str((proximoDaFila(fila)[0]))
                prox = prox[2:-2].replace("\'","")
                UDPServerSocket.sendto(str(prox).encode(), address)
                chamados.append(fila[0])
                deletaPrimeiro(fila)
            elif message == "99":
                UDPServerSocket.sendto(str(chamados).encode(), address)
            else:
                UDPServerSocket.sendto(str("erro ?").encode(), address)

        except KeyboardInterrupt as ex:
            print('Execução cancelada')
            continue_loop = False
        except Exception as ex:
            print('Erro de execução: {}'.format(str(ex)))

    # Release socket
    try:
        UDPServerSocket.close()
    except:
        print('.')


def main():
    op = ''
    while op != '2':
        print_menu()
        op = input('Digite a opção: ')
        print(op)
        if op == '1':
            start_server()

if __name__ == '__main__':
    main()