import pygame
from pygame import *

pygame.init()

clock = pygame.time.Clock()
fps = 24

screen_w = 640
screen_h = 480

screen = pygame.display.set_mode((screen_w, screen_h))
pygame.display.set_caption('AI Flappy Bird')

bg = pygame.image.load('img/bg.png')
ground = pygame.image.load('img/ground.png')

running = True

ground_scroll = 0
scroll_speed = 4

class Bird(pygame.sprite.Sprite):
	def __init__(self, x, y):
		pygame.sprite.Sprite.__init__(self)
		self.images = []
		self.index = 0
		self.counter = 0
		for num in range(1,4):
			img = pygame.image.load(f'img/bird{num}.png')
			self.images.append(img)
		self.image = self.images[self.index]
		self.rect = self.image.get_rect()
		self.rect.center = [x, y]
		self.vel = 0
	def update(self):
		self.vel += 0.5
		if self.vel > 8:
			self.vel = 8
			print(self.vel)
		if self.rect.bottom < 393:
			self.rect.y = int(self.vel)
		self.counter +=1
		cooldown = 5
		if self.counter > cooldown:
			self.counter = 0
			self.index += 1
			if self.index >= len(self.images):
				self.index = 0
		self.image = self.images[self.index]

bird_group = pygame.sprite.Group()

flappy = Bird(100,int(screen_h / 2))

bird_group.add(flappy)

while running:
	clock.tick(fps)
	screen.blit(ground, (ground_scroll,393))
	screen.blit(bg, (0,-80))
	bird_group.draw(screen)
	bird_group.update()
	ground_scroll -= scroll_speed
	if abs(ground_scroll) > 35:
		ground_scroll = 0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False	
	pygame.display.update()
pygame.quit()
