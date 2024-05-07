from core.wakeup import WakeUp
from core.creation import Creation
from core.typings import *
from core.Object import console, BufferConsole

import sys

def helpPage() -> str:
    console.show(" dirio [ '-h', '--help' ]")
    console.show("   -p: To set Global <path>")
    console.show("   ")
    console.show("   --wakeup: Use 'Wake Up' <class> to handle Many things :::")
    console.show("     methods for 'Wake Up' <class> ( '--isex', '--go-get', '--access', '--byfile', '--bydir', '--bymount', '--bylink' )")
    console.show("   ")
    console.show("  --ghost: Ghost <function> is imported from <class> 'Creation' to give all <informations> about the input path :::")
    console.show("     methods for 'Ghost' <function> ( None )")
    console.show("   ")

hpls = BufferConsole().addFlag("-h", "--help")
wku = BufferConsole().addFlag("--wakeup")
ghost = BufferConsole().addFlag("--ghost")
pa = BufferConsole().addFlag("-p")
methods = {
    "access": BufferConsole().addFlag("--access"),
    "bydir": BufferConsole().addFlag("--bydir"),
    "byfile": BufferConsole().addFlag("--byfile"),
    "bylink": BufferConsole().addFlag("--bylink"),
    "bymount": BufferConsole().addFlag("--bymount"),
    "goget": BufferConsole().addFlag("--go-get"),
    "isex": BufferConsole().addFlag("--isex")
}

if len(hpls) >= 1:
    helpPage()
    exit()

else:
    if "--show-stat" in sys.argv:
            console.show(methods)

    if len(pa) >= 1:
        pa = pa[0]

        if pa == "Null":
            console.show("<path> Does not Selected")
            exit()
    
        if len(methods['access']) >= 1:
            console.show(WakeUp(pa).access())
        
        if len(methods['bydir']) >= 1:
            console.show(WakeUp(pa).byDir())

        if len(methods["byfile"]) >= 1:
            console.show(WakeUp(pa).byFile())

        if len(methods["bylink"]) >= 1:
            console.show(WakeUp(pa).byLink())

        if len(methods["bymount"]) >= 1:
            console.show(WakeUp(pa).byMount())
        
        if len(methods["goget"]) >= 1:
            console.show(WakeUp(pa).goGet())

        if len(methods['isex']) >= 1:
            console.show(WakeUp(pa).isExists())

        if len(ghost) >= 1:
            console.show(Creation.getGhost(pa))