import pygame #the module that has all the game functionality that will be used 
import sys #to allow the game to quit properly

SCREENWIDTH = 576
SCREENHEIGHT = 1024
FRAMERATE = 150 #number of frames per second 
BIRDXPOS = 100
BIRDYPOS = 512
GRAVITY = 0.30
JUMPHEIGHT = 10



def draw_floor():
	screen.blit(ground,(groundx,850))
	screen.blit(ground2,(groundx+SCREENWIDTH,850))
	

#initiates pygame
pygame.init()

#creating a display surface 
screen = pygame.display.set_mode((SCREENWIDTH,SCREENHEIGHT))
clock = pygame.time.Clock()

cur_bg = pygame.transform.scale2x(pygame.image.load('assets/background-day.png').convert())

ground = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
ground2 = pygame.transform.scale2x(pygame.image.load('assets/base.png').convert())
groundx = 0

bird = pygame.transform.scale2x(pygame.image.load('assets/bluebird-midflap.png').convert())
birdRec = bird.get_rect(center = (BIRDXPOS,BIRDYPOS))
birdMovement = 0

while True: 
	
	#event loop - have to look for specific types of events 
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			pygame.quit()	#unitializing the game 
			sys.exit()
		if event.type == pygame.KEYDOWN:	#checks if any key has been pressed 
			if event.key == pygame.K_SPACE: 
				birdMovement=0
				birdMovement-= JUMPHEIGHT
		if event.type == pygame.MOUSEBUTTONDOWN: 
			birdMovement=0
			birdMovement-= JUMPHEIGHT 	

	screen.blit(cur_bg,(0,0))

	birdMovement += GRAVITY
	birdRec.centery += birdMovement 
	if(birdRec.centery > SCREENHEIGHT):
		birdRec.centery = SCREENHEIGHT
		print("here")
	screen.blit(bird,birdRec)	

	if(groundx == -SCREENWIDTH):
		groundx = 0
	draw_floor()
	groundx -= 3

	#takes anything drawn before, and updates the display with it
	pygame.display.update() 
	clock.tick(FRAMERATE) 
