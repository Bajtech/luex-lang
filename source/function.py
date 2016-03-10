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

def handle(result, filestring):
   for var in result:
      funcTop = re.match(Keywords.FUNCTION_TOP, var).group(1)

      if "when" in funcTop:
         when = re.match(Keywords.WHEN, funcTop).group(1).strip("(").strip("):")

         if not "==" in when:
            newTop = funcTop.replace("fn ", "function ").replace("):", ")").replace(" when(" + when + ")", "\nif not " + when + " then return end")
         else:
           newTop = funcTop.replace("fn ", "function ").replace("):", ")").replace(" when(" + when + ")", "\nif " + when.replace("==", "~=") + " then return end")

      else:
         newTop = funcTop.replace("fn ", "function ").replace("):", ")")

      replacement = var.replace(funcTop, newTop).replace(":fn", "end")
      filestring = filestring.replace(var, replacement)

   return filestring



