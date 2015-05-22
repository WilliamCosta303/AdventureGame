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

import random, base64 # invoca o random para selecionar numeros

nome = "heroibasico"
HP = 50
maxHP = 50
armadura = 2 # reduz um pouco o dano causado
atkMin = 10
atkMax = 13
velocidade = 5 # aumenta as chances de esquivar de um ataque
forca = 3 # aumenta as chances de criticos
exp = 0 # experiência
expNext = 40 # experiência necessária para subir level
level = 1 # level

# Itens
item1Quant = 0
item1Tipo = 0
item2Quant = 0
item2Tipo = 0
item3Quant = 0
item3Tipo = 0
item4Quant = 0
item4Tipo = 0

#posições X e Y
posX = 0
posY = 0

#posições do mapa salvas
chaveX = 0
chaveY = 0
portaoX = 0
portaoY = 0

def setarPosicaoInicial(limiteX, limiteY):
    global posX, posY
    posX = random.randint(1, limiteX)
    posY = random.randint(1, limiteY)

def atacar():
    global atkMin, atkMax, forca # invoca as variaveis globais
    isCritico = random.randint(1, 10-forca) # testa a chance de um ataque critico
    ataque = random.randint(atkMin, atkMax) # gera o valor de um ataque
    if(isCritico != 1): # se o ataque NÃO for critico
        return ataque
    else: # se for crítico
        return ataque * 2 # duplica o valor

def receberDano(quantidadeDano):
    global HP, armadura, velocidade
    chanceEsquiva = random.randint(1, 15-velocidade)
    if(chanceEsquiva != 1): # se NÃO esquivar o ataque
        HP = HP - (quantidadeDano - (int(armadura * 0.6)))
        print(str(quantidadeDano - (int(armadura * 0.6))) + " recebidos de dano!")
    else:
        print("Se esquivou do golpe!")
        
def subirNivel():
    global exp, expNext, level, HP, maxHP, armadura, atkMin, atkMax, velocidade, forca
    if(exp >= expNext):
        HP = HP + 5
        maxHP = maxHP + 5
        armadura = armadura + 1
        atkMin = atkMin + 3
        atkMax = atkMax + 3
        if(velocidade < 11):
            velocidade = velocidade + 1
        if(forca < 7):
            forca = forca + 1
        expNext = expNext * 2
        level = level + 1
        print("Você subiu de nível!")

def caminhar(direcao, limite):
    global posX, posY
    if(direcao == 1): #caminhar norte
        if(posY != 1):
            posY = posY - 1
            print("OK")
        else:
            print("Impossível caminhar norte!")
    elif(direcao == 2): # caminhar sul
        if(posY != limite):
            posY = posY + 1
            print("OK")
        else:
            print("Impossível caminhar sul!")
    elif(direcao == 3): # caminhar leste
        if(posX != limite):
            posX = posX + 1
            print("OK")
        else:
            print("Impossível caminhar leste!")
    else: # caminhar oeste
        if(posX != 1):
            posX = posX - 1
            print("OK")
        else:
            print("Impossível caminhar oeste!")

def verStatus():
    global nome, HP, maxHP, armadura, atkMin, atkMax, velocidade, forca, exp, expNext, level, pocoes, possuiChave
    print(nome)
    print("HP: " + str(HP) + "/" + str(maxHP) + " | Level: " + str(level))
    print("Ataque: " + str(atkMin) + "(min) / " + str(atkMax) + "(max)")
    print("Experiência: " + str(exp) + "/" + str(expNext))
    print("Força: " + str(forca))
    print("Velocidade: " + str(velocidade))
    print("Armadura: " + str(armadura))
    print("---\nInventário: ")

def beberPocao(quantPoc, quantCura):
    global HP, maxHP
    if(quantPoc > 0):
        if(HP < maxHP):
            HP = HP + quantCura
            quantoCurado = str(quantCura) + " HP" # armazena a quantidade curada
            if(HP > maxHP): # Se o HP ficar maior que o máximo
                temp = HP - maxHP # salva temporáriamente a diferença
                HP = maxHP # Seta o HP para o máximo
                quantoCurado = str(quantCura - temp) + " HP" # altera a mensagem para a diferença
            print("Você bebeu uma poção que curou " + quantoCurado + "!")
            return 1
        else:
            print("Seu HP está cheio! Não é necessario beter uma poção")
            return 0
    else:
        print("Você não possui nenhuma poção!")
        return 0

