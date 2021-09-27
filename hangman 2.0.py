import pygame
import math
import random


pygame.init()
WIDTH, HEIGHT = 800, 500
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Hangman 2.0!")


RADIUS = 20
GAP = 20
letters = []
startx = round((WIDTH - (RADIUS * 2 + GAP) * 13) / 2)
starty = 400
A = 65
for i in range(26):
    x = startx + GAP * 2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = starty + ((i // 13) * (GAP + RADIUS * 2))
    letters.append([x, y, chr(A + i), True])

LETTER_FONT = pygame.font.SysFont("Helvetica",36,"normal")
WORD_FONT = pygame.font.SysFont("System", 30,"roman")
TITLE_FONT = pygame.font.SysFont("Verdana", 40,"italic")


images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)




hangman_status = 0
words = ["CROCODILE", "ENGINEER", "SCHOOL", "TECHNOLOGY","PREPARATION","DEVELOPER" ,"APPLE","PYTHON","HANGMAN","DESIGN"]
word = random.choice(words)
guessed = []


CREAM = (255,253,208)
BLACK = (0,0,0)
RED = (255,0,0)
bg = pygame.image.load("bg.png") 



def draw():
    
    
    bg = pygame.image.load("bg.png") 
    win.blit(bg, (0, 0))
    text = TITLE_FONT.render("WELCOME TO HANGMAN 2.0", 1,RED)
    win.blit(text, (WIDTH/2 - text.get_width()/2, 20))

    
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, BLACK)
    win.blit(text, (400, 200))

    
    for letter in letters:
        x, y, ltr, visible = letter
        if visible:
            pygame.draw.circle(win, RED, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, RED)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (150, 100))
    pygame.display.update()


def display_message(message):
    
    pygame.time.delay(1000)
    bg = pygame.image.load("bg.png") 
    win.blit(bg, (0, 0))
    text = WORD_FONT.render(message, 1, BLACK)
    win.blit(text, (WIDTH/2 - text.get_width()/2, HEIGHT/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def main():
    global hangman_status

    FPS = 60
    clock = pygame.time.Clock()
    run = True

    while run:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                m_x, m_y = pygame.mouse.get_pos()
                for letter in letters:
                    x, y, ltr, visible = letter
                    if visible:
                        dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                        if dis < RADIUS:
                            letter[3] = False
                            guessed.append(ltr)
                            if ltr not in word:
                                hangman_status += 1
        
        draw()

        won = True
        for letter in word:
            if letter not in guessed:
                won = False
                break
        
        if won:
            display_message("YOU GUESSED IT RIGHT!!!!!")
        if hangman_status == 6: 

            display_message("OOPS.....YOU KILLED A KIND MAN")
            break
    
while True:
    win.blit(bg,(150,100))
    
    main()
pygame.quit()