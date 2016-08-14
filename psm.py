from __future__ import print_function
import argparse
import os


sources = {
    "pypi":"https://pypi.python.org/simple/",
    "douban":"http://pypi.douban.com/simple/",
    "aliyun":"http://mirrors.aliyun.com/pypi/simple/"
}

def list():
    for key in sources:
        print(key,sources[key])

def use(name):
    if name not in sources.keys():
        print("Source name is not in the list.")
    else:
        _create_file(name)
        print("change to %s"%(name))
    
def _create_file(name):
    path = os.path.expanduser("~/.pip/pip.conf")
    file = os.path.dirname(path)
    if not os.path.exists(file):
        os.mkdir(file)
    with open(path,'w') as fp:
        str = """
[global]
index-url = %s
[install]
trusted-host = %s
        """%(sources[name],sources[name])
        fp.write(str)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u","--use", help="change pypi source")
    parser.add_argument("-l","--list", help="list all pypi source",
                        action="store_true")
                        
    args = parser.parse_args()
    if args.list:
        list()
    if args.use:
        use(args.use)
        

if __name__ == '__main__':
    main()