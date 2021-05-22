tick = False
load = False

def tick(x):
	global tick
	tick = True
	x()

def load(x):
	global load
	load = True
	x()