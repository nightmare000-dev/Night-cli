from pyfiglet import Figlet
from rich.console import Console

from lexicon.lexicon import *
from options import Options
from config import PageText
from functions import Functions

import os

os.system("clear")

# * Creation of class objects
console = Console()
out = Options()
pagetxt = PageText()
funcs = Functions()

class Main:
    def MainPage(self):
        pagetxt.pageMain() # * display the page title
        out.mainOpt() # * display of actions

        # * Creation of an invitation and applying a configuration to it
        pagetxt.inviteMain()
        mainInvite = console.input(f"\n{pagetxt.invMainColor}> [/]")

        if mainInvite in ["1", "2", "3"]:
            if mainInvite == "1": pass
            elif mainInvite == "2": funcs.funcTools()
            elif mainInvite == "3": funcs.funcExit()

        else: pass

if __name__ == "__main__":
    while True:
        objMain = Main()
        objMain.MainPage()
        console.input("\n[bold magenta]Press ENTER to continue...")
        os.system("clear")