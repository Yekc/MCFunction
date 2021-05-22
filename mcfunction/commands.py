import mcfunction.decorators as d
import mcfunction.project as p

#/say
def say(function="", text=""):

	if d.tick == True:
		p.commands.tick.append("say " + text) 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("say " + text)
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "say " + text + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/scoreboard objectives add
def new_score(function="", name="", type="dummy", displayname=""):
	
	if d.tick == True:
		p.commands.tick.append("")
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/scoreboard players set
def set_score(function="", target="", score_name="", value=""):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/scoreboard objectives setdisplay
def setdisplay_score(function="", display="", score_name=""):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/scoreboard players add
def add_score(function="", target="", score_name="", amount="1"):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/scoreboard players remove
def sub_score(function="", target="", score_name="", amount="1"):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/scoreboard players enable 
def trigger_enable(function="", target="", score_name=""):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/give
def give(function="", target="", item="", nbt="none"):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/clear
def clear(function="", target="", item="none", maxcount="none"):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/tp
def tp(function="", target="", location="none", toplayer="none"):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/gamemode
def gamemode(function="", target="", gamemode=""):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/team add
def new_team(function="", name="", displayname="none"):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/team join
def join_team(function="", target="", team_name=""):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/team modify
def modify_team(function="", team_name="", option="", option_value=""):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		

#/team remove
def remove_team(function="", team_name=""):
	
	if d.tick == True:
		p.commands.tick.append("") 
		d.tick = False

	elif d.load == True:
		p.commands.load.append("") 
		d.load = False

	else:
		exec("p.commands.add(p.commands, \"" + function + "\", \"[\\\"" + "PUT COMMAND HERE" + "\\\"]\")")
		d.tick = False
		d.load = False
		
