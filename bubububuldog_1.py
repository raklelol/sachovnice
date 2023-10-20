
import pygame
pygame.init()
pygame.display.set_caption('Šachy')
sachovnice = [[1,0,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1],
			  [0,0,0,0,0,0,0,0],
			  [0,0,0,0,1,0,0,0],
			  [0,0,0,0,0,0,0,0],
			  [0,0,0,0,0,0,0,0],
			  [1,1,1,1,1,1,1,1],
			  [1,1,1,1,1,1,1,1]]

white = (255, 255, 255)
blue = (1, 25, 54)
black = (0, 0, 0)
brown = (179, 127, 79)
green = (173, 234, 153)

#generace hrací plochy
def plocha():
	#pozadí
	display_surface.fill(green)
	#generace políček
	for x in range(velikost):
		for y in range(velikost):
			if(x%2==y%2): 
				color = brown
			else:
				color = white
			pygame.draw.rect(display_surface, color, pygame.Rect(rozdeleni*x+okraje, rozdeleni*y+okraje, rozdeleni, rozdeleni))
	#ohraničení šachovnice
	pygame.draw.rect(display_surface, black, pygame.Rect(okraje-hrana, okraje-hrana, rozdeleni*velikost+hrana*2, rozdeleni*velikost+hrana*2),  hrana)

#generace figurek
def figurky():
	for x in range(velikost):
		for y in range(velikost):
			if(sachovnice[y][x]==1):
				display_surface.blit(img, (rozdeleni*x+okraje+rozdeleni*1/8, rozdeleni*y+okraje+rozdeleni*0.5/8))
	
#tloušťka ohraničení šachovnice
#rozlišení výšky monitoru, získané z pygame [0]>monitor [1]>pořadí z listu(v našem případě souřadnice y)
#vzdálenost hrací plochy od lévého a horního okraje obrazovky
#rozdělení obrazovky na 9 stejných částí
#velikost sachovnice v počtu políček

velikost = 2
hrana = 10
rozliseni = pygame.display.get_desktop_sizes()[0][1]
rozliseni2 = pygame.display.get_desktop_sizes()[0][0]
okraje = rozliseni/(velikost+1)/2
rozdeleni = rozliseni/(velikost+1)

#rozliseni aplikace
#načtení obrázku
#změna rozlišení obrázku
display_surface = pygame.display.set_mode((pygame.display.get_desktop_sizes()[0]))
img = pygame.image.load("stickman.png")
img = pygame.transform.scale(img, (rozdeleni*3/4, rozdeleni*3.5/4))

while True:
	
	plocha()
	figurky()

	#pokud vypnete program tak se vypne 
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			quit()
		#aktualizace displeje
		pygame.display.update()

