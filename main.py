import pygame
import time
import random

pygame.init()

############# Variáveis Gerais #############
larguraTela = 800
alturaTela = 600
gamedisplay = pygame.display.set_mode((larguraTela,alturaTela))
clock = pygame.time.Clock()

recic = 0
desper = 0
# RGB (Red, Green, Blue) (0,255)
black = (0,0,0)
white = (255,255,255)
gray =  (100,100,100)
red = (255, 0, 0)
green = (0,255,0)

## Lixo movimentavel
obj_metal = pygame.image.load('assets/metal.png')
obj_vidro = pygame.image.load('assets/vidro.png')
obj_papel = pygame.image.load('assets/papel.png')
obj_plast = pygame.image.load('assets/plastico.png')

#Latas de lixo
vidro_ama = pygame.image.load('assets/vidro-ama.png')
vidro_verd = pygame.image.load('assets/vidro-verde.png')
vidro_verm = pygame.image.load('assets/vidro-verm.png')
vidro_azul = pygame.image.load('assets/vidro-azul.png')

papel_ama = pygame.image.load('assets/papel-ama.png')
papel_verd = pygame.image.load('assets/papel-verde.png')
papel_verm = pygame.image.load('assets/papel-verm.png')
papel_azul = pygame.image.load('assets/papel-azul.png')

plast_ama = pygame.image.load('assets/plastico-ama.png')
plast_verd = pygame.image.load('assets/plastico-verde.png')
plast_verm = pygame.image.load('assets/plastico-verm.png')
plast_azul = pygame.image.load('assets/plastico-azul.png')

metal_ama = pygame.image.load('assets/metal-ama.png')
metal_verd = pygame.image.load('assets/metal-verde.png')
metal_verm = pygame.image.load('assets/metal-verm.png')
metal_azul = pygame.image.load('assets/metal-azul.png')

##fundo
fundo = pygame.image.load('assets/fundo.png')



############# Funções Gerais #############



def define_tam(objeto):
    if objeto == obj_vidro:
        larg_obj = 30
        alt_obj = 116
    elif objeto == obj_metal:
        larg_obj = 56
        alt_obj = 120
    elif objeto == obj_papel:
        larg_obj = 100
        alt_obj = 122
    elif objeto == obj_plast:
        larg_obj = 129
        alt_obj = 103


def mostraFundo():
    gamedisplay.blit(fundo, (0,0) )

def mostra_obj(objeto, x, y):
    gamedisplay.blit(objeto, (x, y))

def mostra_lata1(lata1, x, y):
    gamedisplay.blit(lata1, (x, y))

def mostra_lata2(lata2, x, y):
    gamedisplay.blit(lata2, (x, y))

def mostra_lata3(lata3, x, y):
    gamedisplay.blit(lata3, (x, y))

def mostra_lata4(lata4, x, y):
    gamedisplay.blit(lata4, (x, y))

def novo_obj():
    return random.choice([obj_metal, obj_papel, obj_plast, obj_vidro])

def nova_lata(arg1, arg2, arg3, arg4):
    return random.choice([arg1, arg2, arg3, arg4])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def mostra_mensagem(text = 'Descarte incorreto!'):
    largeText = pygame.font.Font('freesansbold.ttf', 40)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (larguraTela/2, alturaTela/2)
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(1)


def reciclados(contador=0):
    fonte = pygame.font.SysFont(None, 25)
    text = fonte.render('Reciclados: '+ str(contador), True, green)
    gamedisplay.blit(text, (10, 30))

def desperdicados(contador=0):
    fonte = pygame.font.SysFont(None, 25)
    text = fonte.render('desperdiçados: '+ str(contador), True, red)
    gamedisplay.blit(text, (600, 30))

def game_over():
    mostra_mensagem('Você poluiu demais!')
    game_loop(0, 0)




############ Looping do Jogo

