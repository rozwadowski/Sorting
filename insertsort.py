from pygame import *
from random import *


N = 25
size = 20
maxv = 300
fps = 20

n = 0

init()
window = display.set_mode((N*size,maxv+30))
clock = time.Clock()
Font=font.SysFont("comicsansms",32)


def drawtab(tab):
	window.fill((0,0,0))
	for i in range(N):
		draw.rect(window,(255,tab[i]*255./maxv,0),Rect(i*size,maxv-tab[i],size-1,tab[i]))
	
	text = Font.render("Insert Sort, N = " + str(N),True,(255,255,255))
	window.blit(text,(20,maxv+3))	

	
	
# create random array
tab = []
for i in range(N):
	tab.append(randint(1,maxv))


# sort
for i in range(1,N):
	key = tab[i]
	j = i - 1
	while j>=0 and tab[j]>key:
		tab[j+1] = tab[j]
		j = j - 1
		drawtab(tab)
		clock.tick(fps)
		display.flip()
		image.save(window, str(n).rjust(5,'0')+".png")
		n = n + 1
	tab[j+1] = key
	
	
# loop
end = False
while not end:
	for z in event.get():
		if z.type == QUIT:
			end = True

	drawtab(tab)
	clock.tick(fps)
	display.flip()