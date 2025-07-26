from rich.console import Console

from lexicon.lexicon import *
from config import PageText
from options import Options
from tools.translatorNight import Translate
from tools.passGenNight import PassGen
from tools.QRGenNight import QRCode

import os

# * Creation of class objects
out = Options()
pagetxt = PageText()
console = Console()
transObj = Translate()
passGenObj = PassGen()
qrCodeObj = QRCode()

class Tools:

    # * Conclusion of Tools actions
    def outputOptions(self):
        out.toolsOpt()

    # * Introduction of the invitation
    def getOption(self):
        pagetxt.inviteTools()
        self.toolsInvite = console.input(f"\n{pagetxt.invToolsColor}> [/]")
    
    # * Return to Main page
    def pageReturnMain(self):
        if self.toolsInvite == "1":
            from functions import Functions

            os.system("clear")
            funcs = Functions()
            funcs.funcMain()

    # * Option Translator
    def translatorTool(self):
        if self.toolsInvite == "2":
            os.system("clear")
            transObj.getText()

    # * Option Password Generator
    def passGenTool(self):
        if self.toolsInvite == "3":
            os.system("clear")
            passGenObj.params()
            passGenObj.generation()
            passGenObj.outputPassword()
        
    def qrGenTool(self):
        if self.toolsInvite == "4":
            os.system("clear")
            qrCodeObj.generate()