import pygame
import time
import random

pygame.init()

############# Variáveis Gerais #############s
larguraTela = 800
alturaTela = 600
gamedisplay = pygame.display.set_mode((larguraTela,alturaTela))
clock = pygame.time.Clock()
# RGB (Red, Green, Blue) (0,255)
black = (0,0,0)
white = (255,255,255)
gray =  (100,100,100)

ironManImg = pygame.image.load('assets/ironLarge.png')
misselImg = pygame.image.load('assets/missile.png')
fundo = pygame.image.load('assets/sky.png')
explo_sound = pygame.mixer.Sound('assets/explosao.wav')
missel_sound = pygame.mixer.Sound('assets/missile.wav')


############# Funções Gerais #############
def mostraFundo():
    gamedisplay.blit(fundo, (0,0) )

def mostraIron( x, y ):
    gamedisplay.blit(ironManImg, (x,y) )

def mostraMissel( x, y ):
    gamedisplay.blit(misselImg, (x,y) )

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


def placar(contador=0):
    fonte = pygame.font.SysFont(None, 25)
    text = fonte.render('Desvios: '+ str(contador), True, white)
    gamedisplay.blit(text, (10, 30))

def morte_iron():
    pygame.mixer.Sound.play(explo_sound)
    pygame.mixer.music.stop()
    mostra_mensagem('Você morreu!')




############ Looping do Jogo

def game_loop():
    pygame.mixer.music.set_volume(0.01)
    pygame.mixer.music.load('assets/ironsound.mp3')
    pygame.mixer.music.play(-1)

    ironPosicaoX = 330
    ironPosicaoY = 470
    movi_x = 0
    altura_iron = 110
    largura_iron = 120


    missel_x = random.randrange(0, larguraTela)
    missel_y = 0 - 250
    altura_missel = 250
    largura_missel = 50
    velo_missel = 7

    cont = 0
    
    while True:
        # event.get() devolve uma lista de eventos que estão acontecendo
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                # quit() é comando native terminar o programa
                quit()
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    movi_x = -5
                if event.key == pygame.K_RIGHT:
                    movi_x = 5
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    movi_x = 0

            if ironPosicaoX > larguraTela - largura_iron or ironPosicaoX < 0:
                movi_x = 0
                morte_iron()

            if missel_y > alturaTela:
                pygame.mixer.music.set_volume(0.01)
                pygame.mixer.Sound.play(missel_sound)
                missel_y = 0 - altura_missel
                missel_x = random.randrange(0, larguraTela)
                velo_missel += 1
                cont += 1

            if ironPosicaoY < missel_y + altura_missel:
                if ironPosicaoX < missel_x and ironPosicaoX + largura_iron > missel_x or missel_x + largura_missel > ironPosicaoX and missel_x + largura_missel < ironPosicaoX + largura_iron:
                    morte_iron()

                

        ironPosicaoX += movi_x
        missel_y += velo_missel        

        mostraFundo()
        placar(cont)
        mostraIron(ironPosicaoX,ironPosicaoY)
        mostraMissel(missel_x, missel_y)
        pygame.display.update()
        clock.tick(60)


game_loop()