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
		draw.rect(window,(tab[i]*255./maxv,255,0),Rect(i*size,maxv-tab[i],size-1,tab[i]))
	
	text = Font.render("Quicksort, N = " + str(N),True,(255,255,255))
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
def quicksort(tab, l=0, r=-1):
	if r == -1:
		r = len(tab) - 1
	i = l
	j = r
	s = tab[(l+r)/2]
	while i <= j:
		while tab[i] < s:
			i = i + 1
		while tab[j] > s:
			j = j -  1
		if i <= j:
			tab[i], tab[j] = tab[j], tab[i]
			drawtab(tab)
			global n
			n=n+1
			#image.save(window, str(n).rjust(5,'0')+".png")
			clock.tick(fps)
			display.flip()
			i = i + 1
			j = j - 1
	if l < j: 
		quicksort(tab, l, j) 
	if r > i:
		quicksort(tab, i, r)	

quicksort(tab)

# loop
end = False
while not end:
	for z in event.get():
		if z.type == QUIT:
			end = True

	drawtab(tab)
	clock.tick(fps)
	display.flip()