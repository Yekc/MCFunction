import os

def create(path="", namespace="datapack", description="Datapack", pack_format="6"):
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
	

	#--------------------------------------------------------------------------------------------------------------------------

