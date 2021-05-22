import os
import shutil

#add new lists to class:
#setattr(commands, name, value)
class commands:
	def add(self, attr, val):
		setattr(self, attr, val)

	tick = []
	load = []

functions = [attr for attr in vars(commands) if not attr.startswith("__") and not attr.startswith("add")]


def create(path="", namespace="datapack", description="Datapack", pack_format="6"):
	if os.path.isdir(path + "/" + namespace):
		shutil.rmtree(path + "/" + namespace)

	os.mkdir(path + "/" + namespace)
	os.mkdir(path + "/" + namespace + "/data")

	mcmeta = open(path + "/" + namespace + "/pack.mcmeta", "w")
	mcmeta.write("""{
"pack": {
    "pack_format": """ + pack_format + """,
    "description": \"""" + description + """\"
  }
}""")
	mcmeta.close()

	os.mkdir(path + "/" + namespace + "/data/minecraft")
	os.mkdir(path + "/" + namespace + "/data/" + namespace)

	os.mkdir(path + "/" + namespace + "/data/minecraft/tags")
	os.mkdir(path + "/" + namespace + "/data/minecraft/tags/functions")

	tick = open(path + "/" + namespace + "/data/minecraft/tags/functions/tick.json", "w")
	tick.write("""{
 "values": [
 \"""" + namespace + """:tick\"
 ]
}""")
	tick.close()

	load = open(path + "/" + namespace + "/data/minecraft/tags/functions/load.json", "w")
	load.write("""{
 "values": [
 \"""" + namespace + """:load\"
 ]
}""")
	load.close()

	os.mkdir(path + "/" + namespace + "/data/" + namespace + "/functions")
	
	for i in functions:
		f = open(path + "/" + namespace + "/data/" + namespace + "/functions/" + i + ".mcfunction", "w")
		f.write("")
		f.close()
		f = open(path + "/" + namespace + "/data/" + namespace + "/functions/" + i + ".mcfunction", "a+")
		#print(i)
		exec("for j in commands." + i + ":\n\tf.write(j + \"\\n\")")


#---------------------------------------------------------------------------------------------------------------------------