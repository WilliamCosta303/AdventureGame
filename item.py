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

import random # só pra ter certeza

class SubItem():
    itemID = 0
    nome = "VAZIO"
    descricao = ""
    quantidade = 0
    aumentoHP = 0
    aumentoAtk = 0
    aumentoArmadura = 0

inventario = (SubItem(), SubItem(), SubItem(), SubItem())

def setarItem(posicao, tipo, quant):
    if(tipo == 1): # Poções do heroi
        inventario[posicao].itemID = tipo
        inventario[posicao].nome = "Poção"
        inventario[posicao].descricao = "Curam 25HP do herói"
        inventario[posicao].quantidade = quant
        inventario[posicao].aumentoHP = 25
        inventario[posicao].aumentoAtk = 0
        inventario[posicao].aumentoArmadura = 0

    elif(tipo == 2): # Super-poção
        inventario[posicao].itemID = tipo
        inventario[posicao].nome = "Super Poção"
        inventario[posicao].descricao = "Curam 50HP do herói"
        inventario[posicao].quantidade = quant
        inventario[posicao].aumentoHP = 50
        inventario[posicao].aumentoAtk = 0
        inventario[posicao].aumentoArmadura = 0

    elif(tipo == 3): # Chave
        inventario[posicao].itemID = tipo
        inventario[posicao].nome = "Chave"
        inventario[posicao].descricao = "Usada para abrir o portão"
        inventario[posicao].quantidade = quant
        inventario[posicao].aumentoHP = 0
        inventario[posicao].aumentoAtk = 0
        inventario[posicao].aumentoArmadura = 0
        
    elif(tipo == 4): # Espada
        inventario[posicao].itemID = tipo
        inventario[posicao].nome = "Espada"
        inventario[posicao].descricao = "Aumenta o ataque em 5 pontos"
        inventario[posicao].quantidade = quant
        inventario[posicao].aumentoHP = 0
        inventario[posicao].aumentoAtk = 5
        inventario[posicao].aumentoArmadura = 0

    else: # Item inválido
        inventario[posicao].itemID = tipo
        inventario[posicao].nome = "VAZIO"
        inventario[posicao].descricao = ""
        inventario[posicao].quantidade = 0
        inventario[posicao].aumentoHP = 0
        inventario[posicao].aumentoAtk = 0
        inventario[posicao].aumentoArmadura = 0

def alterarQuantidadeItem(isConsumir, pos, quant):
    if(isConsumir): # Se estiver consumindo o item
        inventario[pos].quantidade = inventario[pos].quantidade - quant
    else: # Se não consumir o item
        inventario[pos].quantidade = inventario[pos].quantidade + quant

def possuiChave():
    valorRetorno = 0
    for x in range(0,4):
           if(inventario[x].nome == "Chave"):
                valorRetorno = 1
                break
    return valorRetorno

def retornaPrimeiroSlotVazio():
    valorRetorno = -1
    for x in range(0,4):
        if(inventario[x].nome == "VAZIO"):
            valorRetorno = x
            break
    return valorRetorno
    
def lerInventario():
    for x in range(0,4):
        if(inventario[x].nome != "VAZIO"):
            print(str(x+1) + " - " + inventario[x].nome + " (Q: " + str(inventario[x].quantidade) + ") - " + inventario[x].descricao)
        else:
            print(str(x+1) + " - " + inventario[x].nome)
