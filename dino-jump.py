import pygame
import random

# Initialize Pygame
pygame.init()

# Configuration
WIDTH, HEIGHT = 800, 400
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0) # Dino
RED   = (255, 0, 0) # Obstacles
GRAY  = (150, 150, 150)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dino Jump - Retro Edition")
clock = pygame.time.Clock()

# Fonts
pixel_font = pygame.font.SysFont("monospace", 24, bold=True)

def draw_hud(score):
    score_surf = pixel_font.render(f"SCORE:{score:04d}", True, GRAY)
    score_surf.set_alpha(150)
    screen.blit(score_surf, (WIDTH - 180, 20))

def game_loop():
    # Dino Physics
    dino_w, dino_h = 40, 40
    dino_x = 50
    dino_y = HEIGHT - 50 - dino_h
    
    velocity_y = 0
    gravity = 0.8
    jump_strength = -16
    is_jumping = False

    # Obstacle Settings
    obs_w, obs_h = 30, 50
    obstacles = []
    obstacle_timer = 0
    
    score = 0
    running = True
    game_over = False

    while running:
        while game_over:
            screen.fill(BLACK)
            msg = pixel_font.render("GAME OVER! Press ENTER to Restart", True, RED)
            screen.blit(msg, (WIDTH//2 - 250, HEIGHT//2))
            draw_hud(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop()
                    if event.key == pygame.K_q:
                        running = False
                        game_over = False

        # --- EVENT HANDLING ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_SPACE or event.key == pygame.K_UP) and not is_jumping:
                    velocity_y = jump_strength
                    is_jumping = True

        # --- DINO PHYSICS ---
        velocity_y += gravity
        dino_y += velocity_y

        # Floor collision
        if dino_y >= HEIGHT - 50 - dino_h:
            dino_y = HEIGHT - 50 - dino_h
            is_jumping = False

        # --- OBSTACLE LOGIC ---
        obstacle_timer += 1
        # Randomize spawn time
        if obstacle_timer > random.randint(60, 120):
            obstacles.append(pygame.Rect(WIDTH, HEIGHT - 50 - obs_h, obs_w, obs_h))
            obstacle_timer = 0

        for obs in obstacles[:]:
            obs.x -= 7  # Speed of the game
            if obs.right < 0:
                obstacles.remove(obs)
                score += 1
            
            # Collision Detection
            dino_rect = pygame.Rect(dino_x, dino_y, dino_w, dino_h)
            if dino_rect.colliderect(obs):
                game_over = True

        # --- RENDERING ---
        screen.fill(BLACK)
        
        # Ground
        pygame.draw.line(screen, GRAY, (0, HEIGHT - 50), (WIDTH, HEIGHT - 50), 2)
        
        # Dino (Green)
        pygame.draw.rect(screen, GREEN, (dino_x, dino_y, dino_w, dino_h))
        
        # Obstacles (Red)
        for obs in obstacles:
            pygame.draw.rect(screen, RED, obs)

        draw_hud(score)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()