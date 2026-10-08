import pygame
import random


class Shield:
    def __init__(self, width):
        self.x = random.randint(40, width - 40)
        self.y = -20
        self.radius = 10
        self.vx = random.uniform(-1.2, 1.2)
        self.vy = random.uniform(1.5, 3.0)
        self.color = (120, 230, 255)

    def update(self):
        self.x += self.vx
        self.y += self.vy

    def off_screen(self, height):
        return self.y > height + 30

    def collides(self, rect):
        cx, cy = rect.centerx, rect.centery
        dx = self.x - cx
        dy = self.y - cy
        return (dx ** 2 + dy ** 2) ** 0.5 < self.radius + 16

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)
        pygame.draw.circle(screen, (255, 255, 255), (int(self.x), int(self.y)), self.radius - 3, 2)
