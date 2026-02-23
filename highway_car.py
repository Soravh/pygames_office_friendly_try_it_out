import pygame
import random

# Initialize Pygame
pygame.init()

# Configuration
WIDTH, HEIGHT = 500, 600
FPS = 60

# --- EYE-FRIENDLY COLORS ---
BG_COLOR    = (30, 32, 38)
ROAD_COLOR  = (45, 47, 54)
PLAYER_COLOR = (100, 210, 210) 
ENEMY_COLOR  = (210, 100, 110) 
FUEL_COLOR   = (120, 180, 120) 
TEXT_COLOR   = (200, 200, 200) 
LANE_COLOR   = (180, 160, 100) 
WHEEL_COLOR  = (10, 10, 10)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Road Racer: Final Edition")
clock = pygame.time.Clock()
font = pygame.font.SysFont("monospace", 22, bold=True)
small_font = pygame.font.SysFont("monospace", 18, bold=True)

def draw_pixel_car(x, y, color):
    # Main Body
    pygame.draw.rect(screen, color, (x, y + 10, 45, 60), border_radius=2)
    # Cockpit
    pygame.draw.rect(screen, (40, 40, 40), (x + 10, y + 25, 25, 20), border_radius=2)
    # Hood
    pygame.draw.rect(screen, color, (x + 5, y, 35, 15), border_radius=2)
    # Wheels
    pygame.draw.rect(screen, WHEEL_COLOR, (x - 5, y + 10, 8, 15))
    pygame.draw.rect(screen, WHEEL_COLOR, (x - 5, y + 55, 8, 15))
    pygame.draw.rect(screen, WHEEL_COLOR, (x + 42, y + 10, 8, 15))
    pygame.draw.rect(screen, WHEEL_COLOR, (x + 42, y + 55, 8, 15))

def draw_hud(score, fuel):
    score_surf = font.render(f"KM:{score:04d}", True, TEXT_COLOR)
    fuel_text = font.render("FUEL:", True, TEXT_COLOR)
    screen.blit(score_surf, (20, 20))
    screen.blit(fuel_text, (20, 50))
    pygame.draw.rect(screen, (60, 60, 70), (80, 55, 100, 15))
    current_fuel_color = FUEL_COLOR if fuel > 30 else ENEMY_COLOR
    pygame.draw.rect(screen, current_fuel_color, (80, 55, fuel, 15))

def game_loop():
    car_w, car_h = 45, 80
    player_x = WIDTH // 2 - car_w // 2
    player_y = HEIGHT - 120
    player_speed = 8

    enemies = []
    fuels = []
    scroll_speed = 7
    fuel = 100
    score = 0
    spawn_timer = 0
    lane_y = 0
    
    running = True
    game_over = False

    while running:
        while game_over:
            screen.fill(BG_COLOR)
            
            # --- UPDATED GAME OVER UI ---
            reason_text = "ACCIDENT!" if fuel > 0 else "OUT OF FUEL!"
            msg = font.render(reason_text, True, ENEMY_COLOR)
            retry_msg = small_font.render("Press ENTER to Restart", True, TEXT_COLOR)
            quit_msg = small_font.render("Press Q to Quit", True, TEXT_COLOR)
            
            screen.blit(msg, (WIDTH//2 - msg.get_width()//2, HEIGHT//2 - 40))
            screen.blit(retry_msg, (WIDTH//2 - retry_msg.get_width()//2, HEIGHT//2 + 10))
            screen.blit(quit_msg, (WIDTH//2 - quit_msg.get_width()//2, HEIGHT//2 + 40))
            
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game_over = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        game_loop() # Restart
                    if event.key == pygame.K_q:
                        running = False # Return to menu/Exit
                        game_over = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        # --- LOGIC ---
        fuel -= 0.10 
        if fuel <= 0: game_over = True

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player_x > 105: player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < 395 - car_w: player_x += player_speed

        spawn_timer += 1
        if spawn_timer > max(30, 50 - (score // 5)):
            lanes = [120, 225, 330]
            random.shuffle(lanes)
            num_enemies = 2 if random.random() < 0.2 else 1
            for i in range(num_enemies):
                enemies.append(pygame.Rect(lanes[i], -100, car_w, car_h))
            if random.random() < 0.35:
                fuels.append(pygame.Rect(random.choice(lanes), -250, 20, 20))
            spawn_timer = 0

        for e in enemies[:]:
            e.y += scroll_speed
            if e.top > HEIGHT: 
                enemies.remove(e)
                score += 1
                if score % 10 == 0: scroll_speed += 0.5 
            if e.colliderect(pygame.Rect(player_x, player_y, car_w, car_h)):
                game_over = True

        for f in fuels[:]:
            f.y += scroll_speed
            if f.colliderect(pygame.Rect(player_x, player_y, car_w, car_h)):
                fuel = min(100, fuel + 40)
                fuels.remove(f)
            elif f.top > HEIGHT:
                fuels.remove(f)

        # --- RENDERING ---
        screen.fill(BG_COLOR)
        pygame.draw.rect(screen, ROAD_COLOR, (100, 0, 300, HEIGHT))
        
        lane_y += scroll_speed
        if lane_y > 80: lane_y = 0
        for y in range(-80, HEIGHT, 80):
            pygame.draw.rect(screen, LANE_COLOR, (WIDTH//2 - 4, y + lane_y, 8, 35))

        draw_pixel_car(player_x, player_y, PLAYER_COLOR)
        for e in enemies: 
            draw_pixel_car(e.x, e.y, ENEMY_COLOR)
        for f in fuels: 
            pygame.draw.circle(screen, FUEL_COLOR, (f.centerx, f.centery), 12)

        draw_hud(score, int(fuel))
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    game_loop()