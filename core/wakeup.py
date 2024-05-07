import os
from .typings import *

class WakeUp(object):
    def __init__(self, path: str = None):
        self.fp = path

    def isExists(self) -> bool:
        return os.path.exists(self.fp)
    
    def access(self):
        if self.isExists():
            if os.path.isdir(self.fp):return DIR
            elif os.path.isfile(self.fp):return FILE
            elif os.path.ismount(self.fp):return MOUNT
            elif os.path.islink(self.fp):return LINK
        else:
            return "Path Does not Exists"
        
    def goGet(self):
        if self.isExists():
            if self.access() == DIR:
                os.chdir(self.fp)
                return os.listdir()
            else:
                return "Path Does not DIR"
        else:
            "Path Does not Exists"

    def byFile(self):
        if self.isExists():
            datas = self.goGet()
            dbs = []

            for item in datas:
                if WakeUp(item).access() == FILE:
                    dbs.append(item)
                else:pass

            return dbs
        else:
            return "<path> Does not Exists"
    
    def byDir(self):
        if self.isExists():
            datas = self.goGet()
            dbs = []

            for item in datas:
                if WakeUp(item).access() == DIR:
                    dbs.append(item)
                else:pass

            return dbs
        else:
            return "<path> Does not Exists"
    
    def byMount(self):
        if self.isExists():
            datas = self.goGet()
            dbs = []

            for item in datas:
                if WakeUp(item).access() == MOUNT:
                    dbs.append(item)
                else:pass

            return dbs
        else:
            return "<path> Does not Exists"
    
    def byLink(self):
        if self.isExists():
            datas = self.goGet()
            dbs = []

            for item in datas:
                if WakeUp(item).access() == LINK:
                    dbs.append(item)
                else:pass

            return dbs
        else:
            return "<path> Does not Exists"