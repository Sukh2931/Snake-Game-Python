
import pygame
import random
import os

pygame.init()

# ---------------- WINDOW SETTINGS ----------------
WIDTH = 800
HEIGHT = 600
CELL_SIZE = 25

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game - Python Project")

clock = pygame.time.Clock()

# ---------------- COLOURS ----------------
BLACK = (15, 18, 30)
GREEN = (50, 220, 100)
DARK_GREEN = (25, 150, 70)
RED = (255, 75, 75)
WHITE = (255, 255, 255)
YELLOW = (255, 210, 70)
GREY = (150, 160, 180)

# ---------------- FONTS ----------------
font = pygame.font.SysFont("Arial", 28, bold=True)
big_font = pygame.font.SysFont("Arial", 55, bold=True)
small_font = pygame.font.SysFont("Arial", 20)

BEST_FILE = "best_score.txt"

# ---------------- BEST SCORE ----------------
def load_best():
    try:
        with open(BEST_FILE, "r") as file:
            return int(file.read())
    except:
        return 0


def save_best(score):
    with open(BEST_FILE, "w") as file:
        file.write(str(score))


best_score = load_best()

# ---------------- FOOD GENERATION ----------------
def create_food(snake):
    while True:
        food = (
            random.randrange(0, WIDTH // CELL_SIZE) * CELL_SIZE,
            random.randrange(0, HEIGHT // CELL_SIZE) * CELL_SIZE
        )

        if food not in snake:
            return food


# ---------------- RESET GAME ----------------
def reset_game():
    snake = [
        (400, 300),
        (375, 300),
        (350, 300)
    ]

    direction = (CELL_SIZE, 0)
    food = create_food(snake)
    score = 0

    return snake, direction, food, score


snake, direction, food, score = reset_game()

next_direction = direction

game_started = False
game_over = False
paused = False

# ---------------- DRAW FUNCTIONS ----------------
def draw_text(text, selected_font, colour, y):
    image = selected_font.render(text, True, colour)
    rect = image.get_rect(center=(WIDTH // 2, y))
    screen.blit(image, rect)


def draw_background():
    screen.fill(BLACK)

    for x in range(0, WIDTH, CELL_SIZE):
        pygame.draw.line(
            screen, (27, 32, 48),
            (x, 0), (x, HEIGHT)
        )

    for y in range(0, HEIGHT, CELL_SIZE):
        pygame.draw.line(
            screen, (27, 32, 48),
            (0, y), (WIDTH, y)
        )


def draw_snake():
    for index, part in enumerate(snake):
        colour = GREEN if index == 0 else DARK_GREEN

        pygame.draw.rect(
            screen,
            colour,
            (
                part[0] + 2,
                part[1] + 2,
                CELL_SIZE - 4,
                CELL_SIZE - 4
            ),
            border_radius=6
        )


def draw_food():
    pygame.draw.circle(
        screen,
        RED,
        (
            food[0] + CELL_SIZE // 2,
            food[1] + CELL_SIZE // 2
        ),
        CELL_SIZE // 2 - 3
    )


def draw_score():
    score_text = font.render(
        f"Score: {score}", True, WHITE
    )

    best_text = font.render(
        f"Best: {best_score}", True, YELLOW
    )

    screen.blit(score_text, (20, 15))
    screen.blit(best_text, (WIDTH - 180, 15))


# ---------------- MAIN GAME LOOP ----------------
running = True

while running:

    # Speed increases after every 20 points
    speed = min(5 + (score // 20), 20)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:

            if event.key == pygame.K_ESCAPE:
                running = False

            # Start game
            if not game_started and not game_over:
                if event.key == pygame.K_SPACE:
                    game_started = True

            # Restart after game over
            elif game_over:
                if event.key == pygame.K_r:
                    snake, direction, food, score = reset_game()
                    next_direction = direction
                    game_over = False
                    paused = False
                    game_started = True

            # Pause and resume
            elif event.key == pygame.K_p:
                paused = not paused

            # Snake movement
            elif not paused:

                if event.key == pygame.K_UP:
                    if direction != (0, CELL_SIZE):
                        next_direction = (0, -CELL_SIZE)

                elif event.key == pygame.K_DOWN:
                    if direction != (0, -CELL_SIZE):
                        next_direction = (0, CELL_SIZE)

                elif event.key == pygame.K_LEFT:
                    if direction != (CELL_SIZE, 0):
                        next_direction = (-CELL_SIZE, 0)

                elif event.key == pygame.K_RIGHT:
                    if direction != (-CELL_SIZE, 0):
                        next_direction = (CELL_SIZE, 0)

    # ---------------- GAME LOGIC ----------------
    if game_started and not game_over and not paused:

        direction = next_direction

        head_x = snake[0][0] + direction[0]
        head_y = snake[0][1] + direction[1]

        new_head = (head_x, head_y)

        # Wall collision
        if (
            head_x < 0 or
            head_x >= WIDTH or
            head_y < 0 or
            head_y >= HEIGHT
        ):
            game_over = True

        # Self collision
        elif new_head in snake:
            game_over = True

        else:
            snake.insert(0, new_head)

            # Eat food
            if new_head == food:

                score += 10

                food = create_food(snake)

                if score > best_score:
                    best_score = score
                    save_best(best_score)

            else:
                snake.pop()

    # ---------------- DRAW EVERYTHING ----------------
    draw_background()
    draw_snake()
    draw_food()
    draw_score()

    # Start screen
    if not game_started:
        draw_text(
            "SNAKE GAME",
            big_font,
            GREEN,
            220
        )

        draw_text(
            "Press SPACE to Start",
            font,
            WHITE,
            290
        )

        draw_text(
            "Use Arrow Keys to Move",
            small_font,
            GREY,
            340
        )

    # Pause screen
    if paused:
        draw_text(
            "PAUSED",
            big_font,
            YELLOW,
            270
        )

        draw_text(
            "Press P to Resume",
            font,
            WHITE,
            330
        )

    # Game over screen
    if game_over:
        draw_text(
            "GAME OVER!",
            big_font,
            RED,
            240
        )

        draw_text(
            f"Your Score: {score}",
            font,
            WHITE,
            310
        )

        draw_text(
            "Press R to Restart",
            font,
            YELLOW,
            370
        )

        draw_text(
            "Press ESC to Exit",
            small_font,
            GREY,
            410
        )

    pygame.display.update()

    # Apply current speed
    if game_started and not paused and not game_over:
        clock.tick(speed)
    else:
        clock.tick(15)


pygame.quit()
