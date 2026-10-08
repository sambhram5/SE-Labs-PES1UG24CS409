import pygame
import random
from game.ship import Ship
from game.meteor import Meteor
from game.laser import Laser
from game.shield import Shield

WIDTH,HEIGHT=700,520
FPS=60
BG=(8,5,20)

class GameEngine:
    def __init__(self):
        pygame.init()
        self.screen=pygame.display.set_mode((WIDTH,HEIGHT))
        pygame.display.set_caption("Meteor Dodge")
        self.clock=pygame.time.Clock()
        self.font=pygame.font.SysFont("monospace",26,bold=True)
        self.big_font=pygame.font.SysFont("monospace",46,bold=True)
        self.stars=[(random.randint(0,WIDTH),random.randint(0,HEIGHT),random.randint(1,3)) for _ in range(80)]
        self.reset()

    def reset(self):
        self.ship=Ship(WIDTH//2,HEIGHT-80)
        self.meteors=[]
        self.lasers=[]
        self.shields=[]
        self.shield_timer=0
        self.shield_spawn_timer=0
        self.timer=0
        self.spawn_interval=60
        self.score=0
        self.consecutive_survival=0
        self.multiplier=1
        self.game_over=False
        self.started=False

    def handle_events(self):
        for event in pygame.event.get():
            if event.type==pygame.QUIT: return False
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_SPACE:
                    if self.game_over: self.reset()
                    elif not self.started: self.started=True
                    else: self.lasers.append(Laser(self.ship.rect.centerx,self.ship.rect.top))
        return True

    def update(self):
        if self.game_over or not self.started: return
        keys=pygame.key.get_pressed()
        self.ship.move(keys,WIDTH,HEIGHT)
        self.timer+=1
        self.consecutive_survival+=1
        self.multiplier=1 + self.consecutive_survival//(10*FPS)
        self.score+=self.multiplier
        if self.shield_timer>0: self.shield_timer-=1
        if self.shield_spawn_timer>0: self.shield_spawn_timer-=1
        elif not self.shields:
            self.shields.append(Shield(WIDTH))
            self.shield_spawn_timer=random.randint(300,480)
        if self.timer>=self.spawn_interval:
            self.meteors.append(Meteor(WIDTH))
            self.timer=0
            self.spawn_interval=max(20,self.spawn_interval-0.3)
        for shield in self.shields[:]:
            shield.update()
            if shield.collides(self.ship.rect):
                self.shields.remove(shield)
                self.shield_timer=300
            elif shield.off_screen(HEIGHT):
                self.shields.remove(shield)
        for m in self.meteors[:]:
            m.update()
            if m.collides(self.ship.rect):
                if self.shield_timer>0:
                    self.shield_timer=0
                    self.meteors.remove(m)
                    continue
                self.consecutive_survival=0
                self.multiplier=1
                self.game_over=True
        for laser in self.lasers[:]:
            laser.update()
            if laser.off_screen():
                self.lasers.remove(laser)
                continue
            for meteor in self.meteors[:]:
                if meteor.collides_with_laser(laser.rect):
                    self.meteors.remove(meteor)
                    self.lasers.remove(laser)
                    if meteor.is_large:
                        self.meteors.extend(meteor.split())
                    break
        self.meteors=[m for m in self.meteors if not m.off_screen(HEIGHT)]

    def draw(self):
        self.screen.fill(BG)
        for sx,sy,sr in self.stars:
            pygame.draw.circle(self.screen,(200,200,220),(sx,sy),sr)
        for m in self.meteors: m.draw(self.screen)
        for shield in self.shields: shield.draw(self.screen)
        for laser in self.lasers: laser.draw(self.screen)
        if self.shield_timer>0:
            p=pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
            pygame.draw.circle(p,(120,230,255,80),(self.ship.rect.centerx,self.ship.rect.centery),28)
            self.screen.blit(p,(0,0))
        self.ship.draw(self.screen)
        sc=self.font.render(f"Time: {self.consecutive_survival//60}s",True,(200,200,240))
        self.screen.blit(sc,(10,10))
        mult=self.font.render(f"Multiplier: x{self.multiplier}",True,(255,200,90))
        self.screen.blit(mult,(10,40))
        if not self.started:
            msg=self.font.render("Press SPACE to launch",True,(180,180,240))
            self.screen.blit(msg,(WIDTH//2-msg.get_width()//2,HEIGHT//2))
        if self.game_over:
            ov=pygame.Surface((WIDTH,HEIGHT),pygame.SRCALPHA)
            ov.fill((0,0,0,150))
            self.screen.blit(ov,(0,0))
            m=self.big_font.render("DESTROYED!",True,(220,80,60))
            s=self.font.render(f"Survived {self.consecutive_survival//60}s | SPACE to Restart",True,(200,200,200))
            self.screen.blit(m,(WIDTH//2-m.get_width()//2,HEIGHT//2-40))
            self.screen.blit(s,(WIDTH//2-s.get_width()//2,HEIGHT//2+20))
        pygame.display.flip()

    def run(self):
        running=True
        while running:
            running=self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(FPS)
        pygame.quit()
