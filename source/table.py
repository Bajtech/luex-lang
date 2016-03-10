def handle(result, filestring):
	for var in result:
		replace = var.replace("table", "{}")
		filestring = filestring.replace(var, replace)
	
	return filestring