import pygame
import subprocess
import sys

# Initialiser Pygame
pygame.init()

# Définir les dimensions de la fenêtre de jeu
display_width = 1200
display_height = 720

# Définir les couleurs
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
gray = (50, 50, 50)

# Créer la fenêtre de jeu
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Menu de Jeux')

# Définir l'horloge pour contrôler la vitesse du jeu
clock = pygame.time.Clock()

# Fonction pour afficher le texte des objets
def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

# Fonction pour afficher un message sur l'écran
def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 50)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    pygame.display.update()
    pygame.time.wait(2000)

# Fonction pour afficher le menu principal
def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        gameDisplay.fill(gray)
        largeText = pygame.font.Font('freesansbold.ttf', 115)
        TextSurf, TextRect = text_objects("Menu de Jeux", largeText)
        TextRect.center = ((display_width / 2), (display_height / 2 - 100))
        gameDisplay.blit(TextSurf, TextRect)

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Boutons pour sélectionner les jeux
        if button("Course en voiture", 250, 400, 200, 100, green, black, mouse, click):
            launch_game("car_game.py")
            intro = False
        if button("Jeu de Serpent", 500, 400, 200, 100, red, black, mouse, click):
            launch_game("snake_game.py")
            intro = False
        if button("Pong", 750, 400, 200, 100, red, black, mouse, click):
            launch_game("pong_game.py")
            intro = False

        pygame.display.update()
        clock.tick(15)

# Fonction pour dessiner des boutons
def button(msg, x, y, w, h, ic, ac, mouse, click):
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))
        if click[0] == 1:
            return True
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)

    return False

# Fonction pour lancer un jeu
def launch_game(game_script):
    try:
        subprocess.Popen([sys.executable, game_script])
        pygame.quit()
        sys.exit()
    except Exception as e:
        message_display(f"Erreur: {e}")

# Démarrer le menu principal
game_intro()
pygame.quit()
sys.exit()
