import pygame

class Paddle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.speed = 7

    def move(self, dy, screen_height):
        self.y += dy
        self.y = max(0, min(self.y, screen_height - self.height))

    def rect(self):
        return pygame.Rect(self.x, self.y, self.width, self.height)

    def auto_track(self, ball, screen_height):
        # Center positions
        paddle_center = self.y + self.height / 2
        ball_center = ball.y + ball.height / 2

        # Smooth movement: move a fraction of the distance each frame
        speed_factor = 0.15  # smaller = slower and smoother
        dy = (ball_center - paddle_center) * speed_factor

        # Apply movement, but clamp speed so it’s not too fast
        dy = max(-10, min(10, dy))  # max vertical step per frame
        self.move(dy, screen_height)
