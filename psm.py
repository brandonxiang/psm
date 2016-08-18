"""Naval Fate.

Usage:
  psm ls 
  psm use <name>
  psm (-h | --help)
  psm (-v | --version)

Options:
  -h --help        Show this screen.
  -v --version     Show version.

"""

from __future__ import print_function

import os

from docopt import docopt

sources = {
    "pypi":"https://pypi.python.org/simple/",
    "douban":"http://pypi.douban.com/simple/",
    "aliyun":"http://mirrors.aliyun.com/pypi/simple/"
}

def list_source():
    print("\n")
    for key in sources:
        print(key,"\t",sources[key])
    print("\n")

def use(name):
    if name not in sources.keys():
        print("\nSource name is not in the list.\n")
    else:
        _write_file(name)
        print("\nSource is changed to %s.\n"%(name))
    
def _write_file(name):
    path = os.path.expanduser("~/.pip/pip.conf")
    file = os.path.dirname(path)
    if not os.path.exists(file):
        os.mkdir(file)
    with open(path,'w') as fp:
        str = "[global]\nindex-url = %s\n[install]\ntrusted-host = %s"%(
            sources[name], sources[name].split('/')[2])
        fp.write(str)

def main():
    arguments = docopt(__doc__, version='0.0.1')
    if arguments['ls']:
        list_source()
    if arguments['use']:
        use(arguments['<name>'])
        

if __name__ == '__main__':
    main()
