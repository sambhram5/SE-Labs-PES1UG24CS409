import pygame
import random
import math

class Meteor:
    def __init__(self, width, x=None, y=None, radius=None, vx=None, vy=None, color=None):
        self.x = random.randint(0, width) if x is None else x
        self.y = -30 if y is None else y
        self.radius = random.randint(12, 28) if radius is None else radius
        if vx is None or vy is None:
            angle = random.uniform(70,110)
            speed = random.uniform(2,5)
            self.vx = math.cos(math.radians(angle))*speed
            self.vy = math.sin(math.radians(angle))*speed
        else:
            self.vx = vx
            self.vy = vy
        if color is None:
            self.color = (
                random.randint(160,220),
                random.randint(80,120),
                random.randint(40,80)
            )
        else:
            self.color = color
        self.rot = random.uniform(0,360)
        self.rot_speed = random.uniform(-3,3)

    @property
    def is_large(self):
        return self.radius > 18

    def split(self):
        if not self.is_large: return []
        fragments=[]
        for i in range(3):
            angle = math.radians((360/3)*i + random.uniform(-20,20))
            speed = random.uniform(1.6,3.2)
            fragment_radius = max(8,self.radius*random.uniform(0.45,0.7))
            fragment_vx = self.vx + math.cos(angle)*speed
            fragment_vy = self.vy + math.sin(angle)*speed
            fragment_color = tuple(max(0,c-25) for c in self.color)
            fragments.append(Meteor(0,
                x=self.x,
                y=self.y,
                radius=fragment_radius,
                vx=fragment_vx,
                vy=fragment_vy,
                color=fragment_color))
        return fragments

    def update(self):
        self.x+=self.vx; self.y+=self.vy
        self.rot=(self.rot+self.rot_speed)%360

    def off_screen(self, height):
        return self.y > height + 60

    def collides(self, rect):
        cx,cy=rect.centerx,rect.centery
        dx,dy=self.x-cx,self.y-cy
        return (dx**2+dy**2)**0.5 < self.radius + 16

    def collides_with_laser(self, rect):
        closest_x=max(rect.left,min(self.x,rect.right))
        closest_y=max(rect.top,min(self.y,rect.bottom))
        dx=self.x-closest_x
        dy=self.y-closest_y
        return dx**2+dy**2 <= self.radius**2

    def draw(self, screen):
        import math
        pts=[]
        for i in range(7):
            angle=math.radians(self.rot+i*(360/7))
            r=self.radius*(0.8+0.2*(i%2))
            pts.append((int(self.x+r*math.cos(angle)),int(self.y+r*math.sin(angle))))
        pygame.draw.polygon(screen,self.color,pts)
        inner=[(int(self.x+(r*0.5)*math.cos(math.radians(self.rot+i*(360/7)))),
                int(self.y+(r*0.5)*math.sin(math.radians(self.rot+i*(360/7)))))
               for i,(cx,cy) in enumerate(pts)]
        pygame.draw.polygon(screen,tuple(max(0,c-40) for c in self.color),inner)
