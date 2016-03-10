#-*- encoding: utf8 -*-

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
import re
import keywords as Keywords

def handle(result, fileString):
   for var in result:
      localVar = re.match(Keywords.LOCAL_VARIABLE, var)
      if localVar != None:
         replace = var.replace("l ", "local ").replace(">>", "=").replace(".", "")
      else:
         replace = var.replace(">>", "=").replace(".", "")
      
      fileString = fileString.replace(var, replace)
      
   return fileString