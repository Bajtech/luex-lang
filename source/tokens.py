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

import keywords as Keywords
import function as Function
import variable as Variable
import table as Table
import boolean as Boolean
import strings as Strings
import exports as Exports
import anonymousfunction as Anon

tokens = [
   [Keywords.BOOLEAN, Boolean.handle],
   [Keywords.TABLE, Table.handle],
   #[Keywords.VARIABLE, Variable.handle],
   [Keywords.STRING_CONCAT, Strings.handle],
   [Keywords.EXPORTS, Exports.handle],
   [Keywords.FUNCTION_BLOCK, Function.handle], # FUNCTIONS
   [Keywords.ANONYMOUS_FUNCTION_BLOCK, Anon.handle], # FUNCTIONS
]