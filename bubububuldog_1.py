
import pygame
pygame.init()
pygame.display.set_caption('Šachy')
sachovnice = [[1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1],
			  [0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0],
			  [1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1]]

white = (255, 255, 255)
blue = (1, 25, 54)
black = (0, 0, 0)
brown = (179, 127, 79)
green = (173, 234, 153)

#tloušťka ohraničení šachovnice
#rozlišení výšky monitoru, získané z pygame [0]>monitor [1]>souřadnice z listu(v našem případě y)
#vzdálenost hrací plochy od lévého a horního okraje obrazovky

hrana = 10
rozliseni = pygame.display.get_desktop_sizes()[0][1]
okraje = rozliseni/9/2
#velikost_figurek = 

#print(pygame.display.get_desktop_sizes())
display_surface = pygame.display.set_mode((pygame.display.get_desktop_sizes()[0]))
img = pygame.image.load("C:\\tesar\\projekt\\stickman.png")
img = pygame.transform.scale(img, (rozliseni/9, rozliseni/9))

while True:

	#pozadí
	display_surface.fill(green)
	#generace políček
	for x in range(8):
		for y in range(8):
			if(x%2==y%2): 
				color = brown
			else:
				color = white
			pygame.draw.rect(display_surface, color, pygame.Rect(rozliseni/9*x+okraje, rozliseni/9*y+okraje, rozliseni/9, rozliseni/9))
			
			
	#ohraničení šachovnice
	pygame.draw.rect(display_surface, black, pygame.Rect(okraje-hrana, okraje-hrana, rozliseni/9*8+hrana*2, rozliseni/9*8+hrana*2),  hrana)
	for x in range(8):
		for y in range(8):
			if(sachovnice[y][x]==1):
				display_surface.blit(img, (rozliseni/9*x+okraje, rozliseni/9*y+okraje))

	#pokud kliknete na křížek pro vypnutí programu tak se vypne 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		#aktualizace displeje
		pygame.display.update()
