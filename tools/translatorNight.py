from rich.console import Console
from mtranslate import translate
from string import ascii_lowercase

from config import PageText

# * Creation of class objects
pagetxt = PageText()
console = Console()

class Translate:
    def getText(self):
        pagetxt.titleTranslator()

        userTxt = console.input("\n[bold cyan]Enter the text: [/]")
        chars = "!@#$%^&*()<>?1234567890-=+/~№;:.,` '|" + ascii_lowercase

        # * Language definition
        if all(char.lower() in chars for char in userTxt):
            translatedEN = translate(userTxt, to_language="ru")
            console.print(f"[bold green]Translated:[/] {translatedEN}")

        else:
            translatedRU = translate(userTxt, to_language="en")
            console.print(f"[bold green]Translated:[/] {translatedRU}")