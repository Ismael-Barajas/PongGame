import pygame
import sys
import random

pygame.init()

HEIGHTWIND = 600
WIDTHWIND = 900
paddle_Width = 10
paddle_Height = 80
fps = 120
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
playerBallHit = pygame.mixer.Sound('PlayerPongSound.wav')
compBallHit = pygame.mixer.Sound('CompPongSound.wav')
winnerSound = pygame.mixer.Sound('Winnersound.wav')
loserSound = pygame.mixer.Sound('LoserSound.wav')
gameBackground = pygame.image.load('BackGround.png')
g_window = pygame.display.set_mode((WIDTHWIND, HEIGHTWIND))
pygame.display.set_caption('Pong No Walls.')
g_window.blit(gameBackground, (0, 0))


class playerV(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((paddle_Width, paddle_Height))
        self.image = pygame.image.load('redVertPad.png')
        self.rect = self.image.get_rect()
        self.rect.right = WIDTHWIND - 25
        self.rect.centery = HEIGHTWIND / 2
        self.yAxis = 0

    def update(self):
        self.yAxis = 0
        keyState = pygame.key.get_pressed()
        if keyState[pygame.K_UP]:
            self.yAxis = -3
        if keyState[pygame.K_DOWN]:
            self.yAxis = 3
        self.rect.y += self.yAxis
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHTWIND:
            self.rect.bottom = HEIGHTWIND


class playerB(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((paddle_Height, paddle_Width))
        self.image = pygame.image.load('redHorizPad.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHTWIND
        self.rect.centerx = WIDTHWIND - (WIDTHWIND / 4)
        self.xAxis = 0

    def update(self):
        self.xAxis = 0
        keyState = pygame.key.get_pressed()
        if keyState[pygame.K_LEFT]:
            self.xAxis = -3
        if keyState[pygame.K_RIGHT]:
            self.xAxis = 3
        self.rect.x += self.xAxis
        if self.rect.left < WIDTHWIND / 2:
            self.rect.left = WIDTHWIND / 2
        if self.rect.right > WIDTHWIND - 35:
            self.rect.right = WIDTHWIND - 35


class playerT(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((paddle_Height, paddle_Width))
        self.image = pygame.image.load('redHorizPad.png')
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = WIDTHWIND - (WIDTHWIND / 4)
        self.xAxis = 0

    def update(self):
        self.xAxis = 0
        keyState = pygame.key.get_pressed()
        if keyState[pygame.K_LEFT]:
            self.xAxis = -3
        if keyState[pygame.K_RIGHT]:
            self.xAxis = 3
        self.rect.x += self.xAxis
        if self.rect.left < WIDTHWIND / 2:
            self.rect.left = WIDTHWIND / 2
        if self.rect.right > WIDTHWIND - 35:
            self.rect.right = WIDTHWIND - 35


class compV(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = 2
        self.image = pygame.Surface((paddle_Width, paddle_Height))
        self.image = pygame.image.load('blueVertPad.png')
        self.rect = self.image.get_rect()
        self.rect.left = 25
        self.rect.centery = HEIGHTWIND / 2
        self.yAxis = 0

    def update(self):
        self.yAxis = 0
        if Ball.rect.centery < self.rect.centery:
            self.yAxis -= self.velocity
        if Ball.rect.centery > self.rect.centery:
            self.yAxis += self.velocity
        self.rect.y += self.yAxis
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHTWIND:
            self.rect.bottom = HEIGHTWIND


class compB(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = 2
        self.image = pygame.Surface((paddle_Height, paddle_Width))
        self.image = pygame.image.load('blueHorizPad.png')
        self.rect = self.image.get_rect()
        self.rect.bottom = HEIGHTWIND
        self.rect.centerx = WIDTHWIND / 4
        self.xAxis = 0

    def update(self):
        self.xAxis = 0
        if Ball.rect.centerx < self.rect.centerx:
            self.xAxis -= self.velocity
        if Ball.rect.centerx > self.rect.centerx:
            self.xAxis += self.velocity
        self.rect.x += self.xAxis
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTHWIND / 2:
            self.rect.right = WIDTHWIND / 2


class compT(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.velocity = 2
        self.image = pygame.Surface((paddle_Height, paddle_Width))
        self.image = pygame.image.load('blueHorizPad.png')
        self.rect = self.image.get_rect()
        self.rect.top = 0
        self.rect.centerx = WIDTHWIND / 4
        self.xAxis = 0

    def update(self):
        self.xAxis = 0
        if Ball.rect.centerx < self.rect.centerx:
            self.xAxis -= self.velocity
        if Ball.rect.centerx > self.rect.centerx:
            self.xAxis += self.velocity
        self.rect.x += self.xAxis
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTHWIND / 2:
            self.rect.right = WIDTHWIND / 2


class ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTHWIND / 2, HEIGHTWIND / 2)
        self.xAxis = random.choice([-1, 1])
        self.yAxis = random.choice([-2, -1, 1, 2])

    def update(self):
        self.rect.x += self.xAxis
        self.rect.y += self.yAxis

        Collided = pygame.sprite.spritecollideany(Ball, PaddleSprites)
        if Collided:
            if Collided == pVert:
                playerBallHit.play()
                self.rect.x -= self.xAxis
                self.xAxis *= -1
                self.xAxis += random.choice([0, 1])
            if Collided == pBottom:
                playerBallHit.play()
                self.rect.y -= self.yAxis
                self.yAxis *= -1
                self.yAxis += random.choice([0, 1])
            if Collided == pTop:
                playerBallHit.play()
                self.rect.y -= self.yAxis
                self.yAxis *= -1
                self.yAxis += random.choice([0, 1])

            if Collided == cVert:
                compBallHit.play()
                self.rect.x -= self.xAxis
                self.xAxis *= -1
                self.xAxis += random.choice([0, 1])
            if Collided == cBottom:
                compBallHit.play()
                self.rect.y -= self.yAxis
                self.yAxis *= -1
                self.yAxis += random.choice([0, 1])
            if Collided == cTop:
                compBallHit.play()
                self.rect.y -= self.yAxis
                self.yAxis *= -1
                self.yAxis += random.choice([0, 1])

            if self.yAxis == 0:
                self.yAxis = random.choice([-1, 1])
            if self.yAxis <= 0:
                self.yAxis += -random.choice([-1, 0, 1])
            if self.yAxis >= 0:
                self.yAxis += random.choice([-1, 0, 1])
            if self.xAxis == 0:
                self.xAxis += random.choice([-1, 1])


class Score(object):
    def __init__(self):
        self.scoreFont = pygame.font.SysFont(None, 100)
        self.matchFont = pygame.font.SysFont(None, 50)
        self.WinnerFont = pygame.font.SysFont(None, 70)
        self.playerWin = self.WinnerFont.render('Player Wins!', True, WHITE)
        self.compWin = self.WinnerFont.render('Computer Wins!', True, WHITE)
        self.scorePlayer = 0
        self.PlayerScore = 0
        self.CompScore = 0
        self.scoreComputer = 0
        self.PMatches = 0
        self.CMatches = 0

    def update(self):
        if Ball.rect.right < 0:
            self.PlayerScore += 1
            Ball.__init__()
        if Ball.rect.top < 0 and Ball.rect.x <= WIDTHWIND / 2:
            self.PlayerScore += 1
            Ball.__init__()
        if Ball.rect.bottom > HEIGHTWIND and Ball.rect.x <= WIDTHWIND / 2:
            self.PlayerScore += 1
            Ball.__init__()

        if Ball.rect.left > WIDTHWIND:
            self.CompScore += 1
            Ball.__init__()
        if Ball.rect.top < 0 and Ball.rect.x >= WIDTHWIND / 2:
            self.CompScore += 1
            Ball.__init__()
        if Ball.rect.bottom > HEIGHTWIND and Ball.rect.x >= WIDTHWIND / 2:
            self.CompScore += 1
            Ball.__init__()

        self.scorePlayer = self.scoreFont.render(str(self.CompScore), True, WHITE, BLACK)
        self.scoreComputer = self.scoreFont.render(str(self.PlayerScore), True, WHITE, BLACK)

    def draw(self):
        g_window.blit(self.scorePlayer, (WIDTHWIND / 4, HEIGHTWIND / 8))
        g_window.blit(self.scoreComputer, (WIDTHWIND * 3 / 4, HEIGHTWIND / 8))
        if self.PlayerScore >= 11 and self.PlayerScore > self.CompScore + 2:
            winnerSound.play()
            g_window.blit(self.playerWin, (505, HEIGHTWIND / 4))
            self.PMatches += 1
            Ball.xAxis = 0
            Ball.yAxis = 0
        if self.CompScore >= 11 and self.CompScore > self.PlayerScore + 2:
            loserSound.play()
            g_window.blit(self.compWin, (55, HEIGHTWIND / 4))
            self.CMatches += 1
            Ball.xAxis = 0
            Ball.yAxis = 0


PaddleSprites = pygame.sprite.Group()
BallSprite = pygame.sprite.GroupSingle()
pVert = playerV()
pTop = playerT()
pBottom = playerB()
cVert = compV()
cTop = compT()
cBottom = compB()
Ball = ball()
PaddleSprites.add(pVert)
PaddleSprites.add(pTop)
PaddleSprites.add(pBottom)
PaddleSprites.add(cVert)
PaddleSprites.add(cTop)
PaddleSprites.add(cBottom)
BallSprite.add(Ball)

score = Score()
score.__init__()

while True:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    PaddleSprites.update()
    BallSprite.update()
    score.update()

    g_window.blit(gameBackground, [0, 0])
    pygame.draw.circle(g_window, WHITE, (WIDTHWIND // 2, HEIGHTWIND // 2), 80, 1)
    score.draw()

    PaddleSprites.draw(g_window)
    BallSprite.draw(g_window)
    pygame.display.flip()
