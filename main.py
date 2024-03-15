import pygame

pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ginge's first platformer")

# Load player image
player_img = pygame.image.load("player.png")
player_x, player_y = 50, 500  # Initial position
player_y_change = 0
gravity = 0.25
jump = -5  # Reduced jump speed
platforms = [(300, 400), (500, 300), (700, 200), (0, HEIGHT - 10)]  # Added a floor

def draw_player(x, y):
    win.blit(player_img, (x, y))

def draw_platforms():
    for plat in platforms:
        pygame.draw.rect(win, (0, 0, 255), [plat[0], plat[1], 100, 10])

# Game Loop
running = True
jumping = False  # Added jumping variable
while running:

    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Draw the player
    draw_player(player_x, player_y)
    draw_platforms()

    keys = pygame.key.get_pressed()
    on_ground = False
    for plat in platforms:
        if plat[0] < player_x < plat[0] + 100 and plat[1] <= player_y + 32 < plat[1] + 10:
            player_y_change = 0
            player_y = plat[1] - 32
            on_ground = True

    if keys[pygame.K_SPACE] and on_ground and not jumping:
        player_y_change = jump
        jumping = True
    elif not keys[pygame.K_SPACE]:
        jumping = False
    player_y += player_y_change
    player_y_change += gravity

    # Prevent player from moving off the screen
    if player_y < 0:
        player_y = 0
        player_y_change = 0
    elif player_y > HEIGHT - 32:  # Assuming the player's height is 32
        player_y = HEIGHT - 32
        player_y_change = 0

    pygame.display.update()
pygame.quit()
