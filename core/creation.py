import time
import os
from .wakeup import WakeUp

class Creation(object):
    def getGhost(path: str = None):
        dbs = {}
        dbs['path'] = path
        dbs['path_worker'] = os.getcwd()

        if WakeUp(path=path).isExists():
            dbs['is'] = {}
            dbs['is']['exists'] = True
            dbs['is']['file'] = os.path.isfile(path)
            dbs['is']['dir'] = os.path.isdir(path)

            dbs['wakeup'] = {}
            dbs['wakeup']['access'] = WakeUp(path).access()

            dbs['result'] = {}
            dbs['result']['creation_time'] = time.ctime(os.path.getctime(path))
            dbs['result']['name'] = path.split(".")[-2] if dbs['is']['file'] == True else path
            dbs['result']['format'] = path.split(".")[-1] if dbs['is']['file'] == True else "unknown"

        else:
            dbs['is'] = {}
            dbs['is']['exists'] = False

        return dbs
