#!/usr/bin/python

import os

def parseall(path, level=1):
    out = ''
    indent = '  '
    for num in xrange(level):
        indent += '  '
    for obj in os.listdir(path):
        if os.path.isdir(os.path.join(path,obj)):
            out += indent + '<group name="'+obj+'">' + "\n"
            out += parseall( os.path.join(path,obj), level + 1)
            out += indent + "</group>\n"
        else:
            out += "\n%s<!-- begin : %s -->\n" % (indent, os.path.join(path,obj))
            if obj == 'all':
                out += open(os.path.join(path,obj),'r').read()
            else:
                out += '<item name="'+obj+'">' + "\n"
                out += open(os.path.join(path,obj),'r').read()
                out += "</item>\n"
            out += "\n%s<!-- end : %s -->\n" % (indent, os.path.join(path,obj))
    return out


def header():
    out = '<?xml version="1.0"?>'
    out += "\n<presets>\n"
    return out

def footer():
    out = "</presets>"
    return out


def main(path):
    out = header()
    out += parseall(path)
    out += footer()
    print out

if __name__ == "__main__":
    version = 4.2
    main("v%s" % str(version))
