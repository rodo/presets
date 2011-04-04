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

import os,sys

def lastver():
    '''Search for the highest version number'''
    cur = 0
    for obj in os.listdir("./"):
        if os.path.isdir(obj) and obj.startswith('v'):
            cur = max(cur, float(obj[1:]))
    return cur

if __name__ == '__main__':
    print lastver()