def salvarJogo(chaveX, chaveY, portaoX, portaoY, item1Tipo, item1Quant, item2Tipo, item2Quant, item3Tipo, item3Quant, item4Tipo, item4Quant):
    global nome, HP, maxHP, armadura, atkMin, atkMax, velocidade, forca, exp, expNext, level, posX, posY
    
    file = open("saves/" + nome + '.adv','w') # abre o arquivo para salvar

    # Gera o texto a ser codificado
    texto = str(HP) + "," + str(maxHP) + "," + str(armadura) + "," + str(atkMin) + "," + str(atkMax) + "," + str(velocidade) + "," + str(forca) + "," + str(exp) + "," + str(expNext) + "," + str(level) + "," + str(posX) + "," + str(posY) + "," + str(chaveX) + "," + str(chaveY) + "," + str(portaoX) + "," + str(portaoY) + "," + str(item1Tipo) + "," + str(item1Quant) + "," + str(item2Tipo) + "," + str(item2Quant) + "," + str(item3Tipo) + "," + str(item3Quant) + "," + str(item4Tipo) + "," + str(item4Quant)
    texto = base64.b64encode(texto.encode('ascii'))
    
    texto = texto.decode("utf-8")
    
    # Salva os dados no arquivo
    file.write(texto)
    
    file.close() # fecha o arquivo
    print("Jogo salvo com sucesso!")

def abrirJogo():
    global nome, HP, maxHP, armadura, atkMin, atkMax, velocidade, forca, exp, expNext, level, pocoes, possuiChave, posX, posY, chaveX, chaveY, portaoX, portaoY, item1Tipo, item1Quant, item2Tipo, item2Quant, item3Tipo, item3Quant, item4Tipo, item4Quant
    print("Tentando abrir jogo...")
    try:
        file = open("saves/" + nome + ".adv",'r') # abre o arquivo para leitura
        for line in file:
            texto = base64.b64decode(str(line))
        texto = str(texto, 'utf-8')
        texto = texto.split(',')

        contAbrir = 0
        for x in range(0,24):
            if(contAbrir == 0):
                HP = int(texto[x])
            elif(contAbrir == 1):
                maxHP = int(texto[x])
            elif(contAbrir == 2):
                armadura = int(texto[x])
            elif(contAbrir == 3):
                atkMin = int(texto[x])
            elif(contAbrir == 4):
                atkMax = int(texto[x])
            elif(contAbrir == 5):
                velocidade = int(texto[x])
            elif(contAbrir == 6):
                forca = int(texto[x])
            elif(contAbrir == 7):
                exp = int(texto[x])
            elif(contAbrir == 8):
                expNext = int(texto[x])
            elif(contAbrir == 9):
                level = int(texto[x])
            elif(contAbrir == 10):
                posX = int(texto[x])
            elif(contAbrir == 11):
                posY = int(texto[x])
            elif(contAbrir == 12):
                chaveX = int(texto[x])
            elif(contAbrir == 13):
                chaveY = int(texto[x])
            elif(contAbrir == 14):
                portaoX = int(texto[x])
            elif(contAbrir == 15):
                portaoY = int(texto[x])
            elif(contAbrir == 16):
                item1Tipo = int(texto[x])
            elif(contAbrir == 17):
                item1Quant = int(texto[x])
            elif(contAbrir == 18):
                item2Tipo = int(texto[x])
            elif(contAbrir == 19):
                item2Quant = int(texto[x])
            elif(contAbrir == 20):
                item3Tipo = int(texto[x])
            elif(contAbrir == 21):
                item3Quant = int(texto[x])
            elif(contAbrir == 22):
                item4Tipo = int(texto[x])
            elif(contAbrir == 23):
                item4Quant = int(texto[x])
            else:
                print("Dunno")
            contAbrir = contAbrir + 1
        #fim for
        file.close()
        print("\nJogo carregado com sucesso!\n---\n")
    except FileNotFoundError:
        print("Não há nenhum jogo salvo com o nome de herói atual!")

def verificarPossuiJogoSalvo(nome):
    try:
        file = open("saves/" + nome + ".adv",'r')
        file.close()
        return 1
    except:
        return 0

def fugirBatalha():
    global velocidade
    return random.randint(1, 12-velocidade)

def chanceBatalha():
    return random.randint(1, 6)
