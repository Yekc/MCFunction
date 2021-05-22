from mcfunction.decorators import tick, load
import mcfunction.commands as c
import mcfunction.project as p

tick = False
load = False

def testagain():
	c.say(function="test", text="more text")

testagain()

p.create(path="New World", namespace="myDatapack", description="my datapack", pack_format="6")