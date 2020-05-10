import pygame as p
from random import randint, choice
from time import time

# Start ------------------------------

p.init()
p.display.set_caption('Blocks')
disp = p.display.set_mode((610, 595))

# Class ------------------------------

class block():
	def __init__(self, kind):
		self.kind = kind - 1
		self.m = [randint(0, 10 - blocks_ge[kind - 1][0]), 1 - blocks_ge[kind - 1][1]]
		self.angel = 0
		self.ge = []
		for i in blocks_ge[kind - 1]:
			self.ge += [i]
		self.sco = blocks_score[kind - 1]

	def rr(self):
		if 13 - self.m[1] > self.ge[0] and 13 - self.m[1] > self.ge[1] and tuch(self, 3) == 0:
			self.ge.reverse()
			self.angel += 1
			self.angel %= 4
			while self.m[0] + self.ge[0] > 10:
				self.m[0] -= 1
	def mtl(self):
		self.m[0] -= 1
	def mtr(self):
		self.m[0] += 1
	def mtd(self):
		self.m[1] += 1

# Functions ------------------------------

def tuch(nb, mod = 0):
	a = 0
	if mod == 0:
		if nb.m[1] + nb.ge[1] < 13:
			for i in range(nb.ge[0]):
				n = len(list_shap_blocks[nb.kind][nb.angel]) - nb.ge[0]
				n = list_shap_blocks[nb.kind][nb.angel][n + i]
				if n == 1:
					if display[nb.m[1] + nb.ge[1]][nb.m[0] + i] != -1:
						a = 1
				elif n == 0 and len(list_shap_blocks[nb.kind][nb.angel]) / nb.ge[0] >= 2:
					n1 = len(list_shap_blocks[nb.kind][nb.angel]) - nb.ge[0] * 2
					n1 = list_shap_blocks[nb.kind][nb.angel][n1 + i]
					if n1 == 1:
						if display[nb.m[1] + nb.ge[1] - 1][nb.m[0] + i] != -1:
							a = 1
					elif n1 == 0 and len(list_shap_blocks[nb.kind][nb.angel]) / nb.ge[0] >= 3:
						n2 = len(list_shap_blocks[nb.kind][nb.angel]) - nb.ge[0] * 3
						n2 = list_shap_blocks[nb.kind][nb.angel][n2 + i]
						if display[nb.m[1] + nb.ge[1] - 2][nb.m[0] + i] != -1:
							a = 1
		else:
			a = 1
	elif mod == 1:
		if nb.m[0] + nb.ge[0] < 10:
			for i in range(nb.ge[1]):
				n = len(list_shap_blocks[nb.kind][nb.angel]) / nb.ge[1] * (i + 1)
				n = list_shap_blocks[nb.kind][nb.angel][int(n - 1)]
				if display[nb.m[1] + i][nb.m[0] + nb.ge[0]] != -1 and n == 1 and nb.m[1] + i > -1:
					a = 1
		else:
			a = 1
	elif mod == 2:
		if nb.m[0] > 0:
			for i in range(nb.ge[1]):
				n = len(list_shap_blocks[nb.kind][nb.angel]) / nb.ge[1] * i
				n = list_shap_blocks[nb.kind][nb.angel][int(n)]
				if display[nb.m[1] + i][nb.m[0] - 1] != -1 and n == 1 and nb.m[1] + i > -1:
					a = 1
		else:
			a = 1
	elif mod == 3:
		x = nb.ge[0]
		y = nb.ge[1]
		for i in range(y):
			for k in range(x):
				try:
					n = list_shap_blocks[nb.kind][nb.angel][y * k + i]
					if display[nb.m[1] + i][nb.m[0] + k] != -1 and n == 1:
						a = 1
				except:
					pass
				try:
					n = list_shap_blocks[nb.kind][nb.angel][x * i + k]
					if display[nb.m[1] + k][nb.m[0] + i] != -1 and n == 1:
						a = 1
				except:
					pass
	return a

def show(display):
	for i in range(13):
		for k in range(10):
			if display[i][k] > -1:
				x = 5 + k * 45
				y = 5 + i * 45
				disp.blit(list_s_blocks[display[i][k]], (x, y))

def show_freez(t):
	t *= 2
	cont = 0
	rcont = 20
	while cont <= t:
		p.draw.line(disp, (0, 127, 255), (cont + 476, 222), (cont + 476, 269), 1)
		cont += 1
		if cont == rcont:
			rcont += 22
			cont += 2
			t += 2

def show_score(score):
	text = cour.render(str(score), True, (0, 255, 0))
	rect = text.get_rect()
	rect.center = (530, 120)
	disp.blit(text, rect)

def show_first_block(nb):
	image = list_blocks[nb.kind]
	im = p.transform.rotate(image, nb.angel * 90)
	x = 5 + nb.m[0] * 45
	y = 5 + nb.m[1] * 45
	disp.blit(im, (x, y))

def show_second_block(kind):
	image = list_blocks[kind-1]
	t, a = image.get_size()
	y = a / t * 135
	image = p.transform.scale(image, (135, int(y)))
	disp.blit(image, (465, 435))

