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

nome = "inimigobasico"
HP = 50
maxHP = 50
armadura = 2 # reduz um pouco o dano causado
atkMin = 10
atkMax = 13
velocidade = 5 # aumenta as chances de esquivar de um ataque
forca = 3 # aumenta as chances de criticos
expGanhaMin = 0 # mínimo de experiência que o jogador ganhará
expGanhaMax = 0 # náximo de experiência que o jogador ganhará

def setarInimigo(nivelJogador):
    global nome, HP, maxHP, armadura, atkMin, atkMax, velocidade, forca, expGanhaMin, expGanhaMax
    inimigo = random.randint(1, 3)
    if(nivelJogador < 5):
        if(inimigo == 1):
            nome = "Esqueleto"
            HP = 35
            maxHP = 35
            armadura = 1
            atkMin = 5
            atkMax = 8
            velocidade = 3
            forca = 1
            expGanhaMin = 5
            expGanhaMax = 8
        elif(inimigo == 2):
            nome = "Demon"
            HP = 40
            maxHP = 40
            armadura = 2
            atkMin = 3
            atkMax = 6
            velocidade = 2
            forca = 2
            expGanhaMin = 9
            expGanhaMax = 13
        elif(inimigo == 3):
            nome = "Troll"
            HP = 28
            maxHP = 28
            armadura = 2
            atkMin = 3
            atkMax = 6
            velocidade = 6
            forca = 2
            expGanhaMin = 9
            expGanhaMax = 12
    else: # Jogador nivel 5 ou mais
        if(inimigo == 1):
            nome = "Esqueleto com armadura"
            HP = 60
            maxHP = 60
            armadura = 3
            atkMin = 8
            atkMax = 11
            velocidade = 4
            forca = 3
            expGanhaMin = 11
            expGanhaMax = 15
        elif(inimigo == 2):
            nome = "Devil"
            HP = 62
            maxHP = 62
            armadura = 4
            atkMin = 7
            atkMax = 10
            velocidade = 3
            forca = 3
            expGanhaMin = 13
            expGanhaMax = 17
        elif(inimigo == 3):
            nome = "Orc"
            HP = 80
            maxHP = 80
            armadura = 6
            atkMin = 10
            atkMax = 15
            velocidade = 6
            forca = 5
            expGanhaMin = 22
            expGanhaMax = 25

def atacar():
    global atkMin, atkMax, forca
    isCritico = random.randint(1, 10-forca) # testa a chance de um ataque critico
    ataque = random.randint(atkMin, atkMax) # gera o valor de um ataque
    if(isCritico != 1): # se o ataque NÃO for critico
        return ataque
    else: # se for crítico
        return ataque * 2 # duplica o ataque

def receberDano(quantidadeDano):
    global HP, armadura, velocidade
    chanceEsquiva = random.randint(1, 15-velocidade)
    if(chanceEsquiva != 1): # se NÃO esquivar o ataque
        HP = HP - (quantidadeDano - (int(armadura * 0.6)))
        print("Você causou " + str(quantidadeDano - (int(armadura * 0.6))) + " de dano!")
    else:
        print("O inimigo esquivou seu golpe!")

def retornarExpGanha():
    global expGanhaMin, expGanhaMax
    return random.randint(expGanhaMin, expGanhaMax)

def chanceDroparPocao():
    return random.randint(1, 5)
