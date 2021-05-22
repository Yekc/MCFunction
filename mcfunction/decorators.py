tick = False
load = False
function = False

def tick(x):
	global tick
	tick = True
	x()

def load(x):
	global load
	load = True
	x()

def function(x):
	global function
	function = True
	x()