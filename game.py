'''
Adventure Game
Copyright (c) 2015, William Alcântara Costa
All rights reserved.
- This code is licensed under the BSD 3-Clause License - check it on LICENSE.MD

---

Adventure Game (Jogo de aventura)
Copyright (c) 2015, William Alcântara Costa
Todos os direitos reservados.
- Este código está licensiado sob a Licença de Três Cláusulas BSD - leia mais em LICENSE.MD

'''

#------------------------------------------
#       Carregar o jogo
#------------------------------------------
print ("Carregando o jogo...\n")

import mundo
mundo.sortearPosicaoChave()
mundo.sortearPosicaoPortao()
print ("Mundo carregado!")

import item
item.setarItem(0, 1, 5)
print ("Itens carregados!")

import heroi
heroi.setarPosicaoInicial(mundo.limiteX, mundo.limiteY)
print("Herói carregado!")

import inimigo
print ("Inimigos carregados!")

import os
if not os.path.exists("saves"):
    print("Pasta saves não encontrada, ela será criada.")
    os.makedirs("saves")
    print("Pasta para salvar saves do jogo criada!")
else:
    print("Pasta saves encontrada!")

print("\n---\n")

#------------------------------------------
#       Métodos do jogo
#------------------------------------------

def carregarJogo():
    heroi.abrirJogo()
    mundo.abrirPosicoes(heroi.chaveX, heroi.chaveY, heroi.portaoX, heroi.portaoY)
    item.setarItem(0, heroi.item1Tipo, heroi.item1Quant)
    item.setarItem(1, heroi.item2Tipo, heroi.item2Quant)
    item.setarItem(2, heroi.item3Tipo, heroi.item3Quant)
    item.setarItem(3, heroi.item4Tipo, heroi.item4Quant)

def imprimirHud(isBatalha):
    if(isBatalha == 0):
        print("")
        print(heroi.nome + " | HP: " + str(heroi.HP) + "/" + str(heroi.maxHP))
        print("X: " + str(heroi.posX) + " | Y: " + str(heroi.posY) + " - " + mundo.lerPosicaoAtual(heroi.posX, heroi.posY))
        print("O que devo fazer agora?")
    else:
        print("")
        print(heroi.nome + " - HP: " + str(heroi.HP) + "/" + str(heroi.maxHP) + " VS " + inimigo.nome + " - HP: " + str(inimigo.HP) + "/" + str(inimigo.maxHP))
        print("atk - atacar | fug - fugir | bbp - beber poção\nO que fazer agora?")
        

def batalha():
    inimigo.setarInimigo(heroi.level)
    comando = ""
    while(heroi.HP > 0 and inimigo.HP > 0 and comando != "fug"):
        imprimirHud(1)
        comando = input("> ")
        
        if(comando == "atk"): # atacar
            inimigo.receberDano(heroi.atacar())
            if(inimigo.HP > 0):
                heroi.receberDano(inimigo.atacar())
                
        elif(comando == "fug"): # fugir
            chance = heroi.fugirBatalha()
            if(chance == 1): # conseguiu escapar
                print(heroi.nome + " escapou da batalha!")
            else: # NÃO conseguiu escapar
                comando = ""
                print(heroi.nome + " não conseguiu escapar!")
                heroi.receberDano(inimigo.atacar())
                
        elif(comando == "bbp"): # beber poção
            if(heroi.beberPocao(item.inventario[0].quantidade, item.inventario[0].aumentoHP)):
                item.alterarQuantidadeItem(1, 0, 1)
                heroi.receberDano(inimigo.atacar())
                
        else:
            print("Não é hora de '" + comando + "'! Você está no meio de uma batalha!")
            
    if(comando != "fug" and heroi.HP > 0):
        print("---\n" + heroi.nome + " derrotou o " + inimigo.nome + "!")
        print("Você ganhou " + str(inimigo.retornarExpGanha()) + " de experiência!")
        heroi.exp = heroi.exp + inimigo.retornarExpGanha()
        heroi.subirNivel()
        if(inimigo.chanceDroparPocao() == 1):
            item.alterarQuantidadeItem(0, 0, 1)
            print("O inimigo dropou uma poção!")

#------------------------------------------
#       Código do jogo
#------------------------------------------

# Titúlo feito em http://www.network-science.de/ascii/
print("        AAA        dd                        tt                          \n       AAAAA       dd vv   vv   eee  nn nnn  tt    uu   uu rr rr    eee  \n      AA   AA  dddddd  vv vv  ee   e nnn  nn tttt  uu   uu rrr  r ee   e \n      AAAAAAA dd   dd   vvv   eeeee  nn   nn tt    uu   uu rr     eeeee  \n      AA   AA  dddddd    v     eeeee nn   nn  tttt  uuuu u rr      eeeee \n                                                                         \n                        GGGG                             \n                       GG  GG   aa aa mm mm mmmm    eee  \n                      GG       aa aaa mmm  mm  mm ee   e \n                      GG   GG aa  aaa mmm  mm  mm eeeee  \n                       GGGGGG  aaa aa mmm  mm  mm  eeeee ")

heroi.nome = input("Digite um nome para o herói:\n> ")