def game_loop(pon_rec, pon_des):
    '''
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.music.load('assets/ironsound.mp3')
    pygame.mixer.music.play(-1)
    '''
    pos_objX = 350
    pos_objY = 250
    movi_x = 0
    movi_y = 0
    larg_obj = 0
    alt_obj = 0

    pos_lata1X = 50
    pos_lata1Y = 50
    larg_lata1 = 130
    alt_lata1 = 211

    pos_lata2X = 600
    pos_lata2Y = 50
    larg_lata2 = 130
    alt_lata2 = 211

    pos_lata3X = 50
    pos_lata3Y = 350
    larg_lata3 = 130
    alt_lata3 = 211

    pos_lata4X = 600
    pos_lata4Y = 350
    larg_lata4 = 130
    alt_lata4 = 211
    
    recic = pon_rec
    desper = pon_des

    obj_mostrado = novo_obj()

    lata1 = nova_lata(vidro_ama, vidro_azul, vidro_verd, vidro_verm)
    lata2 = nova_lata(metal_ama, metal_azul, metal_verd, metal_verm)
    lata3 = nova_lata(plast_ama, plast_azul, plast_verd, plast_verm)
    lata4 = nova_lata(papel_ama, papel_azul, papel_verd, papel_verm)

    if obj_mostrado == obj_vidro:
        larg_obj = 30
        alt_obj = 116
    elif obj_mostrado == obj_metal:
        larg_obj = 56
        alt_obj = 120
    elif obj_mostrado == obj_papel:
        larg_obj = 100
        alt_obj = 122
    elif obj_mostrado == obj_plast:
        larg_obj = 129
        alt_obj = 103

    
    while True:
        
          

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movi_x = -5
                if event.key == pygame.K_RIGHT:
                    movi_x = 5
                if event.key == pygame.K_DOWN:
                    movi_y = 5
                if event.key == pygame.K_UP:
                    movi_y = -5
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
            if pos_objX > larguraTela - larg_obj or pos_objX < 0:
                movi_x = 0
                mostra_mensagem('Você jogou o lixo na rua!')
                desper += 1
                game_loop(recic, desper)

            if pos_objY > alturaTela - alt_obj or pos_objY < 0:
                movi_x = 0
                mostra_mensagem('Você jogou o lixo na rua!')
                desper += 1
                game_loop(recic, desper)
                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    movi_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movi_y = 0


            if pos_objX  < pos_lata1X + larg_lata1 and pos_objY < pos_lata1Y + larg_lata1:
                if obj_mostrado == obj_vidro:
                    recic +=1
                    game_loop(recic, desper)
                else:
                    desper +=1
                    mostra_mensagem()
                    game_loop(recic, desper)

            if pos_objX + larg_obj  > pos_lata2X and pos_objY < pos_lata2Y + larg_lata2:
                if obj_mostrado == obj_metal:
                    recic += 1
                    game_loop(recic, desper)
                else:
                    desper +=1
                    mostra_mensagem()
                    game_loop(recic, desper)

            if pos_objX < pos_lata3X + larg_lata3 and pos_objY + alt_obj > pos_lata3Y:
                if obj_mostrado == obj_plast:
                    recic +=1
                    game_loop(recic, desper)
                else:
                    desper +=1
                    mostra_mensagem()
                    game_loop(recic, desper)
                

            if pos_objX + larg_obj > pos_lata4X and pos_objY + alt_obj > pos_lata4Y:
                if obj_mostrado == obj_papel:
                    desper +=1
                    recic +=1
                    game_loop(recic, desper)
                else:
                    desper +=1
                    mostra_mensagem()
                    game_loop(recic, desper)  

            if desper >= 5:
                game_over() 

        pos_objX += movi_x
        pos_objY += movi_y      

        mostraFundo()

        reciclados(recic)
        desperdicados(desper)

        mostra_lata1(lata1, pos_lata1X, pos_lata1Y)
        mostra_lata2(lata2, pos_lata2X, pos_lata2Y)
        mostra_lata3(lata3, pos_lata3X, pos_lata3Y)
        mostra_lata4(lata4, pos_lata4X, pos_lata4Y)

        mostra_obj(obj_mostrado, pos_objX, pos_objY)

        pygame.display.update()
        clock.tick(100)

game_loop(recic, desper)