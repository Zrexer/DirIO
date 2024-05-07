from rich import print as Print
import sys

commands: dict = {}

class console(object):
    def show(obj: object):
        Print(obj)

class BufferList(object):
    def __init__(self,
                 List: list = [],
                 ):
        
        self.list = List
        
    def parse(self):
        bfd = {}

        for i in range(len(self.list)):
            bfd["_"+str(i+1)] = self.list[i]

        return bfd
    
    def isexists(self, target):
        if target in self.list:
            return True
        else:return False
    
    def indexexists(self, target):
        if target in self.list:
            return self.list.index(target)
        else:return False

    def isinfrontof(self, target, indexes):
        isit = False

        if target in self.list:
            try:
                indx = self.list.index(target)
                if indx == indexes:
                    isit = True
                else:isit = False
            except Exception as e:return e
        
        return isit

class BufferConsole(object):
    def __init__(self):

        self.data = []

    def __setcommands__(self, __key, __value):
        commands[__key] = __value
        return commands
    
    def getDictArgv(self):
        return BufferList(sys.argv).parse()
    
    def addFlag(self, *flags, mode: str = "in_front_of"):
        flg = list(flags)
        for i in range(len(flg)):
            self.__setcommands__(str(i+1), flg[i])

        if mode == "in_front_of":
            for key, val in BufferConsole().getDictArgv().items():
                if str(val) in flg:
                    keyx = int(str(key).replace("_", ""))
                    keyx += 1
                    if not f"_{keyx}" in BufferConsole().getDictArgv().keys():
                        self.data.append("Null")
                        pass
                    else:
                        self.data.append(BufferConsole().getDictArgv()[f"_{keyx}"])
                        pass
                
                else:
                    pass

            return self.data