if(heroi.verificarPossuiJogoSalvo(heroi.nome)):
    print("Já existe um jogo salvo com esse nome, gostaria de abrí-lo?")
    decisao = ""
    while(decisao != "s" and decisao != "S" and decisao != "n" and decisao != "N"):
        decisao = input("(s/n) | > ")
        if(decisao == "s" or decisao == "S"):
            carregarJogo()
        elif(decisao == "n" or decisao == "N"):
            print("Um novo jogo será iniciado")
        else:
            print("Digite apenas S ou N")
menu = ""
while(menu != "sair" and heroi.HP > 0):
    imprimirHud(0)
    menu = input("> ")

    if(menu == "salvarJogo"):
        heroi.salvarJogo(mundo.posChaveX, mundo.posChaveY, mundo.posPortaoX, mundo.posPortaoY, item.inventario[0].itemID, item.inventario[0].quantidade, item.inventario[1].itemID, item.inventario[1].quantidade, item.inventario[2].itemID, item.inventario[2].quantidade, item.inventario[3].itemID, item.inventario[3].quantidade)

    elif (menu == "abrirJogo"):
        carregarJogo()

    elif(menu == "goN" or menu == "gon" or menu == "go n"):
        heroi.caminhar(1, mundo.limiteY)
        chanceBatalha = heroi.chanceBatalha()
        if(chanceBatalha == 1):
            batalha()

    elif(menu == "goS" or menu == "gos" or menu == "go s"):
        heroi.caminhar(2, mundo.limiteY)
        chanceBatalha = heroi.chanceBatalha()
        if(chanceBatalha == 1):
            batalha()

    elif(menu == "goL" or menu == "gol" or menu == "go l"):
        heroi.caminhar(3, mundo.limiteX)
        chanceBatalha = heroi.chanceBatalha()
        if(chanceBatalha == 1):
            batalha()

    elif(menu == "goO" or menu == "goo" or menu == "go o"):
        heroi.caminhar(4, mundo.limiteX)
        chanceBatalha = heroi.chanceBatalha()
        if(chanceBatalha == 1):
            batalha()

    elif(menu == "pegar"):
        if(heroi.posX == mundo.posChaveX and heroi.posY == mundo.posChaveY):
            item.setarItem(item.retornaPrimeiroSlotVazio(), 3, 1)
            print("Você pegou a chave!\nAgora encontre o portão!")
            mundo.moverChave()
        else:
            print("Você não está perto da chave!")

    elif(menu == "abrir"):
        if(heroi.posX == mundo.posPortaoX and heroi.posY == mundo.posPortaoY):
            if(item.possuiChave()):
                print("Portão aberto!\nVitória!")
                break
            else:
                print("Você não possui a chave!")
        else:
            print("Você não está perto do portão!")

    elif(menu == "status"):
        heroi.verStatus()
        item.lerInventario()

    elif(menu == "beber poção" or menu == "beber pocao" or menu == "beberpocao" or menu == "beberpoção" or menu == "bbp"):
        if(heroi.beberPocao(item.inventario[0].quantidade, item.inventario[0].aumentoHP)):
            item.alterarQuantidadeItem(1, 0, 1)

    elif(menu == "sair"):
        print("Saindo...")
    #-----------------------------------
    #       Comandos para testes durante o BETA
    #               REMOVER DA VERSÃO FINAL!!!
    #-----------------------------------

    elif(menu == "largar"):
        itemRemovido = 5
        while(itemRemovido != 0):
            try:
                print("Digite o nº do item a remover:")
                item.lerInventario()
                print("0 - Cancelar")
                itemRemovido = int(input("largar> "))
                if(itemRemovido != 0):
                    if(item.inventario[itemRemovido-1].nome == "Chave"):
                        print("Esse item é importante demais para ser jogado fora!\nTente outro!\n")
                    elif(item.inventario[itemRemovido-1].nome == "VAZIO"):
                        print("Não há nenhum item nesse espaço!\nTente outro!\n")
                    else:
                        item.setarItem(itemRemovido-1, 0, 0)
                        print("Item largado!")
                        itemRemovido = 0
            except ValueError:
                print("Digite apenas NÚMEROS no campo!\n")
            
            
    elif(menu == "inv vazio"):
        print(item.retornaPrimeiroSlotVazio())

    elif(menu == "adicionarExp"):
        novoValor = input("Digite um valor para adicionar:\n> ")
        heroi.exp = heroi.exp + int(novoValor)
        heroi.subirNivel()

    elif(menu == "dano"):
        valor = int(input("Digite um valor para receber de dano:\n> "))
        heroi.HP = heroi.HP - valor

    elif(menu == "batalha"):
        batalha()
        
    elif(menu == "diz ai seu bosta"):
        print("Chave\nX: " + str(mundo.posChaveX) + " | Y: " + str(mundo.posChaveY))
        print("Portão\nX: " + str(mundo.posPortaoX) + " | Y: " + str(mundo.posPortaoY))
    #------------------------------------
    #       Fim dos comandos de teste
    #------------------------------------

    else:
        print("Não sei o que '" + menu + "' significa!")

if(heroi.HP < 1):
    print(heroi.nome + " morreu!")
