<<<<<<< HEAD
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Configuration
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 200, 12
BALL_RADIUS = 8
BRICK_ROWS = 6
BRICK_COLS = 10
BRICK_HEIGHT = 25
BRICK_WIDTH = WIDTH // BRICK_COLS - 4
FPS = 60 

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  
RED   = (200, 0, 0)      # Standard Brick
ORANGE = (255, 165, 0)   # TNT Brick
GRAY  = (150, 150, 150) 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Breakout - TNT Bomb Edition')
clock = pygame.time.Clock()

# Fonts
score_font = pygame.font.SysFont("monospace", 24, bold=True)
msg_font = pygame.font.SysFont("monospace", 40, bold=True)

def draw_hud(score):
    score_str = f"SCORE:{score:02d}"
    text_surface = score_font.render(score_str, True, GRAY)
    text_surface.set_alpha(150)
    text_rect = text_surface.get_rect(topright=(WIDTH - 30, 30))
    screen.blit(text_surface, text_rect)

def show_message(msg, color):
    mesg = msg_font.render(msg, True, color)
    rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(mesg, rect)

def game_loop():
    paddle_x = (WIDTH - PADDLE_WIDTH) // 2
    paddle_y = HEIGHT - 40
    paddle_speed = 14 

    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    current_speed = 4 
    ball_dx = random.choice([-current_speed, current_speed])
    ball_dy = -current_speed

    # BRICK SETUP
    bricks = []
    tnt_bricks = [] # Special list for TNT
    
    for r in range(BRICK_ROWS):
        for c in range(BRICK_COLS):
            brick_rect = pygame.Rect(c * (BRICK_WIDTH + 4) + 2, r * (BRICK_HEIGHT + 4) + 70, BRICK_WIDTH, BRICK_HEIGHT)
            
            # 10% chance for a brick to be a TNT bomb
            if random.random() < 0.10:
                tnt_bricks.append(brick_rect)
            else:
                bricks.append(brick_rect)

    score = 0
    running = True
    game_over = False
    win = False

    while running:
        while game_over or win:
            screen.fill(BLACK)
            if win: show_message("CHAMPION!", GREEN)
            else: show_message("GAME OVER", RED)
            retry_msg = score_font.render("Press ENTER to Restart or Q to Quit", True, WHITE)
            screen.blit(retry_msg, (WIDTH//2 - 220, HEIGHT//2 + 60))
            draw_hud(score)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: running = False; game_over = False; win = False
                    if event.key == pygame.K_RETURN: game_loop()
                if event.type == pygame.QUIT: running = False; game_over = False; win = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        # Difficulty Shift
        if score >= 20 and current_speed == 4:
            current_speed = 7
            ball_dx = (ball_dx / abs(ball_dx)) * current_speed
            ball_dy = (ball_dy / abs(ball_dy)) * current_speed

        # Paddle Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0: paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH: paddle_x += paddle_speed

        ball_x += ball_dx
        ball_y += ball_dy

        # Wall Bounces
        if ball_x <= 0 or ball_x >= WIDTH - BALL_RADIUS: ball_dx *= -1
        if ball_y <= 0: ball_dy *= -1
        if ball_y >= HEIGHT: game_over = True

        # Paddle Collision
        paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        if paddle_rect.collidepoint(ball_x, ball_y + BALL_RADIUS):
            hit_pos = (ball_x - (paddle_x + PADDLE_WIDTH/2)) / (PADDLE_WIDTH/2)
            ball_dx = hit_pos * current_speed
            ball_dy = -current_speed

        # --- COLLISION WITH TNT BRICKS ---
        for tnt in tnt_bricks[:]:
            if tnt.collidepoint(ball_x, ball_y):
                # EXPLOSION LOGIC
                explosion_radius = 80 
                # Create a blast area
                blast_rect = pygame.Rect(tnt.centerx - explosion_radius, tnt.centery - explosion_radius, 
                                         explosion_radius*2, explosion_radius*2)
                
                # Check which normal bricks are inside the blast
                for b in bricks[:]:
                    if blast_rect.colliderect(b):
                        bricks.remove(b)
                        score += 1
                
                tnt_bricks.remove(tnt)
                score += 1
                ball_dy *= -1
                break

        # --- COLLISION WITH NORMAL BRICKS ---
        for brick in bricks[:]:
            if brick.collidepoint(ball_x, ball_y):
                bricks.remove(brick)
                ball_dy *= -1
                score += 1
                break 

        if not bricks and not tnt_bricks: win = True

        # Rendering
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, paddle_rect)
        pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)
        
        for brick in bricks: pygame.draw.rect(screen, RED, brick)
        for tnt in tnt_bricks: pygame.draw.rect(screen, ORANGE, tnt) # Orange for TNT
        
        draw_hud(score)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
=======
import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Configuration
WIDTH, HEIGHT = 800, 600
PADDLE_WIDTH, PADDLE_HEIGHT = 200, 12
BALL_RADIUS = 8
BRICK_ROWS = 6
BRICK_COLS = 10
BRICK_HEIGHT = 25
BRICK_WIDTH = WIDTH // BRICK_COLS - 4
FPS = 60 

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)  
RED   = (200, 0, 0)      # Standard Brick
ORANGE = (255, 165, 0)   # TNT Brick
GRAY  = (150, 150, 150) 

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Breakout - TNT Bomb Edition')
clock = pygame.time.Clock()

