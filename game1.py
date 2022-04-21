import pygame
pygame.init()

userx = 390
usery = 580
car1x = [0, -400, - 600, -800, -200, -50, -650, -70, -450, -250]
m = 0
kills = 0
wins = 0

pygame.font.init()

font_game = pygame.font.get_default_font()
jogo_font = pygame.font.SysFont(font_game, 45)


janela = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Game')

janela_aberta = True
while janela_aberta:
    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            janela_aberta = False

    events = pygame.event.get()

    if pygame.key.get_pressed()[pygame.K_UP]:
        if usery > 0:
            usery = usery-2
    if pygame.key.get_pressed()[pygame.K_DOWN]:
        if usery < 580:
            usery = usery+2
    if pygame.key.get_pressed()[pygame.K_LEFT]:
        if userx > 0:
            userx = userx-2
    if pygame.key.get_pressed()[pygame.K_RIGHT]:
        if userx < 780:
            userx = userx+2

    car1x[0] = car1x[0]+3
    car1x[1] = car1x[1]+6
    car1x[2] = car1x[2]+3
    car1x[3] = car1x[3]+7
    car1x[4] = car1x[4]+1
    car1x[5] = car1x[5]+2
    car1x[6] = car1x[6]+8
    car1x[7] = car1x[7]+1
    car1x[8] = car1x[8]+6
    car1x[9] = car1x[9]+3

    if car1x[0] > 800:
        car1x[0] = 0

    if car1x[1] > 800:
        car1x[1] = -400

    if car1x[2] > 800:
        car1x[2] = -600

    if car1x[3] > 800:
        car1x[3] = -800

    if car1x[4] > 800:
        car1x[4] = -200

    if car1x[5] > 800:
        car1x[5] = -50

    if car1x[6] > 800:
        car1x[6] = -650

    if car1x[7] > 800:
        car1x[7] = -70

    if car1x[8] > 800:
        car1x[8] = -450

    if car1x[9] > 800:
        car1x[9] = -250

    nkstr = 'KILLS ' + str(kills)
    nwinstr = 'WINS ' + str(wins)

    janela.fill((0, 0, 0))

    pygame.draw.line(janela, (0, 255, 0), (0, 50), (800, 50), 5)
    pygame.draw.line(janela, (0, 255, 0), (0, 550), (800, 550), 5)

    text_safe = jogo_font.render('SAFE ZONE', True, (0, 255, 0))
    numkill = jogo_font.render(nkstr, True, (0, 255, 0))
    numwin = jogo_font.render(nwinstr, True, (0, 255, 0))
    janela.blit(text_safe, (300, 25))
    janela.blit(text_safe, (300, 550))
    janela.blit(numkill, (100, 25))
    janela.blit(numwin, (600, 25))

    user = pygame.draw.rect(janela, (255, 255, 255), (userx, usery, 20, 20))

    c0 = pygame.draw.rect(janela, (255, 0, 0), (car1x[0], 500, 100, 50))
    c1 = pygame.draw.rect(janela, (0, 0, 255), (car1x[1], 450, 100, 50))
    c2 = pygame.draw.rect(janela, (255, 0, 0), (car1x[2], 400, 100, 50))
    c3 = pygame.draw.rect(janela, (0, 0, 255), (car1x[3], 350, 100, 50))
    c4 = pygame.draw.rect(janela, (255, 0, 0), (car1x[4], 300, 100, 50))
    c5 = pygame.draw.rect(janela, (0, 0, 255), (car1x[5], 250, 100, 50))
    c6 = pygame.draw.rect(janela, (255, 0, 0), (car1x[6], 200, 100, 50))
    c7 = pygame.draw.rect(janela, (0, 0, 255), (car1x[7], 150, 100, 50))
    c8 = pygame.draw.rect(janela, (255, 0, 0), (car1x[8], 100, 100, 50))
    c9 = pygame.draw.rect(janela, (0, 0, 255), (car1x[9], 55, 100, 45))

    pygame.display.update()

    if user.colliderect(c0):
        userx = 390
        usery = 580
        kills = kills + 1
    if user.colliderect(c1):
        userx = 390
        usery = 580
        kills = kills + 1
    if user.colliderect(c2):
        userx = 390
        usery = 580
        kills = kills + 1
    if user.colliderect(c3):
        userx = 390
        usery = 580
        kills = kills + 1
    if user.colliderect(c4):
        userx = 390
        usery = 580
        kills = kills + 1
    if user.colliderect(c5):
        userx = 390
        usery = 580
        kills = kills + 1
    if user.colliderect(c6):
        userx = 390
        usery = 580
        kills = kills + 1
    if user.colliderect(c7):
        userx = 390
        usery = 580
        kills = kills + 1
    if user.colliderect(c8):
        userx = 390
        usery = 580
        kills = kills + 1
    if user.colliderect(c9):
        userx = 390
        usery = 580
        kills = kills + 1
    if usery <= 50:
        wins = wins + 1
        usery = 580

pygame.quite()
