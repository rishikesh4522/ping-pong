import pygame
from .paddle import Paddle
from .ball import Ball

WHITE = (255, 255, 255)

class GameEngine:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.paddle_width = 10
        self.paddle_height = 100
        self.winning_score = 5  # default winning score

        # Game objects
        self.player = Paddle(10, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ai = Paddle(width - 20, height // 2 - 50, self.paddle_width, self.paddle_height)
        self.ball = Ball(width // 2, height // 2, 7, 7, width, height)

        # Scores
        self.player_score = 0
        self.ai_score = 0
        self.font = pygame.font.SysFont("Arial", 30)

    def handle_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            self.player.move(-10, self.height)
        if keys[pygame.K_s]:
            self.player.move(10, self.height)

    def update(self, screen):
        # Move ball and check collision
        self.ball.move()
        self.ball.check_collision(self.player, self.ai)

        # Score update
        if self.ball.x <= 0:
            self.ai_score += 1
            self.ball.reset()
        elif self.ball.x >= self.width:
            self.player_score += 1
            self.ball.reset()

        # AI movement
        self.ai.auto_track(self.ball, self.height)

        # Check for game over
        if self.player_score >= self.winning_score or self.ai_score >= self.winning_score:
            self.game_over_screen(screen)

    def render(self, screen):
        # Draw paddles and ball
        pygame.draw.rect(screen, WHITE, self.player.rect())
        pygame.draw.rect(screen, WHITE, self.ai.rect())
        pygame.draw.ellipse(screen, WHITE, self.ball.rect())
        pygame.draw.aaline(screen, WHITE, (self.width // 2, 0), (self.width // 2, self.height))

        # Draw score
        player_text = self.font.render(str(self.player_score), True, WHITE)
        ai_text = self.font.render(str(self.ai_score), True, WHITE)
        screen.blit(player_text, (self.width // 4, 20))
        screen.blit(ai_text, (self.width * 3 // 4, 20))

    def game_over_screen(self, screen):
        running = True
        screen.fill((0, 0, 0))

        # Determine winner and text color
        if self.player_score > self.ai_score:
            winner_text = "Player Wins!"
            winner_color = (0, 255, 0)  # Green
        else:
            winner_text = "AI Wins!"
            winner_color = (255, 0, 0)  # Red

        # Render texts
        text = self.font.render(winner_text, True, winner_color)
        score_text = self.font.render(f"Player: {self.player_score}  AI: {self.ai_score}", True, (255, 255, 255))
        option_text = self.font.render("Press 3, 5, or 7 for Best-of rounds, or ESC to Exit", True, (255, 255, 255))

        # Blit texts on screen
        screen.blit(text, (self.width // 2 - text.get_width() // 2,
                        self.height // 2 - text.get_height() // 2 - 50))
        screen.blit(score_text, (self.width // 2 - score_text.get_width() // 2,
                                self.height // 2 - score_text.get_height() // 2))
        screen.blit(option_text, (self.width // 2 - option_text.get_width() // 2,
                                self.height // 2 - option_text.get_height() // 2 + 50))

        pygame.display.flip()

        # Wait for user input to replay or exit
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_3:
                        self.winning_score = 2
                        running = False
                    elif event.key == pygame.K_5:
                        self.winning_score = 3
                        running = False
                    elif event.key == pygame.K_7:
                        self.winning_score = 4
                        running = False
                    elif event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        exit()

        # Reset for replay
        self.player_score = 0
        self.ai_score = 0
        self.ball.reset()

