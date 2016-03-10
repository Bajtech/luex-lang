#*- encoding: utf8 -*-

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

FUNCTION_BLOCK                            = "(fn \w+\s*\(.*?\)\s*:.+?(?<=:fn))"
FUNCTION_TOP                              = "(fn \w+\s*\(.*?\)\s*:)"
WHEN                                      = "fn \w+\s*\(.*?\)\s*when\s*(.+?)(?<=:)"

ANONYMOUS_FUNCTION_BLOCK                  = "(fn\s*\(.*?\)\s*:.+?(?<=:fn))"
ANONYMOUS_FUNCTION_TOP                    = "(fn\s*\(.*?\)\s*:)"
ANONYMOUS_WHEN                            = "fn\s*\(.*?\)\s*when\s*(.+?)(?<=:)"

VARIABLE                                  = "^[l\s+|\w+].*\."
LOCAL_VARIABLE                            =  "l "
TABLE                                     = "=\s*table"
BOOLEAN                                   = "[>>|==|<=|=>|<|>]\s*(no|yes|off|on|ki|be|igen|nem|empty)"

STRING_CONCAT                             = "#{.*}"

EXPORTS                       = "call>>\w+>>\w+\(\w*\)"