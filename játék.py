import pygame
import random
import sys
import os

# Inicializálás
pygame.init()

# Képernyő beállítás
WIDTH, HEIGHT = 600, 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Fantasy Akadálykerülő")

# Betöltés
background = pygame.image.load("fantasy_game/background.jpg")
player_img = pygame.image.load("fantasy_game/wizard.png")
obstacle_img = pygame.image.load("fantasy_game/fireball.png")

# Színek
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Fontok
font = pygame.font.SysFont(None, 36)

# Globális változók
def reset_game():
    return {
        "player_x": WIDTH // 2 - 25,
        "player_y": HEIGHT - 60,
        "player_speed": 7,
        "obstacles": [create_obstacle() for _ in range(3)],
        "obstacle_speed": 4,
        "score": 0,
        "start_ticks": pygame.time.get_ticks(),
        "game_over": False,
        "highscore": load_highscore()
    }

def create_obstacle():
    return pygame.Rect(random.randint(0, WIDTH - 40), random.randint(-300, -20), 40, 40)

def draw_text(text, size, color, x, y, center=True):
    font_obj = pygame.font.SysFont(None, size)
    text_surface = font_obj.render(text, True, color)
    rect = text_surface.get_rect()
    if center:
        rect.center = (x, y)
    else:
        rect.topleft = (x, y)
    screen.blit(text_surface, rect)

def save_highscore(score):
    with open("highscore.txt", "w") as f:
        f.write(str(score))

def load_highscore():
    if os.path.exists("highscore.txt"):
        with open("highscore.txt", "r") as f:
            return int(f.read())
    return 0

def main_menu():
    menu = True
    while menu:
        screen.fill(BLACK)
        draw_text("Fantasy Akadálykerülő", 48, WHITE, WIDTH // 2, HEIGHT // 4)
        draw_text("1. Könnyű", 36, WHITE, WIDTH // 2, HEIGHT // 2 - 40)
        draw_text("2. Közepes", 36, WHITE, WIDTH // 2, HEIGHT // 2)
        draw_text("3. Nehéz", 36, WHITE, WIDTH // 2, HEIGHT // 2 + 40)
        draw_text("Q - Kilépés", 28, RED, WIDTH // 2, HEIGHT - 40)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return 4
                elif event.key == pygame.K_2:
                    return 7
                elif event.key == pygame.K_3:
                    return 10
                elif event.key == pygame.K_q:
                    pygame.quit(); sys.exit()

def game_loop(initial_speed):
    clock = pygame.time.Clock()
    state = reset_game()
    state["obstacle_speed"] = initial_speed

    while True:
        clock.tick(60)
        screen.blit(background, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit(); sys.exit()

        if not state["game_over"]:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT] and state["player_x"] > 0:
                state["player_x"] -= state["player_speed"]
            if keys[pygame.K_RIGHT] and state["player_x"] < WIDTH - 50:
                state["player_x"] += state["player_speed"]

            player_rect = pygame.Rect(state["player_x"], state["player_y"], 50, 50)
            screen.blit(player_img, (state["player_x"], state["player_y"]))

            for obs in state["obstacles"]:
                obs.y += state["obstacle_speed"]
                screen.blit(obstacle_img, (obs.x, obs.y))
                if obs.y > HEIGHT:
                    obs.y = random.randint(-150, -20)
                    obs.x = random.randint(0, WIDTH - 40)
                    state["score"] += 1
                    if state["score"] % 10 == 0:
                        state["obstacle_speed"] += 1
                        state["obstacles"].append(create_obstacle())

                if player_rect.colliderect(obs):
                    state["game_over"] = True
                    if state["score"] > state["highscore"]:
                        save_highscore(state["score"])

            elapsed = (pygame.time.get_ticks() - state["start_ticks"]) // 1000
            draw_text(f"Pontszám: {state["score"]}", 28, WHITE, 10, 10, center=False)
            draw_text(f"Idő: {elapsed} s", 28, WHITE, 10, 40, center=False)
            draw_text(f"Rekord: {state["highscore"]}", 28, WHITE, 10, 70, center=False)

        else:
            draw_text("Game Over! Nyomj [R] az újrakezdéshez", 36, RED, WIDTH // 2, HEIGHT // 2)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_r]:
                return  # Vissza főmenübe

        pygame.display.flip()

# Fő futtatás
while True:
    speed = main_menu()
    game_loop(speed)