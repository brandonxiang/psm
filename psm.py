"""Naval Fate.
Usage:
  psm ls
  psm use <name>
  psm show
  psm (-h | --help)
  psm (-v | --version)
Options:
  -h --help        Show this screen.
  -v --version     Show version.
"""

from __future__ import print_function

import os
try:
    import configparser
except:
    import ConfigParser as configparser


from docopt import docopt

sources = {
    "pypi":"https://pypi.python.org/simple/",
    "douban":"http://pypi.douban.com/simple/",
    "aliyun":"http://mirrors.aliyun.com/pypi/simple/",
    "qinghua":"https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/"
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

def show():
    conf = configparser.ConfigParser()
    path = os.path.expanduser("~/.pip/pip.conf")
    conf.read(path)
    index_url = conf.get("global", "index-url")
    for key in sources:
        if index_url == sources[key]:
            print("\nCurrent source is %s\n"%key)
            break
    else:
         print("\nUnknown source\n")

def main():
    arguments = docopt(__doc__, version='0.1.0')

    if arguments['ls']:
        list_source()
    if arguments['use']:
        use(arguments['<name>'])
    if arguments['show']:
        show()
        

if __name__ == '__main__':
    main()
