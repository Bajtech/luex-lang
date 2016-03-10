def handle(result, filestring):
	for var in result:
		filestring = filestring.replace(var, var.replace("#{", "\"..tostring(").replace("}", ")..\""))

	return filestring