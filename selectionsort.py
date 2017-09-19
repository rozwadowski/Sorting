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
Font=font.SysFont("arial",26)


def drawtab(tab):
	window.fill((0,0,0))
	for i in range(N):
		draw.rect(window,(0,tab[i]*255./maxv,255),Rect(i*size,maxv-tab[i],size-1,tab[i]))
	
	text = Font.render("Selection Sort, N = " + str(N),True,(255,255,255))
	window.blit(text,(20,maxv+3))	

	
	
# create random array
tab = []
for i in range(N):
	tab.append(randint(1,maxv))

def get_min_ind(from_i,tab):
	min_val = tab[from_i]
	index = from_i
	for i in range(from_i+1,len(tab)):
		if tab[i] < min_val:
			min_val = tab[i]
			index = i
	return index

# sort
for i in range(N):
	min_index = get_min_ind(i,tab)
	tmp = tab[min_index]
	tab[min_index] = tab[i]
	tab[i] = tmp
		
	drawtab(tab)
	clock.tick(fps)
	display.flip()
	#image.save(window, str(n).rjust(5,'0')+".png")
	n = n + 1

	
	
# loop
end = False
while not end:
	for z in event.get():
		if z.type == QUIT:
			end = True

	drawtab(tab)
	clock.tick(fps)
	display.flip()