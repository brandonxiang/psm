"""Naval Fate.
Usage:
  psm ls    
  psm use <name>
  psm current
  psm add <name> <url>
  psm delete <name>
  psm (-h | --help)
  psm (-v | --version)
Options:
  -h --help        Show this screen.
  -v --version     Show version.
"""

from __future__ import print_function
import json
import os
from typing import Dict
from docopt import docopt
import configparser


PSMRC = os.path.expanduser("~/.psmrc")

sources = {
    "pypi":"https://pypi.python.org/simple/",
    "douban":"http://pypi.douban.com/simple/",
    "aliyun":"http://mirrors.aliyun.com/pypi/simple/",
    "thu1":"https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple/",
    "thu2": 'https://pypi.tuna.tsinghua.edu.cn/simple/',
    "ustc":"http://pypi.mirrors.ustc.edu.cn/simple/",

}

def list_source():
    _sources = _read_config()
    print("\n")
    for key in _sources:
        print(key,"\t",_sources[key])
    print("\n")

def use(name: str):
    _sources = _read_config()
    if name not in _sources.keys():
        print("\nSource name is not in the list.\n")
    else:
        _write_pip_conf(name)
        print("\nSource is changed to %s.\n"%(name))

def add(name: str, url: str):
    _sources = _read_config()
    if name in _sources.keys():
        print("\nSource name is already in the list.\n")
    else:
        _sources[name] = url
        _write_config(_sources)
        print("\nSource is added.\n")
    return _sources

def delete(name: str):
    _sources = _read_config()
    if name not in _sources.keys():
        print("\nSource name is not in the list.\n")
    else:
        del _sources[name]
        _write_config(_sources)
        print("\nSource is deleted.\n")
    
def _write_pip_conf(name: str):
    _sources = _read_config()
    path = os.path.expanduser("~/.pip/pip.conf")
    file = os.path.dirname(path)
    if not os.path.exists(file):
        os.mkdir(file)

    conf = configparser.ConfigParser()
    conf.read(path)
    if not conf.has_section('global'):
        conf.add_section('global')
    if not conf.has_section('install'):
        conf.add_section('install')
    conf.set("global", "index-url", _sources[name])
    conf.set("install", "trusted-host", _sources[name].split('/')[2])
    with open(path,'w') as fp:
        conf.write(fp)

def _read_config() -> Dict[str, str]:
    path = os.path.expanduser(PSMRC)
    conf = configparser.ConfigParser()
    conf.read(path)
    if conf.has_section('global'):
        config = conf.get("global", "config")
        if config is not None:
            return json.loads(config)
    return sources

def _write_config(_sources: Dict[str, str]):
    path = os.path.expanduser(PSMRC)
    conf = configparser.ConfigParser()
    conf.read(path)

    if not conf.has_section('global'):
        conf.add_section('global')

    conf.set("global", "config", json.dumps(_sources))
    with open(path, 'w') as fp:
        conf.write(fp)

def current():
    conf = configparser.ConfigParser()
    path = os.path.expanduser("~/.pip/pip.conf")
    conf.read(path)
    index_url = conf.get("global", "index-url")
    _sources = _read_config()
    for key in _sources:
        if index_url == _sources[key]:
            print("\nCurrent source is %s"%key)
            print("Current url is %s\n"%index_url)
            break
    else:
         print("\nUnknown source\n")

def main():
    arguments = docopt(__doc__, version='0.2.0')

    if arguments['ls']:
        list_source()
    if arguments['use']:
        use(arguments['<name>'])
    if arguments['current']:
        current()
    if arguments['add']:
        add(arguments['<name>'], arguments['<url>'])
    if arguments['delete']:
        delete(arguments['<name>'])

if __name__ == '__main__':
    main()
