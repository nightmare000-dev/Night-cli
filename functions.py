# Functions

from config import PageText
from pages.toolsPage import Tools

import os

def cls(): os.system("clear")

# * Creation of class objects
pagetxt = PageText()
pageTools = Tools()

class Functions:

    # * Exit function
    def funcExit(self): exit()
    
    # * Departure to Main
    def funcMain(self):
        from main import Main 
        objMain = Main()
        objMain.MainPage() 

    # * Departure to the ABOUT NIGHT page
    def funcAbout(self):
        cls()

    # * Departure to the tool page
    def funcTools(self):
        cls()
        pagetxt.pageTools()
        pageTools.outputOptions()
        pageTools.getOption()
        pageTools.pageReturnMain()
        pageTools.translatorTool()
        pageTools.passGenTool()
        pageTools.qrGenTool()