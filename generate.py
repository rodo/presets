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

import os

def parseall(path, level=1):
    '''Parse a directory and output his content'''
    out = ''
    indent = '  '
    for num in xrange(level):
        indent += '  '
    for obj in os.listdir(path):
        if os.path.isdir(os.path.join(path, obj)):
            out += indent + '<group name="' + obj + '">' + "\n"
            out += parseall( os.path.join(path, obj), level + 1)
            out += indent + "</group>\n"
        else:
            if not obj.endswith('~'):
                out += "\n%s<!-- begin : %s -->\n" % (indent, 
                                                      os.path.join(path, obj)
                                                      )
                if obj == 'all':
                    out += open(os.path.join(path, obj),'r').read()
                else:
                    out += '<item name="'+obj+'">' + "\n"
                    out += open(os.path.join(path, obj),'r').read()
                    out += "</item>\n"
                out += "\n%s<!-- end : %s -->\n" % (indent, 
                                                    os.path.join(path, obj)
                                                    )
    return out


def header():
    '''Return the header section'''
    out = '<?xml version="1.0"?>'
    out += "\n<presets>\n"
    return out

def footer():
    '''Return the footer section'''
    out = "</presets>"
    return out

def main(path):
    '''Main function'''
    out = header()
    out += parseall(path)
    out += footer()
    print out

if __name__ == "__main__":
    version = 4.2
    main("v%s" % str(version))
