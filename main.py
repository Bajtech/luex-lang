#-*- coding: utf8 -*-

VERSION = "v0.4"

"""
   Luex Source to Source Compiler
   Copyright (C) 2016  Molnár Márk

   This program is free software: you can redistribute it and/or modify
   it under the terms of the GNU General Public License as published by
   the Free Software Foundation, either version 3 of the License, or
   (at your option) any later version.

   This program is distributed in the hope that it will be useful,
   but WITHOUT ANY WARRANTY; without even the implied warranty of
   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
   GNU General Public License for more details.

   You should have received a copy of the GNU General Public License
   along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import sys

sys.path.append("src")

import re
import os
import glob
import keywords 	as Keywords
import tokens 		as Tokens
import function 	as Function
import aliases 		as Aliases
import error
import threading
import time

# Configuration 
config = {}
config["crtResource"] = "something"
# Files being watched
watchingFiles = {}
# Output file
outFile = None
# options
options = None
# global message to show each time get_input is called
globalMessage = None
# thread for file watching
fileWatchThread = None

title = "Luex - Egy Lua Source to Source Transpiler\n"
lhelp = """
Mi az a Luex?

A Luex egy source to source transpiler, ami mas nyelvekbol ismert elemeket visz at a luaba.
Celja hogy megkonnyitse a luaval valo fejlesztest.

Hasznalata:

Inditsuk el a compiler.exe fajlt. majd a compile <luexfajl> paranccsal forditsunk at egy luex fajlt luaba.

Parancsok:

	compile <luex>
	getconfig <confignev>
	setresource <resourcenev>
	new <resourcenev>
	watchfiles
	exit
	help

[Nyomj entert a visszalepeshez]"""

"""
Main Entry
"""

def main():
	load_config()
	get_input()

"""
Function for loading the configuration file (config.luexcfg)
"""

def load_config():
	configContents = open("config.luexcfg", "r").read()
	configNames = re.findall("^:(\w+) ->", configContents)
	configValues = re.findall("^:\w+ -> \"(.*?)\".", configContents)

	for c in configNames:
		if c == None:
			sys.exit()

		config[c] = configValues[configNames.index(c)]

"""
Function for setting config nodes inside the configuration folder
"""

def set_config(confNode, confValue):
	try:
		configFile = open("config.luexcfg", "r")	
		configContents = configFile.read()
		configFile.close()
		find = re.match("^:"+ confNode +" -> \"(.*?)\".", configContents).group(1)
		configContents = configContents.replace(find, confValue)
		configFile = open("config.luexcfg", "w")
		configFile.write(configContents)
		configFile.close()
	except:
		print("Nincs config.luexcfg fajl!")

"""
Function for handling commands
"""

def get_input():
	global outFile, options, globalMessage
	try:
		os.system("title Luex " + VERSION)
		os.system("cls")
		print(title)

		if globalMessage != None:
			print(globalMessage)
			globalMessage = None

		option = raw_input("[Luex]> ")
		options = option.split(" ")

		if options[0] == "compile":
			parse(options[1], options[1] + ".lua")
		
		elif options[0] == "help":
			os.system("cls")
			print(title)	
			print(lhelp)
			raw_input()	
			get_input()

		elif options[0] == "exit":
			fileWatchThread.join()
			sys.exit()

		elif options[0] == "getconfig":
			print(config[options[1]])
			raw_input()
			get_input()

		elif options[0] == "setresource":
			config["crtResource"] =	options[1] + "/"
			globalMessage = "Resource atallitva. Jelenlegi resource: " + options[1]
			get_input()	

		elif options[0] == "watchfiles":
			fileWatchThread = threading.Thread(target=watch)
			fileWatchThread.start()
			globalMessage = "Mostantol a forditas automatikus."

		elif options[0] == "new":
			new = config["mtafolder"] + options[1]
			
			if not os.path.exists(new):
				os.makedirs(new + "/files")
				open(new + "/main.luex", "a").close()
				open(new + "/main.luex.lua", "a").close()
				config["crtResource"] = options[1]
				mainFileType = options[2]
				generate_meta(mainFileType)
	    	else:
	    		print("resource mar letezik.")

	    	get_input()
	except:
		sys.exc_clear()

"""
Function for generating meta files
"""

def generate_meta(typ):
	try:
		meta = "<meta>\n<!-- Generated by Luex -->\n"
		
		os.chdir(config["mtafolder"] + config["crtResource"])
		for file in glob.glob("*.luex.lua"):
			meta += "<script src=\"" + file + "\" type=\"" + typ + "\"/>\n"

		meta += "</meta>"
		metaFile = open("meta.xml", "w+")
		metaFile.write(meta)
	except:
		sys.exc_clear()

"""
Function for file watching
"""

def watch():
	while True:
		os.chdir(config["mtafolder"] + config["crtResource"])
		for file in glob.glob("*.luex"):
			try:
				if watchingFiles[file] != time.ctime(os.path.getmtime(file)):
					watchingFiles[file] = time.ctime(os.path.getmtime(file))
					parse(file, file + ".lua")
			except:
				watchingFiles[file] = time.ctime(os.path.getmtime(file))
  				sys.exc_clear()

"""
Function for code parsing and assemblying
"""

def parse(inFile, outFileName):
	try:
		inFile = open(inFile, "r")
		fileString = inFile.read()
		inFile.close()
		fileString = str(fileString)

		for v in Tokens.tokens:
			pattern = re.compile(v[0], re.S)
			result = re.findall(pattern, fileString)
			fileString = v[1](result, fileString)

		print("\n[Luex Compiler] Sikeres forditas.")
		outFile = open(outFileName, "w+")
		outFile.write("-- Generated by Luex "+ VERSION +"\n\n")

		for v in Aliases.aliases:
			fileString = fileString.replace(v[0], v[1])

		outFile.write(fileString)
		outFile.close()
	except:
		print("Hibas kod.")
    	sys.exc_clear()

main()