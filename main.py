import random
import pygame

WIDTH = 800
HEIGHT = 600
FPS = 60


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/avatar.png").convert_alpha()
        self.rect = self.image.get_rect(center=(WIDTH / 2, HEIGHT - 60))

    def update(self, dt):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.rect.x += 300 * dt
        if keys[pygame.K_LEFT]:
            self.rect.x -= 300 * dt


class Star(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("assets/ball.png").convert_alpha()
        x = random.randint(0, WIDTH - 32)
        self.rect = self.image.get_rect(topleft=(x, -32))

    def update(self, dt):
        self.rect.y += 150 * dt
        if self.rect.top > HEIGHT:
            self.kill()


pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

player = Player()
stars = pygame.sprite.Group()
score = 0
timer = 0

running = True
while running:
    dt = clock.tick(FPS) / 1000

    # 1. Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 2. Update
    timer += dt
    if timer > 1:
        timer = 0
        stars.add(Star())

    player.update(dt)
    stars.update(dt)

    hits = pygame.sprite.spritecollide(player, stars, True)
    score += len(hits)
    pygame.display.set_caption(f"Bälle: {score}")

    # 3. Zeichnen
    background = pygame.image.load("background.jpg").convert_alpha()
    screen.blit(background, (0, 0))
    stars.draw(screen)
    screen.blit(player.image, player.rect)
    pygame.display.flip()

pygame.quit()