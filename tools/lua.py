# Copyright (C) 2009, 2010  Gaetan Guidet
#
# This file is part of excons.
#
# excons is free software; you can redistribute it and/or modify it
# under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation; either version 2.1 of the License, or (at
# your option) any later version.
#
# excons is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301,
# USA.

from SCons.Script import *
import sys
import excons

def Require(env):
  linc, llib = excons.GetDirs("lua")
  if linc:
    env.Append(CPPPATH=[linc])
  if llib:
    env.Append(LIBPATH=[llib])

  if sys.platform == "win32":
    env.Append(CPPDEFINES=["LUA_BUILD_AS_DLL"])
    env.Append(LIBS=["lua51"])
  
  else:
    env.Append(LIBS=["lua"])
  
  #elif sys.platform == "darwin":
  #  # Do not link lua static lib [would duplicate core]
  #  # But add linkflags so OSX doesn't complain about unresolved symbols
  #  env.Append(LINKFLAGS = " -undefined dynamic_lookup")
  #else:
  #  # Do not link lua static lib [would duplicate core]
  #  # Only do it for final executable [using LinkLUA]
  #  pass

def ModulePrefix():
  return "lib/lua/"

def ModuleExtension():
  return ".so"
