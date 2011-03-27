#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2011 Rodolphe Quiédeville <rodolphe@quiedeville.org>
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.
#
#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
"""generate.py create an xml file of JOSM presets

generate.py read all the subdirs and file and concatenate them. Each
directory is a group and each file is an item. A special fill namesd
'all' is added as is without add an item key.
"""

import os,sys
from time import time

def parseall(path, level=1):
    '''Parse a directory and output his content'''
    out = ''
    indent = '  '
    for num in xrange(level):
        indent += '  '
    for obj in os.listdir(path):
        if os.path.isdir(os.path.join(path, obj)):
            print indent + obj
            out += indent + '<group name="' + obj + '">' + "\n"
            out += parseall( os.path.join(path, obj), level + 1)
            out += indent + "</group>\n"
        else:
            if obj.endswith('.xml'):
                print indent + obj[:-4]
                out += "%s<!-- file : %s -->\n" % (indent, 
                                                      os.path.join(path, obj)
                                                      )
                out += open(os.path.join(path, obj),'r').read()
                out += "%s<!-- end file : %s -->\n\n" % (indent, 
                                                    os.path.join(path, obj)
                                                    )
    return out


def lastver():
    '''Search for the highest version number'''
    cur = 0
    for obj in os.listdir("./"):
        if os.path.isdir(obj) and obj.startswith('v'):
            cur = max(cur, float(obj[1:]))
    return cur


def header(version):
    '''Return the header section'''
    fullver = str(version) + "_" + str(int(time()))
    out = '<?xml version="1.0" encoding="UTF-8"?>'
    out += "\n"+'<presets xmlns="http://josm.openstreetmap.de/tagging-preset-1.0"'
    out += "\n"+ '  version="' + fullver + '"'
    out += "\n"+ '  author="HOT (Humanitarian OpenStreetMap Team)"'
    out += "\n"+ '  shortdescription="Humanitarian Data Model"'
    out += "\n"+ '  description="Humanitarian Data Model">'+"\n\n"
    return out

def footer():
    '''Return the footer section'''
    out = "</presets>"
    return out

def main(prefix):
    '''Main function'''
    version = lastver()
    if version == 0:
        print "No version found please create a vNUM dir"
        sys.exit(1)
    path = "v%s" % str(version)
    out = header(version)
    out += parseall(path)
    out += footer()
    filename = "%s-%s.xml" % (prefix, version)
    with open(filename, 'w') as f_:
        f_.write(out)
    print "\n%s was generated" % filename

if __name__ == "__main__":
    version = 4.2
    main("hdm_josm_presets")
