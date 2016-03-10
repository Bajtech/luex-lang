def handle(result, filestring):
	for var in result:
		parts = var.split(">")
		filestring = filestring.replace(var, var.replace("call>" + parts[1], "exports[\"" + parts[1] + "\"]").replace(">" + parts[2], ":" + parts[2]))

	return filestring