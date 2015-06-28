'''
Adventure Game
Copyright (c) 2015, William Alcântara Costa
All rights reserved.
- This code is licensed under the BSD 3-Clause License - check it on LICENSE.MD

---

Adventure Game (Jogo de aventura)
Copyright (c) 2015, William Alcântara Costa
Todos os direitos reservados.
- Este código está licensiado sob a Licença de três cláusulas BSD - leia mais em LICENSE.MD

'''

import random

# Limites do mapa
limiteX = 10
limiteY = 10

# Posição da chave
posChaveX = 0
posChaveY = 0

# Posição do portao de saída
posPortaoX = 0
posPortaoY = 0

# Posição da loja
posNPCX = 0
posNPCY = 0

def salvarPosicoes(objeto, tipo):
    global posChaveX, posChaveY, posPortaoX, posPortaoY, posNPCX, posNPCY
    if(objeto == 1 and tipo == 1):
        return posChaveX
    elif(objeto == 1 and tipo == 2):
        return posChaveY
    elif(objeto == 2 and tipo == 1):
        return posPortaoX
    elif(objeto == 2 and tipo == 2):
        return posPortaoY
    elif(objeto == 3 and tipo == 1):
        return posNPCX
    else:
        return posNPCY

def abrirPosicoes(chaveX, chaveY, portaoX, portaoY, NPCX, NPCY):
    global posChaveX, posChaveY, posPortaoX, posPortaoY, posNPCX, posNPCY
    posChaveX = chaveX
    posChaveY = chaveY
    posPortaoX = portaoX
    posPortaoY = portaoY
    posNPCX = NPCX
    posNPCY = NPCY

def sortearPosicaoChave():
    global posChaveX, posChaveY
    posChaveX = random.randint(1, limiteX)
    posChaveY = random.randint(1, limiteY)

def sortearPosicaoPortao():
    global posPortaoX, posPortaoY, limiteX, limiteY, posChaveX, posChaveY
    direcao = random.randint(1, 4)
    if(direcao == 1): # norte
        posPortaoX = random.randint(1, limiteX)
        while(posPortaoX == posChaveX):
            posPortaoX = random.randint(1, limiteX)
        posPortaoY = 1
    elif(direcao == 2): # sul
        posPortaoX = random.randint(1, limiteX)
        while(posPortaoX == posChaveX):
            posPortaoX = random.randint(1, limiteX)
        posPortaoY = limiteY
    elif(direcao == 3): # leste
        posPortaoX = limiteX
        posPortaoY = random.randint(1, limiteY)
        while(posPortaoY == posChaveY):
            posPortaoY = random.randint(1, limiteY)
    else: # oeste
        posPortaoX = 1
        posPortaoY = random.randint(1, limiteY)
        while(posPortaoY == posChaveY):
            posPortaoY = random.randint(1, limiteY)

def sortearPosicaoNPC():
    global posNPCX, posNPCY, limiteX, limiteY, posPortaoX, posPortaoY
    posNPCX = random.randint(1, limiteX)
    while(posNPCX == posPortaoX):
        posNPCX = random.randint(1, limiteX)
    posNPCY = random.randint(1, limiteY)
    while(posNPCY == posPortaoY):
        posNPCY = random.randint(1, limiteY)

def lerPosicaoAtual(X, Y):
    global posChaveX, posChaveY, posPortaoX, posPortaoY, posNPCX, posNPCY
    if(X == posPortaoX and Y == posPortaoY):
        mensagem = "portão"
    elif(X == posNPCX and Y == posNPCY):
        mensagem = "loja"
    else:
        mensagem = "terra"
    if(X == posChaveX and Y == posChaveY):
        mensagem = mensagem + " (chave no chão)"
    return mensagem

def moverChave():
    global posChaveX, limiteX
    posChaveX = limiteX+1
        
def imprimirPosicoes():
    global posChaveX, posChaveY, posPortaoX, posPortaoY, posNPCX, posNPCY
    print("Chave: X" + str(posChaveX) + " / Y" + str(posChaveY))
    print("Portão: X" + str(posPortaoX) + " / Y" + str(posPortaoY))
    print("Loja: X" + str(posNPCX) + " / Y" + str(posNPCY))
