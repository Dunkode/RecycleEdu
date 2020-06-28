import pygame
import time
import random

pygame.init()

############# Variáveis Gerais #############
larguraTela = 800
alturaTela = 600
gamedisplay = pygame.display.set_mode((larguraTela,alturaTela))
clock = pygame.time.Clock()
# RGB (Red, Green, Blue) (0,255)
black = (0,0,0)
white = (255,255,255)
gray =  (100,100,100)

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
papel_verd = pygame.image.load('assets/vidro-verde.png')
papel_verm = pygame.image.load('assets/papel-verm.png')
papel_azul = pygame.image.load('assets/papel-azul.png')

plast_ama = pygame.image.load('assets/plastico-ama.png')
plast_verd = pygame.image.load('assets/vidro-verde.png')
plast_verm = pygame.image.load('assets/plastico-verm.png')
plast_azul = pygame.image.load('assets/plastico-azul.png')

metal_ama = pygame.image.load('assets/metal-ama.png')
metal_verd = pygame.image.load('assets/vidro-verde.png')
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

def muda_obj():
    return random.choice([obj_metal, obj_papel, obj_plast, obj_vidro])

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def mostra_mensagem(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (larguraTela/2, alturaTela/2)
    gamedisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    time.sleep(5)
    game_loop()


def reciclados(contador=0):
    fonte = pygame.font.SysFont(None, 25)
    text = fonte.render('Reciclados: '+ str(contador), True, white)
    gamedisplay.blit(text, (10, 30))

def desperdicados(contador=0):
    fonte = pygame.font.SysFont(None, 25)
    text = fonte.render('Desperdiçados: '+ str(contador), True, white)
    gamedisplay.blit(text, (760, 770))

def game_over():
    mostra_mensagem('Você morreu!')




############ Looping do Jogo

def game_loop():
    '''
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.music.load('assets/ironsound.mp3')
    pygame.mixer.music.play(-1)
    '''

    pos_objX = 400
    pos_objY = 300
    movi_x = 0
    movi_y = 0
    larg_obj = 0
    alt_obj = 0

    pos_lata1X = 100
    pos_lata1Y = 100
    larg_lata1 = 1
    alt_lata1 = 1

    pos_lata2X = 600
    pos_lata2Y = 100
    larg_lata2 = 110
    alt_lata2 = 120

    pos_lata3X = 100
    pos_lata3Y = 600
    larg_lata3 = 110
    alt_lata3 = 120

    pos_lata4X = 600
    pos_lata4Y = 600
    larg_lata4 = 110
    alt_lata4 = 120

    troca_obj = 0
    obj_mostrado = random.choice([obj_metal, obj_papel, obj_plast, obj_vidro])
    
    cont = 0
    
    while True:
        # event.get() devolve uma lista de eventos que estão acontecendo
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # quit() é comando native terminar o programa
                quit()

            if troca_obj == 0:
                obj_mostrado = random.choice([obj_metal, obj_papel, obj_plast, obj_vidro])
                define_tam(obj_mostrado)
                troca_obj += 1
            else:
                pass

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
                 game_loop()

            if pos_objY > alturaTela - alt_obj or pos_objY < 0:
                movi_x = 0
                troca_obj = 0
                break
                

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    movi_x = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    movi_y = 0

            

            '''
            if ironPosicaoY < missel_y + altura_missel:
                if ironPosicaoX < missel_x and ironPosicaoX + largura_iron > missel_x or missel_x + largura_missel > ironPosicaoX and missel_x + largura_missel < ironPosicaoX + largura_iron:
                    morte_iron()
            '''

                

        pos_objX += movi_x
        pos_objY += movi_y      

        mostraFundo()
        mostra_obj(obj_mostrado, pos_objX, pos_objY)
        pygame.display.update()
        clock.tick(60)


game_loop()