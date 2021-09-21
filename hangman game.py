import pygame

pygame.init()
W,H = 800,500
Win =  pygame.display.set_mode((W,H))
pygame.display.set_caption("Hangman Game!")

print("Welcome to Hangman")

FPS = 60
clock = pygame.time.Clock()
run = True 

while run : clock.tick(FPS)

for event in pygame.event.get():
    if event.type == pygame.QUIT:
        run = False

        pygame.display.update()
        


pygame.quit()

