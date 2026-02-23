import pygame
import random

# Initialize Pygame
pygame.init()

# Configuration
WIDTH, HEIGHT = 800, 600
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)   # Player
RED   = (255, 0, 0)   # Asteroids
YELLOW = (255, 255, 0) # Lasers
GRAY  = (150, 150, 150)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Shooter - Retro Edition")
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 24, bold=True)

def draw_hud(score):
    score_surf = font.render(f"SCORE:{score:04d}", True, GRAY)
    score_surf.set_alpha(150)
    screen.blit(score_surf, (WIDTH - 180, 20))

def game_loop():
    # Player Settings
    player_w, player_h = 40, 30
    player_x = WIDTH // 2 - player_w // 2
    player_y = HEIGHT - 60
    player_speed = 8

    # Projectiles
    bullets = []
    bullet_speed = -10

    # Asteroids
    asteroids = []
    asteroid_speed = 4
    spawn_timer = 0

    score = 0
    running = True
    game_over = False

    while running:
        while game_over:
            screen.fill(BLACK)
            msg = font.render("MISSION FAILED! ENTER to Restart", True, RED)
            screen.blit(msg, (WIDTH//2 - 250, HEIGHT//2))
            draw_hud(score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False; game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN: game_loop()
                    if event.key == pygame.K_q: running = False; game_over = False

        # --- EVENT HANDLING ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Shoot a bullet from the center of the ship
                    bullet_rect = pygame.Rect(player_x + player_w//2 - 2, player_y, 4, 10)
                    bullets.append(bullet_rect)

        # --- MOVEMENT ---
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_w:
            player_x += player_speed

        # Move Bullets
        for b in bullets[:]:
            b.y += bullet_speed
            if b.bottom < 0:
                bullets.remove(b)

        # --- ASTEROID LOGIC ---
        spawn_timer += 1
        if spawn_timer > 30: # Spawns an asteroid every 30 frames
            ax = random.randint(0, WIDTH - 30)
            asteroids.append(pygame.Rect(ax, -30, 30, 30))
            spawn_timer = 0

        for a in asteroids[:]:
            a.y += asteroid_speed
            if a.top > HEIGHT:
                asteroids.remove(a)
            
            # Check collision with Player
            player_rect = pygame.Rect(player_x, player_y, player_w, player_h)
            if a.colliderect(player_rect):
                game_over = True

        # --- COLLISION DETECTION (Bullet vs Asteroid) ---
        for b in bullets[:]:
            for a in asteroids[:]:
                if b.colliderect(a):
                    if b in bullets: bullets.remove(b)
                    if a in asteroids: asteroids.remove(a)
                    score += 10
                    break

        # --- RENDERING ---
        screen.fill(BLACK)
        
        # Draw Ship (Triangle shape)
        pygame.draw.polygon(screen, GREEN, [
            (player_x, player_y + player_h), 
            (player_x + player_w // 2, player_y), 
            (player_x + player_w, player_y + player_h)
        ])
        
        # Draw Bullets
        for b in bullets:
            pygame.draw.rect(screen, YELLOW, b)
            
        # Draw Asteroids
        for a in asteroids:
            pygame.draw.rect(screen, RED, a)

        draw_hud(score)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()