import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Shooting Game")

# Set up colors
white = (255, 255, 255)
black = (0, 0, 0)

# Set up the player
player_width = 50
player_height = 50
player_x = (window_width - player_width) // 2
player_y = window_height - player_height - 10
player_speed = 5

# Set up the bullet
bullet_width = 10
bullet_height = 30
bullet_x = 0
bullet_y = player_y
bullet_speed = 10
bullet_state = "ready"  # "ready" means the bullet is not on screen, "fire" means it's moving

# Set up enemies
enemy_width = 50
enemy_height = 50
enemy_x = random.randint(0, window_width - enemy_width)
enemy_y = random.randint(50, 200)
enemy_speed = 3

# Set up the score
score_value = 0
font = pygame.font.Font(None, 36)

def show_score():
    score_text = font.render("Score: " + str(score_value), True, white)
    window.blit(score_text, (10, 10))

def player(x, y):
    pygame.draw.rect(window, white, (x, y, player_width, player_height))

def enemy(x, y):
    pygame.draw.rect(window, white, (x, y, enemy_width, enemy_height))

def fire_bullet(x, y):
    pygame.draw.rect(window, white, (x, y, bullet_width, bullet_height))

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        # Handle player movement
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_x -= player_speed
            elif event.key == pygame.K_RIGHT:
                player_x += player_speed
            elif event.key == pygame.K_SPACE and bullet_state == "ready":
                bullet_x = player_x + player_width // 2 - bullet_width // 2
                bullet_state = "fire"

    # Update the player position
    player_x = max(0, min(player_x, window_width - player_width))

    # Update the bullet position
    if bullet_state == "fire":
        bullet_y -= bullet_speed
        fire_bullet(bullet_x, bullet_y)
        if bullet_y <= 0:
            bullet_state = "ready"
            bullet_y = player_y

    # Update the enemy position
    enemy_x += enemy_speed
    if enemy_x <= 0 or enemy_x >= window_width - enemy_width:
        enemy_speed *= -1
        enemy_y += enemy_height

    # Check for collision
    if bullet_state == "fire" and bullet_x >= enemy_x and bullet_x <= enemy_x + enemy_width and bullet_y <= enemy_y + enemy_height:
        score_value += 1
        bullet_state = "ready"
        bullet_y = player_y
        enemy_x = random.randint(0, window_width - enemy_width)
        enemy_y = random.randint(50, 200)

    # Clear the screen
    window.fill(black)

    # Draw the game elements
    player(player_x, player_y)
    enemy(enemy_x, enemy_y)
    show_score()

    # Update the display
    pygame.display.update()

# Quit the game
pygame.quit()