def remove_blocks(l, y):
	global bes
	cy = y
	y = 5 + y * 45
	bes.play()
	for i in range(10):
		x = 5 + i * 45
		disp.blit(list_s_blocks[6], (x, y))
		p.display.update()
		p.time.Clock().tick(10)
	l.pop(cy)
	l = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]] + l
	return l

# Variables ------------------------------

blocks_ge = [[2, 2], [3, 2], [3, 1], [3, 2], [3, 2], [5, 1]]
blocks_score = [4, 4, 3, 4, 4, 5]
list_shap_blocks = [
    [[1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]],
    [[0, 1, 0, 1, 1, 1], [0, 1, 1, 1, 0, 1], [1, 1, 1, 0, 1, 0], [1, 0, 1, 1, 1, 0]],
    [[1, 1, 1], [1, 1, 1], [1, 1, 1], [1, 1, 1]],
    [[0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 0, 1], [0, 1, 1, 1, 1, 0], [1, 0, 1, 1, 0, 1]],
    [[0, 0, 1, 1, 1, 1], [1, 1, 0, 1, 0, 1], [1, 1, 1, 1, 0, 0], [1, 0, 1, 0, 1, 1]],
    [[1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]]]
list_available_blocks = [1, 2, 3, 4, 5, 6]
list_blocks = []
for i in range(1, 7):
	list_blocks += [p.image.load("data/%i.png" % (i))]
list_s_blocks = []
for i in range(1, 8):
	list_s_blocks += [p.image.load("data/Block_%i.png" % (i))]
freez_image = p.image.load('data/Freez.png')
borders = p.image.load('data/Borders.png')
backgrand = p.image.load('data/BG.png')
cour = p.font.Font('data/cour.ttf', 45)
nfs = p.mixer.Sound('data/NFS.wav')
dfs = p.mixer.Sound('data/DFS.wav')
tbs = p.mixer.Sound('data/TBS.wav')
bes = p.mixer.Sound('data/BES.wav')
done = 0
score = 0
freez = 0
freez_time = 0
freezed = 0
move_time = 1
fast_move = 0
fast_move_time = 1
list_rand_blocks = [choice(list_available_blocks), choice(list_available_blocks)]
nb = block(list_rand_blocks[0])
display = [
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
    [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]
p.display.set_icon(list_s_blocks[3])
start = time()

# Main_Loop ------------------------------

while not done:
	disp.blit(backgrand, (0, 0))
	now = time()
	if len(set(display[0]) & {1, 2, 3, 4, 5, 6}) > 0:
		done = 1
	if round(now - start) >= freez_time and freezed == 0 and freez < 50:
		freez += 1
		freez_time = round(now - start) + 1
	if freez % 10 == 0 and freez < 50:
		nfs.play()
	if freezed > 0:
		if round(now - stop_freez_time) >= freezed:
			freezed = 0
	if tuch(nb) and freezed == 0:
		tbs.play()
		for i in range(nb.ge[1]):
			for k in range(nb.ge[0]):
				n = i * nb.ge[0] + k
				if list_shap_blocks[nb.kind][nb.angel][n] == 1:
					display[i + nb.m[1]][k + nb.m[0]] = nb.kind
		score += nb.sco
		list_rand_blocks[0] = list_rand_blocks[1]
		list_rand_blocks[1] = choice(list_available_blocks)
		nb = block(list_rand_blocks[0])
	if freezed == 0 and round(now - start) >= move_time and fast_move == 0:
		nb.mtd()
		move_time = round(now - start) + 1
	for event in p.event.get():
		if event.type == p.QUIT:
			done = 1
		if event.type == p.KEYDOWN:
			if event.key == p.K_SPACE and freez >= 10:
				dfs.play()
				freez -= 10
				freezed += 3
				stop_freez_time = time()
			if event.key == p.K_RIGHT and tuch(nb, 1) == 0:
				nb.mtr()
			if event.key == p.K_LEFT and tuch(nb, 2) == 0:
				nb.mtl()
			if event.key == p.K_UP:
				nb.rr()
			if event.key == p.K_DOWN:
				fast_move = 1
		if event.type == p.KEYUP:
			if event.key == p.K_DOWN:
				fast_move = 0
	if round((now - start) * 3) >= fast_move_time and fast_move == 1:
		nb.mtd()
		fast_move_time = round((now - start) * 3) + 1
	show_score(score)
	show_freez(freez)
	show_first_block(nb)
	show_second_block(list_rand_blocks[1])
	show(display)
	for i in range(13):
		if not(-1 in display[i]):
			score += 15
			display = remove_blocks(display, i)
	if len(set(display[0])) > 1:
		done = 1
		break
	if freezed > 0:
		disp.blit(freez_image, (5, 5))
	disp.blit(borders, (0, 0))
	p.time.Clock().tick(30)
	p.display.update()
p.time.Clock().tick(4)
disp.fill((0, 0, 0))
text = cour.render('Score: ' + str(score), True, (0, 255, 0))
rect = text.get_rect()
rect.center = (int(610 / 2), int(595 / 2))
disp.blit(text, rect)
p.display.update()
p.time.Clock().tick(1)
p.quit()