# Fonts
score_font = pygame.font.SysFont("monospace", 24, bold=True)
msg_font = pygame.font.SysFont("monospace", 40, bold=True)

def draw_hud(score):
    score_str = f"SCORE:{score:02d}"
    text_surface = score_font.render(score_str, True, GRAY)
    text_surface.set_alpha(150)
    text_rect = text_surface.get_rect(topright=(WIDTH - 30, 30))
    screen.blit(text_surface, text_rect)

def show_message(msg, color):
    mesg = msg_font.render(msg, True, color)
    rect = mesg.get_rect(center=(WIDTH/2, HEIGHT/2))
    screen.blit(mesg, rect)

def game_loop():
    paddle_x = (WIDTH - PADDLE_WIDTH) // 2
    paddle_y = HEIGHT - 40
    paddle_speed = 14 

    ball_x, ball_y = WIDTH // 2, HEIGHT // 2
    current_speed = 4 
    ball_dx = random.choice([-current_speed, current_speed])
    ball_dy = -current_speed

    # BRICK SETUP
    bricks = []
    tnt_bricks = [] # Special list for TNT
    
    for r in range(BRICK_ROWS):
        for c in range(BRICK_COLS):
            brick_rect = pygame.Rect(c * (BRICK_WIDTH + 4) + 2, r * (BRICK_HEIGHT + 4) + 70, BRICK_WIDTH, BRICK_HEIGHT)
            
            # 10% chance for a brick to be a TNT bomb
            if random.random() < 0.10:
                tnt_bricks.append(brick_rect)
            else:
                bricks.append(brick_rect)

    score = 0
    running = True
    game_over = False
    win = False

    while running:
        while game_over or win:
            screen.fill(BLACK)
            if win: show_message("CHAMPION!", GREEN)
            else: show_message("GAME OVER", RED)
            retry_msg = score_font.render("Press ENTER to Restart or Q to Quit", True, WHITE)
            screen.blit(retry_msg, (WIDTH//2 - 220, HEIGHT//2 + 60))
            draw_hud(score)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q: running = False; game_over = False; win = False
                    if event.key == pygame.K_RETURN: game_loop()
                if event.type == pygame.QUIT: running = False; game_over = False; win = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT: running = False

        # Difficulty Shift
        if score >= 20 and current_speed == 4:
            current_speed = 7
            ball_dx = (ball_dx / abs(ball_dx)) * current_speed
            ball_dy = (ball_dy / abs(ball_dy)) * current_speed

        # Paddle Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and paddle_x > 0: paddle_x -= paddle_speed
        if keys[pygame.K_RIGHT] and paddle_x < WIDTH - PADDLE_WIDTH: paddle_x += paddle_speed

        ball_x += ball_dx
        ball_y += ball_dy

        # Wall Bounces
        if ball_x <= 0 or ball_x >= WIDTH - BALL_RADIUS: ball_dx *= -1
        if ball_y <= 0: ball_dy *= -1
        if ball_y >= HEIGHT: game_over = True

        # Paddle Collision
        paddle_rect = pygame.Rect(paddle_x, paddle_y, PADDLE_WIDTH, PADDLE_HEIGHT)
        if paddle_rect.collidepoint(ball_x, ball_y + BALL_RADIUS):
            hit_pos = (ball_x - (paddle_x + PADDLE_WIDTH/2)) / (PADDLE_WIDTH/2)
            ball_dx = hit_pos * current_speed
            ball_dy = -current_speed

        # --- COLLISION WITH TNT BRICKS ---
        for tnt in tnt_bricks[:]:
            if tnt.collidepoint(ball_x, ball_y):
                # EXPLOSION LOGIC
                explosion_radius = 80 
                # Create a blast area
                blast_rect = pygame.Rect(tnt.centerx - explosion_radius, tnt.centery - explosion_radius, 
                                         explosion_radius*2, explosion_radius*2)
                
                # Check which normal bricks are inside the blast
                for b in bricks[:]:
                    if blast_rect.colliderect(b):
                        bricks.remove(b)
                        score += 1
                
                tnt_bricks.remove(tnt)
                score += 1
                ball_dy *= -1
                break

        # --- COLLISION WITH NORMAL BRICKS ---
        for brick in bricks[:]:
            if brick.collidepoint(ball_x, ball_y):
                bricks.remove(brick)
                ball_dy *= -1
                score += 1
                break 

        if not bricks and not tnt_bricks: win = True

        # Rendering
        screen.fill(BLACK)
        pygame.draw.rect(screen, GREEN, paddle_rect)
        pygame.draw.circle(screen, WHITE, (int(ball_x), int(ball_y)), BALL_RADIUS)
        
        for brick in bricks: pygame.draw.rect(screen, RED, brick)
        for tnt in tnt_bricks: pygame.draw.rect(screen, ORANGE, tnt) # Orange for TNT
        
        draw_hud(score)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
>>>>>>> 5571346 (Initial commit: Added 4 retro games and arcade launcher)
    game_loop()