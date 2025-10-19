import pygame
import random

pygame.mixer.init()

# Load sounds
PADDLE_HIT_SOUND = pygame.mixer.Sound("assets/paddle_hit.wav")
WALL_BOUNCE_SOUND = pygame.mixer.Sound("assets/wall_bounce.wav")
SCORE_SOUND = pygame.mixer.Sound("assets/score.wav")

class Ball:
    def __init__(self, x, y, width, height, screen_width, screen_height):
        self.original_x = x
        self.original_y = y
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.velocity_x = random.choice([-5, 5])
        self.velocity_y = random.choice([-3, 3])
        self.last_collision = None  # "player" or "ai"

    def move(self):
        self.x += self.velocity_x
        self.y += self.velocity_y

        # Bounce off top/bottom walls
        if self.y <= 0:
            self.y = 0
            self.velocity_y *= -1
            WALL_BOUNCE_SOUND.play()
        elif self.y + self.height >= self.screen_height:
            self.y = self.screen_height - self.height
            self.velocity_y *= -1
            WALL_BOUNCE_SOUND.play()

    def check_collision(self, player, ai):
        # Predictive collision along X axis
        next_rect = pygame.Rect(
            self.x + self.velocity_x,
            self.y + self.velocity_y,
            self.width,
            self.height
        )

        # Player paddle
        if next_rect.colliderect(player.rect()) and self.last_collision != "player":
            self.x = player.x + player.width + 1
            self.velocity_x *= -1
            self.last_collision = "player"
            PADDLE_HIT_SOUND.play()
        # AI paddle
        elif next_rect.colliderect(ai.rect()) and self.last_collision != "ai":
            self.x = ai.x - self.width - 1
            self.velocity_x *= -1
            self.last_collision = "ai"
            PADDLE_HIT_SOUND.play()
        else:
            # Reset collision flag if not touching any paddle
            self.last_collision = None

    def reset(self):
        self.x = self.original_x
        self.y = self.original_y
        self.velocity_x *= -1
        self.velocity_y = random.choice([-3, 3])
        self.last_collision = None
        SCORE_SOUND.play()

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)
