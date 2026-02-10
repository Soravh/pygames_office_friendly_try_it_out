import pygame
import random

# Initialize Pygame
pygame.init()

# Configuration
WIDTH, HEIGHT = 600, 400
SNAKE_SIZE = 10
SPEED = 15

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
GRAY  = (150, 150, 150)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Snake - Retro HUD Edition')
clock = pygame.time.Clock()

# Fonts
score_font = pygame.font.SysFont("monospace", 22, bold=True)
msg_font = pygame.font.SysFont("monospace", 25, bold=True)

def draw_transparent_score(score):
    score_str = f"SCORE:{score:02d}"
    text_surface = score_font.render(score_str, True, GRAY)
    text_surface.set_alpha(150)
    text_rect = text_surface.get_rect(topright=(WIDTH - 20, 20))
    screen.blit(text_surface, text_rect)

def show_message(msg, color, y_offset=0):
    mesg = msg_font.render(msg, True, color)
    rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2 + y_offset))
    screen.blit(mesg, rect)

def game_loop():
    x, y = WIDTH // 2, HEIGHT // 2
    dx, dy = 0, 0
    snake_list = []
    snake_len = 1
    
    fx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
    fy = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0

    running = True
    game_close = False # Flag for the Game Over state

    while running:

        # --- GAME OVER SCREEN ---
        while game_close:
            screen.fill(BLACK)
            show_message("YOU BIT YOURSELF!", RED, -20)
            show_message("Press ENTER to Retry or Q to Quit", WHITE, 20)
            draw_transparent_score(snake_len - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        running = False
                        game_close = False
                    if event.key == pygame.K_RETURN: # Press Enter to restart
                        game_loop() # This restarts the function
                if event.type == pygame.QUIT:
                    running = False
                    game_close = False

        # --- NORMAL GAMEPLAY EVENTS ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and dx == 0:
                    dx, dy = -SNAKE_SIZE, 0
                elif event.key == pygame.K_RIGHT and dx == 0:
                    dx, dy = SNAKE_SIZE, 0
                elif event.key == pygame.K_UP and dy == 0:
                    dx, dy = 0, -SNAKE_SIZE
                elif event.key == pygame.K_DOWN and dy == 0:
                    dx, dy = 0, SNAKE_SIZE

        x += dx
        y += dy

        # Wrap Around Logic
        if x >= WIDTH: x = 0
        elif x < 0: x = WIDTH - SNAKE_SIZE
        if y >= HEIGHT: y = 0
        elif y < 0: y = HEIGHT - SNAKE_SIZE

        screen.fill(BLACK)
        pygame.draw.rect(screen, RED, [fx, fy, SNAKE_SIZE, SNAKE_SIZE])
        
        head = [x, y]
        snake_list.append(head)
        if len(snake_list) > snake_len:
            del snake_list[0]

        # Check self-collision
        for segment in snake_list[:-1]:
            if segment == head and snake_len > 1:
                game_close = True # Trigger the Game Over state

        for segment in snake_list:
            pygame.draw.rect(screen, GREEN, [segment[0], segment[1], SNAKE_SIZE, SNAKE_SIZE])

        draw_transparent_score(snake_len - 1)
        pygame.display.update()

        if x == fx and y == fy:
            fx = round(random.randrange(0, WIDTH - SNAKE_SIZE) / 10.0) * 10.0
            fy = round(random.randrange(0, HEIGHT - SNAKE_SIZE) / 10.0) * 10.0
            snake_len += 1

        clock.tick(SPEED)

    pygame.quit()

if __name__ == "__main__":
    game_loop()