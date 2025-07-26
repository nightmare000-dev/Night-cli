# The conclusion of possible actions

from rich.console import Console
from lexicon.lexicon import *

cons = Console()

def titleOutput(page):
    N = 1
    
    for value in page.values():
        cons.print(f"({N}) {value}", justify="center")
        N += 1

class Options:

    # * Conclusion of actions for the Main page
    def mainOpt(self):
        titleOutput(MAIN)
            
    # * Option output for Tools page
    def toolsOpt(self):
        titleOutput(TOOLS)