import pygame

SPEED = 9
COLOR = (80, 240, 255)


class Laser:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x - 2, y - 14, 4, 14)

    def update(self):
        self.rect.y -= SPEED

    def off_screen(self):
        return self.rect.bottom < 0

    def draw(self, screen):
        pygame.draw.rect(screen, COLOR, self.rect)
