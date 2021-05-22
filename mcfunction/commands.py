import mcfunction.decorators as d

commandstick = []
commandsload = []
commandssay = []
commandsnewscore = []
commandsremovescore = []
commandssetscore = []
commandssetdisplayscore = []
commandsaddscore = []
commandssubscore = []
commandstriggerenable = []
commandsgive = []
commandsclear = []
commandstp = []
commandsgamemode = []
commandsnewteam = []
commandsjointeam = []
commandsmodifyteam = []
commandsremoveteam = []

#/say
def say(text=""):
	global commands
	if d.tick == True:
		print("tick") 

		commandstick.append("say " + text)

		d.tick = False

	elif d.load == True:
		print("load") 

		commandsload.append("say " + text)

		d.load = False

	elif d.function == True:
		print("function") 

		commandssay.append("say " + text)

		d.function = False

	else:
		print("neither")

		commands.append("say " + text)

		d.tick = False
		d.load = False
		d.function = False

#/scoreboard objectives add
def new_score(name="", type="dummy", displayname=""):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("scoreboard objectives add " + name + " " + type + " " + displayname)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("scoreboard objectives add " + name + " " + type + " " + displayname)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("scoreboard objectives add " + name + " " + type + " " + displayname)

		d.function = False

	else:
		print("neither")

		commands.append("scoreboard objectives add " + name + " " + type + " " + displayname)

		d.tick = False
		d.load = False
		d.function = False

#/scoreboard objectives remove
def remove_score(score_name=""):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("scoreboard objectives remove " + score_name)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("scoreboard objectives remove " + score_name)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("scoreboard objectives remove " + score_name)
		
		d.function = False

	else:
		print("neither")

		commands.append("scoreboard objectives remove " + score_name)
		
		d.tick = False
		d.load = False
		d.function = False

#/scoreboard players set
def set_score(target="", score_name="", value=""):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("scoreboard players set " + target + " " + score_name + " " + value)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("scoreboard players set " + target + " " + score_name + " " + value)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("scoreboard players set " + target + " " + score_name + " " + value)

		d.function = False

	else:
		print("neither")

		commands.append("scoreboard players set " + target + " " + score_name + " " + value)

		d.tick = False
		d.load = False
		d.function = False

#/scoreboard objectives setdisplay
def setdisplay_score(display="", score_name=""):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("scoreboard objectives setdisplay " + display + " " + score_name)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("scoreboard objectives setdisplay " + display + " " + score_name)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("scoreboard objectives setdisplay " + display + " " + score_name)

		d.function = False

	else:
		print("neither")

		commands.append("scoreboard objectives setdisplay " + display + " " + score_name)

		d.tick = False
		d.load = False
		d.function = False

#/scoreboard players add
def add_score(target="", score_name="", amount="1"):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("scoreboard players add " + target + " " + score_name + " " + amount)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("scoreboard players add " + target + " " + score_name + " " + amount)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("scoreboard players add " + target + " " + score_name + " " + amount)

		d.function = False

	else:
		print("neither")

		commands.append("scoreboard players add " + target + " " + score_name + " " + amount)

		d.tick = False
		d.load = False
		d.function = False

#/scoreboard players remove
def sub_score(target="", score_name="", amount="1"):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("scoreboard players remove " + target + " " + score_name + " " + amount)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("scoreboard players remove " + target + " " + score_name + " " + amount)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("scoreboard players remove " + target + " " + score_name + " " + amount)

		d.function = False

	else:
		print("neither")

		commands.append("scoreboard players remove " + target + " " + score_name + " " + amount)

		d.tick = False
		d.load = False
		d.function = False

#/scoreboard players enable 
def trigger_enable(target="", score_name=""):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("scoreboard players enable " + target + " " + score_name)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("scoreboard players enable " + target + " " + score_name)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("scoreboard players enable " + target + " " + score_name)

		d.function = False

	else:
		print("neither")

		commands.append("scoreboard players enable " + target + " " + score_name)

		d.tick = False
		d.load = False
		d.function = False

#/give
def give(target="", item="", nbt="", amount="1"):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("give " + target + " " + item + "{" + nbt + "}" + " " + amount)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("give " + target + " " + item + "{" + nbt + "}" + " " + amount)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("give " + target + " " + item + "{" + nbt + "}" + " " + amount)

		d.function = False

	else:
		print("neither")

		commands.append("give " + target + " " + item + "{" + nbt + "}" + " " + amount)

		d.tick = False
		d.load = False
		d.function = False

#/clear
def clear(target="", item="", nbt="", maxcount=""):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("clear " + target + " " + item + "{" + nbt + "} " + maxcount)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("clear " + target + " " + item + "{" + nbt + "} " + maxcount)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("clear " + target + " " + item + "{" + nbt + "} " + maxcount)

		d.function = False

	else:
		print("neither")

		commands.append("clear " + target + " " + item + "{" + nbt + "} " + maxcount)

		d.tick = False
		d.load = False
		d.function = False

#/tp
def tp(target="", location=""):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("tp " + target + " " + location)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("tp " + target + " " + location)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("tp " + target + " " + location)

		d.function = False

	else:
		print("neither")

		commands.append("tp " + target + " " + location)

		d.tick = False
		d.load = False
		d.function = False

#/gamemode
def gamemode(target="", gamemode=""):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("gamemode " + gamemode + " " + target)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("gamemode " + gamemode + " " + target)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("gamemode " + gamemode + " " + target)

		d.function = False

	else:
		print("neither")

		commands.append("gamemode " + gamemode + " " + target)

		d.tick = False
		d.load = False
		d.function = False

#/team add
def new_team(name="", displayname=""):
	global commands
	if d.tick == True:
		print("tick") 

		commands.append("team add " + name + " " + displayname)

		d.tick = False

	elif d.load == True:
		print("load") 

		commands.append("team add " + name + " " + displayname)

		d.load = False

	elif d.function == True:
		print("function") 

		commands.append("team add " + name + " " + displayname)

		d.function = False

	else:
		print("neither")

		commands.append("team add " + name + " " + displayname)

		d.tick = False
		d.load = False
		d.function = False

#/team join
def join_team(target="", team_name=""):
	global commands
	if d.tick == True:
		print("tick") 
		d.tick = False

	elif d.load == True:
		print("load") 
		d.load = False

	elif d.function == True:
		print("function") 
		d.function = False

	else:
		print("neither")
		d.tick = False
		d.load = False
		d.function = False

#/team modify
def modify_team(team_name="", option="", option_value=""):
	global commands
	if d.tick == True:
		print("tick") 
		d.tick = False

	elif d.load == True:
		print("load") 
		d.load = False

	elif d.function == True:
		print("function") 
		d.function = False

	else:
		print("neither")
		d.tick = False
		d.load = False
		d.function = False

#/team remove
def remove_team(team_name=""):
	global commands
	if d.tick == True:
		print("tick") 
		d.tick = False

	elif d.load == True:
		print("load") 
		d.load = False

	elif d.function == True:
		print("function") 
		d.function = False

	else:
		print("neither")
		d.tick = False
		d.load = False
		d.function = False
