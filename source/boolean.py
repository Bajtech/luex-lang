def handle(result, filestring):
	for var in result:
		if var == "no" or var == "off" or var == "ki" or var == "nem":
			filestring = filestring.replace(var, var.replace(var, "false"))
		elif var == "yes" or var == "on" or var == "be" or var == "igen":
			filestring = filestring.replace(var, var.replace(var, "true"))
		elif var == "empty":
			filestring = filestring.replace(var, var.replace(var, "nil"))

	
	return filestring